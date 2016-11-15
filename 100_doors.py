items = ['c'] * 100
open_door=[]
s = 0

while s < 100:
    s += 1

    for i in range(s-1,len(items),s):
        if items[i] == 'c':
            items[i] = 'o'

        else:
            items[i] = 'c'

for i in range(len(items)):
    if items[i] == 'o':
        open_door.append(i+1)



print('folowing numbers: '+str(open_door))
