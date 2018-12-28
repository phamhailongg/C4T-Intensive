class Stack : 
    items = []
    def push(self, n) :
        self.items.append(n)
    def pop(self) : 
        return self.items.pop()
    def is_empty(self) : 
        return self.items == [] 
    def clear(self) : 
        self.items = []
    def __str__(self) : 
        if self.is_empty():
            return ""
        return " ".join(str(x) for x in self.items)

