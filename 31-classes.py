class Point:
    x = 0
    y = 0

    def move(self):
        print("move")
    
    def draw(self):
        print("draw")


point1 = Point()
point1.draw()

point1.x = 10
print(point1.x)

point1.z = 30
print(point1.z)

point2 = Point()
# print(point2.z)  # Error - No z attribute defined
