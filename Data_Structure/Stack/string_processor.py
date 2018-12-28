from stack import Stack
class StringProcessor : 
    def __init__(self) : 
        self.stack = Stack() 
        self.bird = Stack()

    def reverse(self, name) : 
        return name[::-1] 
    def process_sequence(self, text) : 
        s = ""
        for i in text : 
            if i.isalpha() : 
                self.stack.push(i) 
            elif i == "*" : 
                s += self.stack.pop()
        return s 
    def binary_string(self, num) : 
        return str(bin(num))[2:]
    def is_balanced(self, string) :
        balance = {
            "{" : "}" , 
            "[" : "]" , 
            "(" : ")" ,
        }
        keys = balance.keys()
        values = balance.values() 
        for x in string : 
            if x in keys : 
                self.stack.push(x)
            elif x in values : 
                self.bird.push(x)
                if len(self.stack.items) == len(self.bird.items) : 
                    length = len(self.stack.items)
                    for i, zohan in enumerate(self.stack.items) : 
                        if not balance[zohan] == self.bird.items[len(self.stack.items) - i - 1] : 
                            self.stack.clear()
                            self.bird.clear() 
                            return False
                    self.stack.clear()
                    self.bird.clear() 
        if len(self.stack.items) == 0 and len(self.bird.items) == 0 : 
            return True 
        self.stack.clear()
        self.bird.clear() 
        return False
