import matplotlib.pyplot as plt

def plot_data():
#open the txt file
    data_file = open('C:/Downloads/x_y_coordinates.txt', 'r')

    x_coords = []
    y_coords = []
    data_file.readline()

#read the data and append
    for line in data_file.readlines():
        x_coords.append(float(line.split(',')[0]))
        y_coords.append(float(line.split(',')[1]))

#plot the coordinates
    plt.scatter(x_coords, y_coords)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
plot_data()