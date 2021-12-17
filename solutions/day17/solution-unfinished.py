from helper import *
from tabulate import tabulate

# # === TEST DATA ===
# x_min = 20
# x_max = 30
# x_range = range(x_min, x_max+1)
# y_min = -10
# y_max = -5
# y_range = range(y_min, y_max+1)
# max_steps = 1000

# # === REAL DATA ===
x_min = 192
x_max = 251
x_range = range(x_min, x_max+1)
y_min = -89
y_max = -59
y_range = range(y_min, y_max+1)

max_steps = 1000

# ====================
class Probe:
    def __init__(self, x_pos, y_pos, x_vel, y_vel):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.max_y = 0

    def step(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        if self.y_pos > self.max_y:
            self.max_y = self.y_pos
        if self.x_vel > 0:
            self.x_vel -= 1
        elif self.x_vel < 0:
            self.x_vel += 1
        self.y_vel -= 1
        

def check_trajectory(x_vel, y_vel):
    probe = Probe(0,0,x_vel,y_vel)
    for _ in range(max_steps):
        probe.step()
        # if probe.y_pos > probe.max_y:
        #     probe.max_y = probe.y_pos
        if probe.x_pos in x_range and probe.y_pos in y_range:
            return True
        elif probe.x_pos > x_max:
            return "OVERSHOT"
        elif probe.y_pos < y_min:
            return "UNDERSHOT"
        #     (probe.x_vel > 0 and probe.x_pos > x_max) or \
        #    (probe.y_vel < 0 and probe.y_pos < y_min) or \
        #    (probe.x_vel < 0 and probe.x_pos < x_min):
        #     return None
    else:
        return None


# max_y = 0
# xx = (0,0)

# # === Part One ===
# for Y_VEL in range(0,200):
#     for x_vel in range(-1000,1000):
#         result = check_trajectory(x_vel, Y_VEL)
#         if result and result > max_y:
#             max_y = result
#             xx = (x_vel, Y_VEL)
# print(max_y)


# === Part Two ===
# for Y_VEL in range(y_min,1000):
#     for x_vel in range(-1000,1000):
#         result = check_trajectory(x_vel, Y_VEL)
#         if result:
#             all_velocities.append((x_vel, Y_VEL))

# Pos x, pos y
all_velocities = []
for Y_VEL in range(-90,2000):
    for x_vel in range(0,252):
        result = check_trajectory(x_vel, Y_VEL)
        if result == True:
            all_velocities.append((x_vel, Y_VEL))

print(len(all_velocities))

# # Pos x, neg y
# all_velocities = []
# for x_vel in range(0,252):
#     for Y_VEL in range(0,-90,-1):
#         result = check_trajectory(x_vel, Y_VEL)
#         if result == True:
#             all_velocities.append((x_vel, Y_VEL))

print(len(all_velocities))
# for v in all_velocities:
#     print (v)

# Neg X -> x can never become greater than 0