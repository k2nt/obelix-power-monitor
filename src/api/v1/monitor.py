from typing import Annotated

from fastapi import APIRouter, Path, Query

from src.domain import response


router = APIRouter(prefix='/monitor')


@router.get("/{obelix_node_name}/energy")
async def get_energy_consumption(
        obelix_node_name: Annotated[str, Path(title="Obelix node name")],
        t_seconds: Annotated[int, Query(alias="tsec")] = 15,
):    
    return response.ok(data={'node': obelix_node_name, 't': t_seconds})
