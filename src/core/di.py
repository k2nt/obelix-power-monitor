from dependency_injector import providers, containers


class App(containers.DeclarativeContainer):
    """Application dependency injection container."""
    # Core

    config_dict = providers.Configuration(json_files=["cfg.json"])
    
    
def build():
    """Build dependency injection."""
    # dependency injection

    app_di = App()
    app_di.init_resources()

    # only inject into service layer
    
    app_di.wire(
        modules=[
            "src.main",
            ]
        )    
