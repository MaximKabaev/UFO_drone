import math
import sys

class Frisbee:
    x = 0.0
    y = 0.0
    vx = 0.0
    vy = 0.0
    g = -9.81
    m = 0.175
    RHO = 1.23
    AREA = 0.0568
    CL0 = 0.1
    CLA = 1.4
    CD0 = 0.08
    CDA = 2.72
    ALPHA0 = -4

    @staticmethod
    def simulate(y0, vx0, vy0, alpha, de):
        dt = 0.01
        t = 0.0
        x = 0.0
        y = y0
        vx = vx0
        vy = vy0
        while y >= 0:
            v = math.sqrt(vx * vx + vy * vy)
            alpha_rad = math.radians(alpha)
            de_rad = math.radians(de)
            cl = Frisbee.CL0 + Frisbee.CLA * alpha_rad
            cd = Frisbee.CD0 + Frisbee.CDA * cl * cl
            l = 0.5 * Frisbee.RHO * v * v * Frisbee.AREA * cl
            d = 0.5 * Frisbee.RHO * v * v * Frisbee.AREA * cd
            ax = (l * math.sin(alpha_rad) - d * math.cos(alpha_rad)) / Frisbee.m
            ay = (l * math.cos(alpha_rad) + d * math.sin(alpha_rad)) / Frisbee.m - Frisbee.g
            vx += ax * dt
            vy += ay * dt
            x += vx * dt
            y += vy * dt
            t += dt
        return x, t

y0 = float(sys.argv[1])
vx0 = float(sys.argv[2])
vy0 = float(sys.argv[3])
alpha = float(sys.argv[4])
de = float(sys.argv[5])

x, t = Frisbee.simulate(y0, vx0, vy0, alpha, de)
print("x =", x)
print("t =", t)