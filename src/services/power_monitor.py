from dataclasses import dataclass

import os
from pathlib import Path


@dataclass(frozen=True)
class PowerMonitor:
    def __init__(self, data_folder: Path | str):
        self.data_folder: Path = Path(data_folder)
        
        # open persistent filestreams to each node's power data
            
            
def sample_energy_watts(
        m: PowerMonitor, 
        node_name: str,
        t_seconds: int
) -> float:
    pass
