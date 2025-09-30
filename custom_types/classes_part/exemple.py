class MicroWaveManager:
    def __init__(self):
        self.status = "close"

    def open(self):
        self.status = "open"

    def close(self):
        self.status = "close"

microwave_manager = MicroWaveManager()
microwave_manager.open()
microwave_manager.close()