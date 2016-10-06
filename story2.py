from input import *

#Written by Mr. Spooner
def story():
    location1 = getWord("Enter a location: ")
    temperature1 = getWord("Enter a subject: ")
    
    text = ""
    text += "One day Kent Heckel, the famous YouTuber was going for a walk in " + location1
    text += ". He got out his dank vlogging gear to make a vlog about " + temperature1
    text += " out."    
    return text
