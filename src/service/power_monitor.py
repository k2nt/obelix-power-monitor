from typing import Any, Dict, List
from dataclasses import dataclass

import os
from pathlib import Path

from src.infra.logging import logger_store


logger = logger_store.get('default')


@dataclass(init=True, repr=True)
class PowerMonitor:
    ...
            
            
def new(data_folder: Path | str) -> PowerMonitor:
    data_folder = Path(data_folder)
        
    # get nodes being monitored for power
    file_names = os.listdir(data_folder)
    
    # open persistent filestreams to each node's power data
    fs: Dict[str, Any] = dict()
    for n in file_names:
        node = Path(n).stem
        fs[node] = open(data_folder / n)
            
            
def sample_energy_watts(
        m: PowerMonitor, 
        node_name: str,
        t_seconds: int
) -> float:
    pass
