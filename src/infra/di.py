from typing import List

from dependency_injector import providers, containers

from src import service


class App(containers.DeclarativeContainer):
    """Application dependency injection container."""
    # infra
    config = providers.Configuration(json_files=["cfg.json"])
    
    # services
    power_monitor_service = providers.Factory(
        service.PowerMonitor,
        data_folder=config.POWER_DATA_FOLDER
        )
    
    
def build(modules: List[str]):
    """Build dependency injection."""
    app_di = App()
    app_di.init_resources()
    app_di.wire(modules=modules)
