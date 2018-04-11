import matplotlib.pyplot as plt
import sys
driver_fr = [[200,96.],[250,94.],[300,95.],[400,94.],[500,93.],[600,92.],[700,93.],
             [800,95.],[1000,92.5],[1500,90.],[1750,93.],[2000,90.],[2500,94.],
             [3000,90.],[4000,90.],[5000,72.5],[6000,60.]]

driver_fr_x = [x[0] for x in driver_fr]
driver_fr_y = [y[1] for y in driver_fr]

f = open("12h.txt")
iterr = 0
for freq in f:
    character = freq[0]
    i = 0
    word = ""
    while character != " " and character !="\t":
        word = word + character
        i = i+1
        #print(i)
        character = freq[i]
        print(word)
##    try:
##        freq_int = int(float(word))
##    except:
##        freq_int = 0
##        print("Oops!",sys.exc_info()[0],"occured.")
##    print(freq_int)
##    
##    if abs(freq_int-driver_fr[iterr][0])<20:
##        print(freq_int,freq)
##        iterr += 1
    if word[0] == str(driver_fr[iterr][0])[0]:
        print(freq)
        iterr += 1
            


               
##plt.plot(driver_fr_x,driver_fr_y)
##plt.xscale('log')
##
##plt.show()
