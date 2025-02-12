def task2():

    coordinates_of_the_center = 'center.txt'
    coordinate_of_the_points = 'points.txt'

    with open(coordinates_of_the_center, 'r') as file:
        x, y = map(float, file.readline().split())
        radius = float(file.readline().strip())

    with open(coordinate_of_the_points, 'r') as file:
        points = [line.strip() for line in file if line.strip()]

    for point in points:
        t1, t2 = map(float, point.split())
        distance_squared = (x - t1) ** 2 + (y - t2) ** 2
        radius_squared = radius ** 2
        if distance_squared == radius_squared:
            print(0)
        elif distance_squared < radius_squared:
            print(1)
        else:
            print(2)

task2()
