import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

grid_size = 1000
dimentions = [1000,1000] #in mm
space_grid = np.mgrid[0:dimentions[0]:grid_size*1j,0:dimentions[1]:grid_size*1j]

##source_position_1 = np.array([5,100,1])
##source_position_2 = np.array([5,150,1])
##source_position_3 = np.array([5,200,1])
##source_position_4 = np.array([5,250,1])
##source_position_5 = np.array([5,300,1])
##source_position_6 = np.array([5,350,1])
##source_position_7 = np.array([5,400,1])
##source_position_8 = np.array([5,450,1])
##source_position_9 = np.array([5,500,1])
##source_position_10 = np.array([5,550,1])
##source_position_11 = np.array([5,600,1])
##source_position_12 = np.array([5,650,1])
##source_position_13 = np.array([5,700,1])
##source_position_14 = np.array([5,830,1])
##source_pos_list = [source_position_1,source_position_2,source_position_3,source_position_4,source_position_5,source_position_6,
##                   source_position_7,source_position_8,source_position_9,source_position_10,source_position_11,source_position_12,
##                   source_position_13]

source_pos_list = [np.array([5,150+10*i,1]) for i in range(70)]
freq  = 1500

wavelength = 340000/freq
complex_array = np.zeros((grid_size,grid_size),dtype=np.complex_)
for i in source_pos_list:
    
    rx = (space_grid[1] - i[1])
    print(rx)

    ry = (space_grid[0] - i[0])
    print(ry)

    r = np.sqrt(np.square(rx)+np.square(ry))

    theta = 2*np.pi*r/wavelength

    complex_mag_per_source = i[2]*np.exp(-0.003*r)*(np.sin(theta) + 1j*np.cos(theta))

    #complex_array = complex_array + (1/(r+0.1))*(np.sin(theta) + 1j*np.cos(theta))
    complex_array = complex_array + complex_mag_per_source


mag = np.sqrt(np.real(complex_array)**2+np.imag(complex_array)**2)

#maglog = np.log10(mag)

print(mag)

plt.imshow(np.log10(mag))

plt.show()
