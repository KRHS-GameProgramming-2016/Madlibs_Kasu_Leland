from input import *

#Written by Mr. Spooner
def story():
    location1 = getWord("Enter a location: ")
    object1 = getWord("Enter a Object: ")
    monster1 = getWord("Enter a Monster: ")
    location2 = getWord("Enter a Location: ")
    action1 = getWord("Enter a Action: ")
    adjective =  getWord("Enter a Adjective: ")
    text = ""
    text += "One day Kent Heckel, the famous YouTuber was going for a walk in the " + location1
    text += ". While he was there he saw Kasu sucking a  " + object1
    text += "vigurously."    
    text += "Before he could blink, Kasu add been dragged away by a little " + monster1 
    text += """. He started to yell, "Help me! He is taking me to his """ + location2
    text += """. He is going to """ + action1
    text += """.""" 
    text += "Out of nowhere, Elijah the Magical " +adjective1 
    return text
