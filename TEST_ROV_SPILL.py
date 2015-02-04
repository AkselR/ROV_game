<<<<<<< HEAD

=======
import sys

#Keyboard keys for input
>>>>>>> origin/master
up='w'
down='s'
left='a'
right='d'

<<<<<<< HEAD
list_size=5
out=0

Matrix = [[0 for x in range(list_size)] for x in range(list_size)]
=======
#Printed graphics
ROV='Z'
background='~'

#other variables
listSize=6
lastXPos=0
xPos=0
inn=0

#Creates a list containing listSize elements, lists initialized to 0
Grid = [[0 for x in range(listSize)] for x in range(listSize)]
#fill the Grid with background elements
for x in xrange(0, listSize):
        for y in xrange(0, listSize):
            Grid[x][y]=(str(background))
Grid[0][0]=str(ROV)
lastXPos=0
>>>>>>> origin/master


#check if player want to start or end program
while (1>0):
<<<<<<< HEAD
    inn=raw_input("were do you want to go \n")
=======
    inn=raw_input('Write "start" to start and "end" to end after start (small letters)')
    if (str(inn)==str('start')):
        break
    elif (str(inn)==str('end')):
        sys.exit('Game ended')
#------------------------------------------
>>>>>>> origin/master

while (1>0):
    print('')
    #fills "---..." over the grid
    for x in xrange(0,listSize+1):
        print('-'),
    print('')
    #Prints the grid to commandwindow
    for x in xrange(0, listSize):
        for y in xrange(0, listSize):
            print(str(Grid[x][y])),
        print('')
    #fills "---..." below the grid
    for x in xrange(0,listSize+1):
        print('-'),
    print('')
    #gets the input data
    inn=raw_input('Were do you want to go?: ')

    #check if player want to go up, down, wants to end or if the input is wrong
    if (str(inn)==up):
        print('up')
        xPos=int(xPos)-1
    elif(str(inn)==down):
        print('down')
        xPos=int(xPos)+1

    #elif(str(inn)==left):
    #    print('left')

    #elif(str(inn)==right):
    #    print('right')
    elif(str(inn)==str('end')):
        sys.exit('Game ended')
    else:
<<<<<<< HEAD
        print(str('controls are w,a,s, or d (no caps)'))
	
    print('')
    print('------')
    
    for x in xrange(1, list_size):
        Matrix[x][0]=str(x)
        for y in xrange(1, list_size):
            out=str(out)+ str(y)
        print(str(out))
        print('\n')
=======
        print'controls are w or s (small letters only)'
    #------------------------------------------

    #check if ROV is still in the grid, if not fill last position
    if (int(xPos)<0):
        xPos=0
    elif (int(xPos)>=int(listSize)):
        xPos=int(listSize)-1
    else:
        Grid[int(lastXPos)][0]=str(background)
    #------------------------------------------

    #Place the ROV in the new position
    Grid[int(xPos)][0]=ROV
    lastXPos=int(xPos)
    #------------------------------------------
>>>>>>> origin/master
