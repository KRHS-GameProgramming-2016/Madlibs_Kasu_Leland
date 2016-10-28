from input import *

#Written by Leland
def story():
    location1 = getWord("Enter a location: ")
    adjective1 = getWord("Enter an adjective: ")
    name1 = getWord("Enter a name: ")
    name2 = getWord("Enter another name: ")
    number1 = getWord("Enter a number: ")
    object1 = getWord("Enter an object: ")
    
    text = ""
    text += "One day in the " + location1
    text += ", there was a " + adjective1
    text += " Elementary School."  
    text += " There was a Shark named " + name1
    text += " and an Octopus named " + name2
    text += ". One day, on the " + location1
    text += " playgroud, all of the big octopi made fun of " + name2
    text += " because he only had " + number1
    text += " arms. That day he was crying on the " + object1
    text += ". " + name1
    text += " decided to kill himself because he couldn't withstand the pain of existance."

    return text

