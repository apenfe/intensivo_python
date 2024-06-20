from random import choice
from matplotlib import pyplot as plt

class RandomWalk:

    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        while len(self.x_values) < self.num_points:
            x_direction = choice([1])
            x_distance = choice([0,1,2,3,4,5,6,7,8])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9),dpi=128)


    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values,c=point_numbers,cmap=plt.cm.Blues, edgecolors='none', s=5)
    ax.set_aspect('equal')

    # enfatizar primer y ultimo punto
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    # eliminar los ejes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Continue? (y/n): ')
    if keep_running == 'n':
        break