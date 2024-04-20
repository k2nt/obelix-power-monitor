from typing import List

from dependency_injector import providers, containers

from src import service
from src import repo


class App(containers.DeclarativeContainer):
    """Application dependency injection container."""
    # infra
    config = providers.Configuration(json_files=["cfg.json"])
    
    # repos
    power_meter_repo = providers.Factory(
        repo.PowerMeter,
        sample_per_second=config.POWER_METER_SAMPLE_PER_SECOND,
        data_folder=config.POWER_METER_FOLDER,
        )
    
    # services
    power_monitor_service = providers.Factory(
        service.PowerMonitor,
        r=power_meter_repo,
        )
    
    
def build(modules: List[str]):
    """Build dependency injection."""
    app_di = App()
    app_di.init_resources()
    app_di.wire(modules=modules)
