up='w'
down='s'
left='a'
right='d'



while (1>0):
    #check_keyboard()
#def check_keyboard():
    inn=raw_input("hvor vil du \n")

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

