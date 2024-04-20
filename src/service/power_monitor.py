from src import repo


class PowerMonitor:
    def __init__(self, r: repo.PowerMeter):
        self.r = r
        
    def sample_energy_watts(self, node_name: str, t_sec: int) -> float:
        return self.r.sample_energy_watts(node_name, t_sec)
