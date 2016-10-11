from input import *

#Written by Mr. Spooner
def story():
    location1 = getWord("Enter a location: ")
    temperature1 = getWord("Enter a subject: ")
    noun1 = getWord("Enter a noun: ")
    object1 = getWord("Enter an object: ")
    adjective1 = getWord("Enter and adjective: ")
    insult1 = getWord("Enter an insult: ")
    insult2 = getWord("Enter a verb: ")
    
    text = ""
    text += "One day Kent Heckel, the famous YouTuber was going for a walk in " + location1
    text += ". He got out his dank vlogging gear to make a vlog about " + temperature1
    text += ". Suddenly a " + noun1
    text += " jumped out and slit Kent Heckel's throat with a diamond tipped " + object1
    text += "! Since Kent was dead, his little sister Leland had to take over the most famous YouTube channel ever. But there was one small probem... Leland was " + adjective1
    text += """! But Leland was brave, "It doesn't matter that I'm """ +adjective1
    text += ". People will love me for who I am! "
    text += "But he was wrong... So very wrong. When he uploaded his first video everybody in the comments called him " + insult1
    text += " boy, and told him to go " +insult2
    text += " himself."
    return text
