from dependency_injector import providers, containers


class AppDI(containers.DeclarativeContainer):
    """Application dependency injection container."""
    # Core

    config_dict = providers.Configuration().from_env('.env')
    
    
def build_di():
    """Build dependency injection."""
    # Dependency injection

    app_di = AppDI()
    app_di.config_dict.from_yaml(".env")
    app_di.init_resources()

    # only inject into Service layer
    # this is to obey Clean Architecture, where Views are state-agnostic.
    app_di.wire(
        modules=[
            __name__
            ]
        )    
