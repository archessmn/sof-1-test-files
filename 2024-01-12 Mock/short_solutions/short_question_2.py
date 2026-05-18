import math

sphere = tuple[float, float, float, float]


def union(oa: set[sphere], ob: set[sphere]) -> set[sphere]:
    return set(filter(lambda sa: not any(map(lambda sb: comprisedCalc(sa, sb), oa.union(ob))), oa.union(ob)))


def comprisedCalc(s1: sphere, s2: sphere) -> bool:
    return False if s1 == s2 else math.sqrt(pow(s1[0] - s2[0], 2) + pow(s1[1] - s2[1], 2) + pow(s1[2] - s2[2], 2)) + s1[3] <= s2[3]
