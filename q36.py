36.
class Solid:
    def calculate(self, shape, **kwargs):
        if shape == "cube":
            a = kwargs.get("side")
            surface_area = 6 * a * a
            volume = a ** 3
        elif shape == "sphere":
            r = kwargs.get("radius")
            surface_area = 4 * 3.14 * r * r
            volume = (4/3) * 3.14 * r ** 3
        elif shape == "cylinder":
            r = kwargs.get("radius")
            h = kwargs.get("height")
            surface_area = 2 * 3.14 * r * (r + h)
            volume = 3.14 * r * r * h
        elif shape == "cuboid":
            l = kwargs.get("length")
            b = kwargs.get("breadth")
            h = kwargs.get("height")
            surface_area = 2 * (l*b + b*h + h*l)
            volume = l * b * h
        else:
            return "Invalid shape"
        return surface_area, volume
s = Solid()
print("Cube:", s.calculate("cube", side=3))
print("Sphere:", s.calculate("sphere", radius=2))
print("Cylinder:", s.calculate("cylinder", radius=2, height=5))
print("Cuboid:", s.calculate("cuboid", length=2, breadth=3, height=4))