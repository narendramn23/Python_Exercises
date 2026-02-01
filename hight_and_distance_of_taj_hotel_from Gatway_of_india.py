import math


def distance_hight(tower_distance_from_gate = 100, angle_elevation_from_gateway = 25, angle_elevation_from_security = 65):
    #given

    #tower_distance_from_gate = 100
    #angle_elevation_from_gateway = 25
    #angle_elevation_from_security = 65


    ##convert to radins

    angle_elevation_from_gateway = math.radians(angle_elevation_from_gateway)
    angle_elevation_from_security = math.radians(angle_elevation_from_security)

    #hight_of tower from secuitygaurd_gate

    hight_of_tower = math.tan(angle_elevation_from_security) * 100

    print("hight of the tower is",hight_of_tower,"yards")

    # diastance_between_gateway to

    distance = hight_of_tower // math.tan(angle_elevation_from_gateway)
    print("distance between gateway of india to entrance", distance, "yards")


distance_hight()













