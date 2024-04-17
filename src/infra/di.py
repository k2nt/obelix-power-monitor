from typing import List

from dependency_injector import providers, containers


class App(containers.DeclarativeContainer):
    """Application dependency injection container."""
    config_dict = providers.Configuration(json_files=["cfg.json"])
    
    
def build(modules: List[str]):
    """Build dependency injection."""
    app_di = App()
    app_di.init_resources()    
    app_di.wire(modules=modules)
