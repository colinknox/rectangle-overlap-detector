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
        condition_one = self.get_left_x() <= other.get_right_x()

        return condition_one


rectangle = Rectangle(5, 4, 8, 5)
rectangle_two = Rectangle(6, 2, 3, 8)



print(f"DEBUG: Rectangle 1 | left side = {rectangle.get_left_x()}, right side = {rectangle.get_right_x()}")
print(f"DEBUG: Rectangle 2 | left side = {rectangle_two.get_left_x()}, right side = {rectangle_two.get_right_x()}")
print(f"DEBUG: Rectangle 1 overlaps Rectangle 2 = {rectangle.overlaps(rectangle_two)}")