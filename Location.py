class Location():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x},{self.y}"
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.x == other.x and
            self.y == other.y)
        else:
            return False