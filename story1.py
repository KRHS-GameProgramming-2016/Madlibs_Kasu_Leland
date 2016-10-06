from input import *

#Written by Mr. Spooner
def story():
    location1 = getWord("Enter a location: ")
    temperature1 = getWord("Enter a Number: ")
    
    text = ""
    text += "One day Kent Heckel went to the " + location1
    text += ". It was like " + temperature1
    text += " out."    
    return text
