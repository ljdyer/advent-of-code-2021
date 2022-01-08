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


# ====================
def check_trajectory(x_vel, y_vel):

    probe = Probe(0, 0, x_vel, y_vel)
    for _ in range(max_steps):
        probe.step()
        if probe.x_pos in x_range and probe.y_pos in y_range:
            return (True, probe.max_y)
        elif probe.x_pos > x_max:
            return ("OVERSHOT", 0)
        elif probe.y_pos < y_min:
            return ("UNDERSHOT", 0)
    else:
        return (None, 0)


# === Part One ===
max_y = 0
xx = (0, 0)
for Y_VEL in range(0, 200):
    for x_vel in range(-1000, 1000):
        result, ymax = check_trajectory(x_vel, Y_VEL)
        if result is True and ymax > max_y:
            max_y = ymax
            xx = (x_vel, Y_VEL)
print('Part One answer:', max_y)


# === Part Two ===
all_velocities = []
for Y_VEL in range(-90, 2000):
    for x_vel in range(0, 252):
        result, _ = check_trajectory(x_vel, Y_VEL)
        if result is True:
            all_velocities.append((x_vel, Y_VEL))
print('Part Two answer:', len(all_velocities))
