

from math import pi


def volume_of_cylinder(r_in = None, r_out = None, d = 3 ): 

    #vol of hollow sphere 
    vol_of_inner_sphere = (4/3) * pi * r_in * r_in * r_in

    vlo_of_external_sphere = (4/3) * pi * r_out * r_out * r_out

    vol_of_hollow_sphere = vlo_of_external_sphere - vol_of_inner_sphere

    # 5% loss in vol
    Vol_of_cyl = vol_of_hollow_sphere * 0.95
     
    # radius of the cylinder

    r_c = d/2 # cm

    #cylinder length 
    #Vol_of_cyl = pi * r_c * r_c * h

    h = Vol_of_cyl / pi * r_c**2

    return h



r_in = float(input("enter inner radius : "))
r_out = float(input("enter outer radius : "))
a = print("hight of the cylinder", volume_of_cylinder(r_in, r_out, d = 3))











