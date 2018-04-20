from frdtools import frdparse

fr = open("fr-ph_nofilter.txt")

a = frdparse(fr)

##print(a[0])

def valuetoindex(a_list,a_value):
    smallest_diff = abs(a_list[0]-a_value)

    for i in range(len(a_list)):
        diff = abs(a_value-a_list[i])
        if diff<smallest_diff:
            smallest_diff = diff
            index = i
    return index
    
index = valuetoindex(a[0],200)

print(index)
