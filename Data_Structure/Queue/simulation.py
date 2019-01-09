from random import randint
class Simulation : 
    def __init__(self, process_rate, min_req_rate, max_req_rate) : 
        self.process_rate = process_rate
        self.min_req_rate = min_req_rate
        self.max_req_rate = max_req_rate
    def run(self, cock) : 
        loss_req = 0 
        for i in range(cock) : 
            req = randint(self.min_req_rate, self.max_req_rate)
            loss = req - self.process_rate
            if loss > 0 : 
                loss_req += loss 
        return loss_req / cock