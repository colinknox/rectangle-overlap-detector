class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_left_x(self):
        return min(self.x1, self.x2)
    
    def get_right_x(self):
        return max(self.x1, self.x2)
    
    def get_bottom_y(self):
        return min(self.y1, self.y2)
    
    def get_top_y(self):
        return max(self.y1, self.y2)
    
    def overlaps(self, other):
        condition_one = self.get_left_x() <= other.get_right_x() # True
        condition_two = self.get_right_x() >= other.get_left_x() # False
        condition_three = self.get_bottom_y() <= other.get_top_y()
        condition_four = self.get_top_y() >= other.get_bottom_y()

        if condition_one and condition_two and condition_three and condition_four:
            return True
        else:
            return False