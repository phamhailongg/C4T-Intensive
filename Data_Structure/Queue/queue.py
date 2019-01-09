class Queue : 
    def __init__(self, capacity = -1) : 
        self.capacity = capacity
        self.items = []
    def is_empty(self) : 
        return not self.items 
    def insert(self, x, is_list=False):
        if not self.is_full():
            if not is_list:
                self.items.insert(0, x)
            else:
                for i in x:
                    if not self.is_full():
                        self.items.insert(0, i)
                    else:
                        break
            return True
        return False
    def remove(self, how_many = 1) : 
        return self.items.pop()
    def remove_all(self) : 
        return self.remove(self.size())
    def size(self) : 
        return len(self.items)
    def is_full(self) : 
        return self.size() == self.capacity

    def __str__(self) : 
        if self.is_empty():
            return ""
        return " ".join(str(x) for x in self.items)