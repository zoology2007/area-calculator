def area():
    area_calculator = input("Please enter the shape you want the area of:")
    value = 0
    if area_calculator =="square":
        side = int (input("Please enter the sides of the square"))
        value = value + (side*side)
    elif area_calculator == "rectangle":
        length = int (input("Please enter the length of the rectangle"))
        breadth = int (input("Please enter the breadth of the rectangle"))
        value = value + (length*breadth)
    elif area_calculator == "triangle":
        base = int (input("Please enter the base of the triangle"))
        height = int (input("Please enter the height of the triangle"))
        value = value + (0.5*base*height)
    elif area_calculator == "circle":
        radius = int (input("Please enter the radius of the circle"))
        value = value + (3.14*radius*radius)
    else :
        print("Select a valid shape")
    print(value)
area()