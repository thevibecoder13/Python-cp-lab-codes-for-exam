import math

class Shape:
    
    def calculate(self, shape, **kwargs):
        
        if shape == "square":
            a = kwargs.get("side")
            perimeter = 4 * a
            area = a * a
        
        elif shape == "rectangle":
            l = kwargs.get("length")
            b = kwargs.get("breadth")
            perimeter = 2 * (l + b)
            area = l * b
        
        elif shape == "circle":
            r = kwargs.get("radius")
            perimeter = 2 * math.pi * r   # circumference
            area = math.pi * r * r
        
        elif shape == "triangle":   # equilateral
            a = kwargs.get("side")
            perimeter = 3 * a
            area = (math.sqrt(3)/4) * a * a
        
        else:
            return "Invalid shape"
        
        return perimeter, area


# 🔸 Driver code
s = Shape()

print("Square:", s.calculate("square", side=4))
print("Rectangle:", s.calculate("rectangle", length=5, breadth=3))
print("Circle:", s.calculate("circle", radius=2))
print("Triangle:", s.calculate("triangle", side=3))