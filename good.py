# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.

# You receive an array with your peers' test scores. Now calculate the average and compare your score!

# Return True if you're better, else False!
# Note:

# Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!


# def better_than_average(class_points, your_points):
#     cls_point = sum(class_points) / len(class_points)
#     if your_points > cls_point:
#         return True
#     else:
#         return False
# print(better_than_average(2,3))

def better_score(class_point,your_points):
    average = sum(class_point) / len(class_point)
    if your_points > average:
        return True
    else:
        return False
class_point = [1,2,3]
your_points = 7
print(better_score(class_point,your_points))




