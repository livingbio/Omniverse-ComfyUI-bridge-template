import omni.ext
import omni.kit.ui
from omni.services.core import main

import carb
import os
from fastapi.staticfiles import StaticFiles

from .services.viewport_capture import router as capture_router
from .services.viewport_record import router as record_router

# For convenience, let's also reuse the utility methods we already created to handle and format the storage location of
# the captured images so they can be accessed by clients using the server, once API responses are issued from our
# Service:
from . import ext_utils

_global_instance = None


class ComfyUIConnectorExtension(omni.ext.IExt):
    """Comfy UI Connector Extension"""

    WINDOW_NAME = "ComfyUI"
    MENU_PATH = f"Window/GliaCloud Custom/{WINDOW_NAME}"

    def on_startup(self, ext_id):
        carb.log_warn("Extension started")
        global _global_instance
        _global_instance = self

        # store extension id in Carbonite
        _settings = carb.settings.get_settings()
        _settings.set("exts/omni.comfyui.connector.core/ext_id", str(ext_id))

        # At this point, we register our Service's `router` under the path we gave our API using the settings system,
        # to facilitate its configuration and to ensure it is unique from all other extensions we may have enabled:
        _path = ext_utils.get_setting_service_path()

        main.register_router(
            router=capture_router,
            prefix=_path,
        )

        main.register_router(
            router=record_router,
            prefix=_path,
        )

        # Proceed to create a temporary directory in the USD Composer application file hierarchy where captured stage
        # images will be stored, until the application is shut down:
        _local_resource_directory = ext_utils.get_local_resource_directory()
        if not os.path.exists(_local_resource_directory):
            os.makedirs(_local_resource_directory)

        # Register this location as a mount, so its content is served by the web server bundled with the Omniverse
        # application instance, thus making the captured image available on the network:
        main.register_mount(
            path=ext_utils.get_full_resource_path(), app=StaticFiles(directory=_local_resource_directory, html=True)
        )

    def on_shutdown(self):
        global _global_instance
        _global_instance = None

        _path = ext_utils.get_setting_service_path()

        # When disabling the extension or shutting down the instance of the Omniverse application, let's make sure we
        # also deregister our Service's `router` in order to avoid our API being erroneously advertised as present as
        # part of the OpenAPI specification despite our handler function no longer being available:
        main.deregister_router(
            router=capture_router,
            prefix=_path,
        )

        main.deregister_router(
            router=record_router,
            prefix=_path,
        )

        main.deregister_mount(path=ext_utils.get_full_resource_path())

        carb.log_warn("Extension shut down.")

    @staticmethod
    def get_instance():
        global _global_instance
        return _global_instance
