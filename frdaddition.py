import matplotlib.pyplot as plt
from frdtools import frdparse,valuetoindex
import numpy as np



## Open frequency - phase responce files
fr1 = open("fr-ph_nofilter.txt")
fr2 = open("fr-ph_inductor2.txt")


##Parse files to lists
a = frdparse(fr1)
b = frdparse(fr2)

a_spl = np.array(a[1])
a_phase = np.radians(np.array(a[2]))

b_spl = np.array(b[1])
b_phase = np.radians(np.array(b[2]))

##Addition code
a_presure = 10**(a_spl/20)
b_presure = 10**(b_spl/20)

a_complex = a_presure*(np.cos(a_phase)+1j*np.sin(a_phase))
b_complex = b_presure*(np.cos(b_phase)+1j*np.sin(b_phase))

complex_sum = a_complex + b_complex

complex_mag = np.sqrt(np.square(np.real(complex_sum))+np.square(np.imag(complex_sum)))

complex_mag_spl = 20*np.log10(complex_mag)

##p_total = a_presure + b_presure

##p_total_spl = 20*np.log10(p_total)

##define plot range

low_freq = 50
high_freq = 10000

r_b = valuetoindex(a[0],low_freq)
r_t = valuetoindex(a[0],high_freq)



plt.figure(1)
plt.subplot(211)
plt.plot(a[0][r_b:r_t],a[1][r_b:r_t],'b-',b[0][r_b:r_t],b[1][r_b:r_t],'r-',a[0][r_b:r_t],complex_mag_spl[r_b:r_t],'y-')
plt.xscale('log')

plt.subplot(212)
plt.plot(a[0][r_b:r_t],a[2][r_b:r_t],'b-',b[0][r_b:r_t],b[2][r_b:r_t],'r-')
plt.xscale('log')
plt.show()
