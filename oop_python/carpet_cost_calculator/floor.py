class Floor:

    def __init__(self, _width, _length):
        if _width < 0:
            self.width = 0
        elif _length < 0:
            self.length = 0
        else:
            self.width = _width
            self.length = _length
    
    def get_area(self):
        return self.length * self.width



    