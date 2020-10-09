from playsound import playsound

def logn() :
    print('Password: ')
    pasw = input()
    if(pasw == 'masteryo0'):
        print('access granted')
        playsound('output2.mp3')
    if(pasw != 'masteryo0'):
        print('Incorrect password')
logn()