from lessons.CQ07.point import Point

my_point: Point = Point(3, 6)

print(my_point.x)
print(my_point.y)

my_point.scale_by(2)

print(my_point.x)
print(my_point.y)

another_point: Point = my_point.scale(3)

print(another_point.x)
print(another_point.y)