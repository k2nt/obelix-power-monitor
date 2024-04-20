from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query
from dependency_injector.wiring import Provide, inject

from src import service
from src import repo
from src.infra import di
from src.domain import response


router = APIRouter(prefix='/monitor')


@router.get("/{node_name}/energy")
@inject
async def get_energy_consumption(
        node_name: Annotated[str, Path(title="Obelix node name")],
        t_sec: Annotated[int, Query(alias="tsec")] = 15,
        s: repo.PowerMeter = Depends(Provide[di.App.power_meter_repo])
):    
    eu = s.sample_energy_watts(node_name, t_sec)
    return response.ok(data={'eu': eu})
