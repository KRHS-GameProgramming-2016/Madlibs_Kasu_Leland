# -*- coding: utf-8 -*-

import os
if os.name == "nt":
    import msvcrt
from input import *

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
    print("""

.


XXXXXXXXXXX,            /XXXXXXXXYXXXXXXXXXXXXXXX/
XXXXXXXXXXXX.          *XXXXXXXXXXXXXXXXXXXXXXXXI
XXXXXXXXXXXXXXXX       /XXXXXXXXXXXXF**YXXXXXF-
XXXXXXXXXXXXXXXXXXX    *XXXXXXXXXXXT         *XXL
XXXXXXXXXXXXXXXXXXX)  /XXXXXXXXXXXX     MMMM   VXL
XXXXXXXXXXXXXXXXXXX/ JXXXXXXXXXXXX     X    Y   YXL
XXXXXXXXXXXXXXXXXXXXXXXXXX*--*XXX                VXL
(XXXXXXXXXXXXXXXXXXXXXXXF        *                 VXL
(XXXXXXXXXXXXXXXXXXXXX  NM           $$$*         VXX
 (XXXXXXXXXXXXXXXXXXX   Y            $    $$        XXL
  TXXXXXXXXXXXX/AXXXY   7    $$      R      $       )XI
   -XXXXXXXXXX/ XXXXI       $ $$     $      $      YXX
     *XXXXX*    XXXX(      $     $     $   ,*$      IXX
                TXXXX      $      $     $.$$$$      /XX)
                XXXXX       $   *$$$      $$$*      XYTTX=-.
                 XXXX(       $$$$$$$   XXXX-,      /        X
                  XXXXL        *$$$* XX  .,. Y               X
                   XXXXL           XX   XXXXX        XXX      )
                    XXXXL,.      XX    XXXXXX         X X     I
                     *XY                XXXX         X       /
                     X                              X        X
                    X                              X         X
                   X                              X         X
                  Y      XX*.                   X         X
                  (     X    X*.              .*V        .X
                  I             TX=XXXXXXXX=*XXX      X X
                   XX              TL.   T   )XV     X X
                     XX               X.      X/     XX
                       XX               XX.  .X      X
                         TXXXXXX*,(        TT        X
                                  XX               X
                                    XXX           XX
                                       XXX    XXXX
                                          XXXX
""")
    if os.name == "nt":
        end = False
        while not end:
            for i in range(99):
                if i <= 9:
                    num="0"+str(i)
                else:
                    num=str(i)
                os.system("color " + num)
                if msvcrt.kbhit():
                    os.system("color 07")
                    end = True
                    break;



def meme2():
    print("""
       ,'``.._   ,'``.
      :,--._:)\\,:,._,.:       All Glory to
      :`--,''   :`...';\\      the HYPNO PEPE!
       `,'       `---'  `.
       /                 :
      /                   \\
    ,'                     :\\.___,-.
   `...,---'``````-..._    |:       \\
     (                 )   ;:    )   \\  _,-.
      `.              (   //          `'    \\
       :               `.//  )      )     , ;
     ,-|`.            _,'/       )    ) ,' ,'
    (  :`.`-..____..=:.-':     .     _,' ,'
     `,'\\ ``--....-)='    `._,  \\  ,') _ '``._
  _.-/ _ `.       (_)      /     )' ; / \\ \\`-.'
 `--(   `-:`.     `' ___..'  _,-'   |/   `.)
     `-. `.`.``-----``--,  .'
       |/`.\\`'        ,','); SSt
           `         (/  (/
""")
    if os.name == "nt":
        end = False
        while not end:
            for i in range(99):
                if i <= 9:
                    num="0"+str(i)
                else:
                    num=str(i)
                os.system("color " + num)
                if msvcrt.kbhit():
                    os.system("color 07")
                    end = True
                    break;
def meme3():
    print("""
      .--..--..--..--..--..--.
    .' \\  (`._   (_)     _   \\
  .'    |  '._)         (_)  |
  \\ _.')\      .----..---.   /
  |(_.'  |    /    .-\-.  \\  |
  \\     0|    |   ( O| O) | o|
   |  _  |  .--.____.'._.-.  |
   \\ (_) | o         -` .-`  |
    |    \\   |`-._ _ _ _ _\\ /
    \\    |   |  `. |_||_|   |
    | o  |    \\_      \\     |     -.   .-.
    |.-.  \\     `--..-'   O |     `.`-' .'
  _.'  .' |     `-.-'      /-.__   ' .-'
.' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
`-._  `.  |________/\\_____|    `-.'
   .'   ).| '=' '='\\/ '=' |
   `._.`  '---------------'
           //___\\   //___\\
             ||_.-.   ||_.-.
            (_.--__) (_.--__)
""")
    if os.name == "nt":
        end = False
        while not end:
            for i in range(99):
                if i <= 9:
                    num="0"+str(i)
                else:
                    num=str(i)
                os.system("color " + num)
                if msvcrt.kbhit():
                    os.system("color 07")
                    end = True
                    break;

meme3()
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
