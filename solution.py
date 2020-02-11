import matplotlib.pyplot as plt
import numpy as np

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['a', 'b', 'c'])


def calculate_length(p1: Point, p2: Point) -> float:
    """Calculate length line segment formed by two points"""
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5


def calculate_line(p1: Point, p2: Point) -> Line:
    """Calculate equation of a straight line ax + by + c = 0"""
    a = p2.y - p1.y
    b = p1.x - p2.x
    c = p2.x * p1.y - p1.x * p2.y
    return Line(a, b, c)


def calculate_r_incircle(p1: Point, p2: Point, p3: Point) -> float:
    """Calculate radius incirle triangle formed by three points"""
    side1 = calculate_length(p1, p2)
    side2 = calculate_length(p1, p3)
    side3 = calculate_length(p2, p3)
    p = (side1 + side2 + side3) / 2
    r = ((p - side1) * (p - side2) * (p - side3) / p)**0.5
    return r


def calculate_center_incircle(p1: Point, p2: Point, p3: Point) -> Point:
    """Calculate coordinates center of incirle triangle by three points"""
    bis1 = calculate_bisector(p1, p2, p3)
    bis3 = calculate_bisector(p3, p1, p2)
    result = calculate_point_of_intersection_two_lines(bis1, bis3)
    return result


def calculate_point_of_intersection_two_lines(line1: Line, line2:Line) -> Point:
    """Calculate coodrinates point of intersection two lines"""
    a = np.array([[line1.a, line1.b], [line2.a, line2.b]])
    b = np.array([-line1.c, -line2.c])
    x = np.linalg.solve(a, b)
    return Point(x[0], x[1])


def calculate_bisector(vertex: Point, opposite1: Point, opposite2: Point) -> Line:
    """Calculate equation of a straight line in ax + by + c = 0
       that bisector angle with vertex"""
    # Найдем уравнение сторон, прилегающих к улгу
    side1 = calculate_line(vertex, opposite1)
    side2 = calculate_line(vertex, opposite2)
    
    # Рассчитаем уравнение двух биссектрис
    p1 = (side1.a**2 + side1.b**2)**0.5
    p2 = (side2.a**2 + side2.b**2)**0.5
    
    a1 = side1.a * p2 + side2.a * p1
    a2 = side1.a * p2 - side2.a * p1

    b1 = side1.b * p2 + side2.b * p1
    b2 = side1.b * p2 - side2.b * p1

    c1 = side1.c * p2 + side2.c * p1
    c2 = side1.c * p2 - side2.c * p1

    # Определим, какая биссектрисса является биссектриссой внутреннего угла

    var1_dot1 = a1 * opposite1.x + b1 * opposite1.y + c1
    var1_dot2 = a1 * opposite2.x + b1 * opposite2.y + c1

    var2_dot1 = a2 * opposite1.x + b2 * opposite1.y + c2
    var2_dot2 = a2 * opposite2.x + b2 * opposite2.y + c2

    if (var1_dot1 * var1_dot2) < 0:
        bis = Line(a1, b1, c1)
    elif (var2_dot1 * var2_dot2) < 0:
        bis = Line(a2, b2, c2)
    else:
        raise ValueError("Can't calculate bisector")

    return bis


def calculate_perpendicular_line(line: Line, dot: Point) -> Line:
    """Calculate line perpendicular line and passed throu dot"""
    return Line(line.b, -line.a, line.a * dot.y - line.b * dot.x)


def show_graph(points, 
               center_incircle: Point,
               radius_incircle: float,
               segments):
    """Show graph"""
    
    fig, ax = plt.subplots()
    
    # рисуем треугольник
    p1, p2, p3 = points
    ax.plot([p1.x, p2.x], [p1.y, p2.y], color='black')
    ax.plot([p1.x, p3.x], [p1.y, p3.y], color='black')
    ax.plot([p2.x, p3.x], [p2.y, p3.y], color='black')

    circle1 = plt.Circle((center_incircle.x, center_incircle.y), radius_incircle, color='green', fill=False)
    ax.add_artist(circle1)
    
    # рисуем центр окружности
    ax.plot([center_incircle.x], [center_incircle.y], marker='o', markersize=2, color='green')

    for segment in segments:
        p1, p2 = segment
        ax.plot([p1.x, p2.x], [p1.y, p2.y], color='black')

    plt.axis('scaled')
    plt.show()


def calculate_segment(p1, p2, center, L):
    side = calculate_line(p1, p2)
    perpendicular = calculate_perpendicular_line(side, center)
    point = calculate_point_of_intersection_two_lines(side, perpendicular)

    d = ((center.x - point.x)**2 + (center.y - point.y)**2) ** 0.5
    coeff = L / 2 / d

    x1 = point.x + (center.x - point.x) * coeff
    y1 = point.y + (center.y - point.y) * coeff
    x2 = point.x - (x1 - point.x)
    y2 = point.y - (y1 - point.y)
    return (Point(x1, y1), Point(x2, y2))


# read data
p1 = Point(*tuple(map(float, input("Please enter x1 and y1: ").split())))
p2 = Point(*tuple(map(float, input("Please enter x2 and y2: ").split())))
p3 = Point(*tuple(map(float, input("Please enter x3 and y3: ").split())))
L = float(input("Please enter L: "))
visualisation = input("Show visualization? [y/n]: ").lower() == 'y'

# does the task have a solution?
r = calculate_r_incircle(p1, p2, p3)

if (L / 2) >= r:
    print("Task doesn't have a solution")
else:
    center = calculate_center_incircle(p1, p2, p3)

    segment1 = calculate_segment(p1, p2, center=center, L=L)
    segment2 = calculate_segment(p1, p3, center=center, L=L)
    segment3 = calculate_segment(p2, p3, center=center, L=L)

    print(segment1, segment2, segment3)
    
    if visualisation:
        show_graph([p1, p2, p3],
                   center_incircle=center,
                   radius_incircle=r,
                   segments=[segment1, segment2, segment3])
