up='w'
down='s'
left='a'
right='d'

list_size=4

# Creates a list containing 4 lists initialized to 0
Matrix = [[0 for x in range(list_size)] for x in range(list_size)]

while (1>0):
    #check_keyboard()
#def check_keyboard():
    inn=raw_input("were do you want to go \n")

    if (str(inn)==up):
        print('up')
    elif(str(inn)==down):
        print('down')
    elif(str(inn)==left):
        print('left')
    elif(str(inn)==right):
        print('right')
    else:
        print(str('controls are w,a,s, or d (no caps)'))
	
	
    print('')
    print('------')
    print(str(Matrix[0][0]))

	
