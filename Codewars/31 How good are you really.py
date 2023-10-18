def better_than_average(class_points, your_points):
    points_sum = 0
    for i in class_points:
        points_sum += i
    points_sum += your_points
    num_of_points = len(class_points) + 1
    avg = points_sum/num_of_points
    if your_points > avg:
        return True
    else:
        return False