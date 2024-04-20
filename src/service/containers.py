from dependency_injector import providers, containers

from src import repo
from .power_monitor import PowerMonitor


class PowerMonitorService(containers.DeclarativeContainer):
    sample_per_second = providers.Dependency()
    power_meter_folder = providers.Dependency()
    
    repo = providers.Factory(
        repo.PowerMeter,
        sample_per_second=sample_per_second,
        data_folder=power_meter_folder,
        )
    
    service = providers.Factory(
        PowerMonitor,
        r=repo,
    )
