import matplotlib.pyplot as plt




fr = open("fr-ph_nofilter.txt")
fr.readline()
freq = []
spl = []
phase = []

il = [freq,spl,phase]
value = ""
 
for line in fr:
    j = 0 
    for character in line:
         if character == "\t":
              il[j].append(float(value))
              value = ""
              j = j+1
              print(j)
              continue
         if character == "\n":
              il[j].append(float(value))
              value = ""

              continue
         
         value = value + character


#print(freq)
#print(spl)
#print(phase)

plt.plot(freq,phase)
plt.xscale('log')

plt.show()
         
      
              
