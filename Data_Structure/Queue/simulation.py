class Simulation : 
    def __init__(self, process_rate, min_req_rate, max_req_rate) : 
        self.process_rate = process_rate
        self.min_req_rate = min_req_rate
        self.max_req_rate = max_req_rate
    def step(self, requests) : 
        loss_req = 0 
        