import math
points=[[1,2],[3,4],[5,6],[7,8],[9,10]]
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distances.append(euclidean_distance(points[i], points[j]))

min_distance = min(distances)
print(f"Minimum distance between two points:,{min_distance:.2f}")
