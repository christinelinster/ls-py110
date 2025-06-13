# Tri-Angles

def triangle(angle1, angle2, angle3):
    angles = [angle1, angle2, angle3]
    max_angle = max(angles)
    if 0 in angles or sum(angles) != 180:
        return 'invalid'
    
    if max_angle > 90:
        return 'obtuse'
    if max_angle < 90:
        return 'acute' 
    
    return 'right'


print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True