import math


def radius_sum(r1, r2):

    return r1 + r2


def euclid_distance(x1, y1, x2, y2):

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def has_intersection(circle_1, circle_2):

    d = euclid_distance(circle_1['x'], circle_1['y'], circle_2['x'], circle_2['y'])
    r_sum = radius_sum(circle_1['r'], circle_2['r'])
    r_diff = abs(circle_1['r'] - circle_2['r'])


    if d > r_sum:
        return {"is_intersection": False, "intersections_count": 0}


    if math.isclose(d, r_sum):
        return {"is_intersection": True, "intersections_count": 1}


    if d < r_diff:
        if math.isclose(d, r_diff):
            return {"is_intersection": True, "intersections_count": 1}
        return {"is_intersection": False, "intersections_count": 0}


    return {"is_intersection": True, "intersections_count": 2}