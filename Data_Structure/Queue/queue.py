class Queue : 
    def __init__(self) : 
        self.items = []
    def is_empty(self) : 
        return not self.items 
    def insert(self, num) : 
        self.items.insert(0, num)
    def remove(self) : 
        return self.items.pop()
    def __str__(self) : 
        if self.is_empty():
            return ""
        return " ".join(str(x) for x in self.items)
