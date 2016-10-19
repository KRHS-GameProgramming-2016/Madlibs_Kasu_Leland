import os
def splash():
    screen = ""
    screen += "*********************************\n"
    screen += "*                               *\n"
    screen += "*           Welcome             *\n"
    screen += "*             to                *\n"
    screen += "*           Madlibs             *\n"
    screen += "*                               *\n"
    screen += "*                               *\n"
    screen += "*       by KASU & LELAND        *\n"
    screen += "*                               *\n"
    screen += "*       press enter to continue *\n"
    screen += "*********************************\n"
    return screen


def menu():
    screen = ""
    screen += "*********************************\n"
    screen += "* Madlibs Menu                  *\n"
    screen += "*                               *\n"
    screen += "*   1) Story One                *\n"
    screen += "*   2) Story Two                *\n"
    screen += "*   3) Story Tree               *\n"
    screen += "*                               *\n"
    screen += "*   Q) Quit                     *\n"
    screen += "*                               *\n"
    screen += "*                               *\n"
    screen += "*********************************\n"
    return screen

def memesplash():
    screen = ""
    screen += "*********************************\n"
    screen += "*                               *\n"
    screen += "*           Welcome             *\n"
    screen += "*            to the             *\n"
    screen += "*          MEME MENU            *\n"
    screen += "*                               *\n"
    screen += "*                               *\n"
    screen += "*       by KASU & LELAND is dum *\n"
    screen += "*                               *\n"
    screen += "*       press enter to continue *\n"
    screen += "*********************************\n"
    return screen

def memesplash():
    screen = ""
    screen += "*********************************\n"
    screen += "*                               *\n"
    screen += "*      Dont let your memes      *\n"
    screen += "*           BE MEMES            *\n"
    screen += "*                               *\n"
    screen += "*                               *\n"
    screen += "*                               *\n"
    screen += "*                               *\n"
    screen += "*                               *\n"
    screen += "*    press enter to continue    *\n"
    screen += "*********************************\n"
    return screen
    
def mememenu():
    screen = ""
    screen += "*********************************\n"
    screen += "*                               *\n"
    screen += "*         Select a meme         *\n"
    screen += "*                               *\n"
    screen += "*                               *\n"
    screen += "*        Meme 1 (Press 1)       *\n"
    screen += "*        Meme 2 (Press 2)       *\n"
    screen += "*        Meme 3 (Press 3)       *\n"
    screen += "*                               *\n"
    screen += "*                               *\n"
    screen += "*********************************\n"
    return screen
    
def meme1():
    if os.name == "nt":
        os.system("color 02")
    """

    """
    if os.name == "nt":
        os.system("color 07")
        
def meme2():
    if os.name == "nt":
        for i in range(99):
            if i <= 9:
                num=0+str(i)
            else:
                num=str(i)
            os.system("color" + num)
    print("""
    
    
    
    
    
    """)
            

def hacks():
    print mememenu()
    raw_input()
    end = False
    while not end:
        print mememenu()
        option = getMemeMenuOption()
        if option == "q":
            end = True
        elif option == "1":
            print meme1()
            raw_input()
        elif option == "2":
            print meme2()
            raw_input()
        elif option == "3":
            print meme3()
            raw_input()
