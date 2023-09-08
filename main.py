import matplotlib.pyplot as plt

TIME = 0
DURATION = 15 #sec
DRONE_MASS = 1890 #kg
DELTA_T = 0.1 #s
FUEL_CONSUMPTION = 0.6831 #liters
DIAMETER = 10 #m
AREA = 1 #m

THRUST_DURATION = 15 #s



class Drone():

    def __init__(self, drone_mass, delta_t, diameter, area, thrust_duration):
        self.thrust_duration = thrust_duration
        self.area =area
        self.diameter = diameter
        self.drone_mass = drone_mass
        self.delta_t = delta_t
        self.x_vel = 0
        self.y_vel = 0
        self.delta_x_vel = 0
        self.delta_y_vel = 0
        self.x_pos = 0
        self.y_pos = 0
        self.delta_delta_x_pos = 0
        self.delta_delta_y_pos = 0

    def thrust(self):
        thrust = 1000 #N
                
        acceleration = thrust / self.drone_mass

        self.delta_x_vel += acceleration * self.delta_t

    def drag(self):
        density_of_air = 1.293 #kg m−3
        viscosity_of_air = 1.48*10**(-5) #m2/s
        drag_cooficient =  0.08

        #Reynolds number
        #r_numebr = (density_of_air * self.x_vel * self.diameter)/viscosity_of_air

        #laminal:
        # if(r_numebr < 3750):
        #     pass

        # #turbulent:
        # else:
        #     pass

        drag = 0.5*density_of_air*-self.x_vel**2*self.area*drag_cooficient

        acceleration = drag / self.drone_mass

        self.delta_x_vel += acceleration * self.delta_t


    def start_x(self):
        self.delta_x_vel = 0
        self.delta_y_vel = 0
        
        if self.thrust_duration > 0:
            self.thrust()
            self.thrust_duration -= self.delta_t
        else:
            print('DONE')

        self.drag()
        self.x_vel += self.delta_x_vel

        

velocities = []
times = []

drone = Drone(DRONE_MASS, DELTA_T, DIAMETER, AREA, THRUST_DURATION)

for t in range(0, int(30/DELTA_T)):
    drone.start_x()
    velocities.append(drone.x_vel)
    TIME += DELTA_T
    times.append(TIME)
    print(drone.x_vel)

plt.plot(times, velocities)
plt.xlabel('x - time')
plt.ylabel('y - velocity')
plt.show()

# x-axis



