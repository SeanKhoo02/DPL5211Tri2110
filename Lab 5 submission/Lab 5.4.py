# Student ID : 1201201336
# Student Name : Khoo Chong Qin

def rectangle(length, width):
    Ar = length*width
    return Ar

def triangle(length, width):
    At = width*length/2
    return At

i= 0
while(i<2):
    width = float(input("Enter width: "))
    length = float(input("Enter length: "))

    area_rectangle = rectangle(length, width)
    area_triangle = triangle(length, width)

    print("Rectangle area : {:.2f}".format(area_rectangle))
    print("Triangle area : {:.2f}".format(area_triangle))

    i = i + 1