"""
把这种多角度分类分离出来，让它们独立变化，减少它们之间耦合
"""
class DrawingAPI1:
    def draw_circle(self, x, y, radius):
        print("API1.circle at {}:{} radius {}".format(x, y, radius))


class DrawingAPI2:
    def draw_circle(self, x, y, radius):
        print("API2.circle at {}:{} radius {}".format(x, y, radius))


class Circle:

    def __init__(self, x, y, radius, api):
        self.x = x
        self.y = y
        self.radius = radius
        self.api = api

    def draw(self):
        """
        >>> Circle(1,1,1,DrawingAPI1()).draw()
        API1.circle at 1:1 radius 1
        >>> Circle(1,1,1,DrawingAPI2()).draw()
        API2.circle at 1:1 radius 1
        >>> c = Circle(1,1,1,DrawingAPI1())
        >>> c.scale(2)
        >>> c.draw()
        API1.circle at 1:1 radius 2
        """
        self.api.draw_circle(self.x, self.y, self.radius)

    def scale(self, n):
        self.radius *= n


if __name__ == '__main__':
    import doctest
    doctest.testmod()