from typing import Any, Dict, List
from dataclasses import dataclass

import os
from pathlib import Path


@dataclass(frozen=True)
class PowerMonitor:
    def __init__(self, data_folder: Path | str):        
        data_folder = Path(data_folder)
        
        # get nodes being monitored for power
        file_names = os.listdir(self.data_folder)
        self.active_nodes: List[str] = [Path(n).stem for n in file_names]
        
        # open persistent filestreams to each node's power data
        self._fs: Dict[str, Any] = dict()
        for n in file_names:
            node = Path(n).stem
            self._fs[node] = open(data_folder / n)
            
            
def sample_energy_watts(
        m: PowerMonitor, 
        node_name: str,
        t_seconds: int
) -> float:
    pass
