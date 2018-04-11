import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

grid_size = 20
space_grid = np.mgrid[-grid_size:grid_size,-grid_size:grid_size]
D = 1

def F(a):
    f = a[0]**2-a[1]
    return(f)
lamd = F(space_grid)

dx = D/np.sqrt(1+lamd**2)
dy =lamd*D/np.sqrt(1+lamd**2)

print(dx)
print(dy)
#plt.imshow(mag)

#plt.show()

#fig, ax = plt.subplots()
plt.quiver(dx,dy)


plt.show()
