def frdparse(file):
    file.readline()
    freq = []
    spl = []
    phase = []

    item_list = [freq,spl,phase]
    value = ""
     
    for line in file:
        j = 0 
        for character in line:
             if character == "\t":
                  item_list[j].append(float(value))
                  value = ""
                  j = j+1
                  #print(j)
                  continue
             if character == "\n":
                  item_list[j].append(float(value))
                  value = ""

                  continue
             
             value = value + character

    return item_list

