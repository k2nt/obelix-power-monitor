from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query
from dependency_injector.wiring import Provide, inject

from src.infra import di
from src import service
from src.domain import response


router = APIRouter(prefix='/monitor')


@router.get("/{obelix_node_name}/energy")
@inject
async def get_energy_consumption(
        obelix_node_name: Annotated[str, Path(title="Obelix node name")],
        t_seconds: Annotated[int, Query(alias="tsec")] = 15,
        m: service.PowerMonitor = Depends(Provide[di.App.power_monitor_service]),
):    
    print(repr(m))
    return response.ok(data={'node': obelix_node_name, 't': t_seconds})
