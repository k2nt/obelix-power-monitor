from typing import Any, Dict

import os
from pathlib import Path

import pandas as pd


class PowerMeter:
    def __init__(self, sample_per_seconds: float, data_folder: Path | str):
        data_folder = Path(data_folder)
        
        self.sample_per_seconds: float = sample_per_seconds
        
        # get nodes being monitored for power
        file_names = os.listdir(data_folder)
    
        # open persistent filestreams to each node's power data
        self._fs: Dict[str, Any] = dict()
        for n in file_names:
            node = Path(n).stem
            self._fs[node] = open(data_folder / n)
    
    def is_measuring_node(self, node_name: str) -> bool:
        return node_name in list(self._fs.keys())
    
    def sample_energy_watts(self, node_name: str, t_sec: int) -> float:
        if not self.is_measuring_node(node_name):
            raise KeyError(f"node '{node_name}' not found")
        
        df = pd.read_csv(self._fs[node_name], on_bad_lines='skip')
        t = t_sec * self.sample_per_second
        energy_watts_samples = df.tail(t)[:, -1]
        return energy_watts_samples.sum()
