import clr
import sys
import json
import os
import ctypes
import codecs

ScriptName = "Insulter"
Website = "https://github.com/Szar"
Description = "Random insult generator"
Creator = "Soflne"
Version = "1.0.0"

configFile = "config.json"
settings = {}

sentences = ["no one asked for your opinion, you", "i fail to understand how you've become such a", "get out of my way, you sorry excuse for a", "i cannot believe that you are such a", "you are such a", "i'm getting really tired of this shit, you", "i can't believe you are even talking to me, you"]
adjectives = ["abnormal", "actually", "damned", "serious", "worst", "ultimate", "worse", "original", "gross", "deep", "good", "adorable", "cute", "aggressive", "amazing", "ambitious", "annoying", "apathetic", "anxious", "arrogant", "attractive", "average", "awful", "bad", "evil", "big", "bizarre", "boring", "brainless", "busted", "charming", "cheap", "childish", "classy", "colossal", "cursed", "cowardly", "creepy", "dead", "delicate", "delicious", "demonic", "dirty", "disgusting", "dramatic", "dusty", "elderly", "elite", "empty", "fancy", "fine", "friendly", "fresh", "fragile", "furry", "fuzzy", "gaping", "gigantic", "godly", "greedy", "grubby", "handsome", "hellish", "helpless", "hideous", "homeless", "hot", "hungry", "thirsty", "juicy", "lame", "large", "little", "loud", "lumpy", "magical", "meaty", "moldy", "nasty", "nervous", "nice", "ordinary", "pointless", "poor", "premium", "questionable", "rabid", "repulsive", "ripe", "rotten", "rude", "salty", "savory", "scrawny", "sloppy", "sneaky", "spooky", "stupid", "super", "supreme", "tasty", "teeny-tiny", "tender", "thick", "ugly", "wacky", "wild", "zesty"]
curseWords = ["fuckass", "fuck", "ass", "as-heck", "thief", "bitch", "frog", "shitty", "dumbo", "fucker"]
nouns = ["goon", "bean", "snack", "boy", "anime"]
vowels = ["a", "e", "i", "o", "u"]

def insult():
	s = random.choice(sentences)
	a = random.choice(adjectives)
	n = random.choice(nouns)
	c = random.choice(curseWords)
	if s[-1]=="a" and s[-2]==" " and a[0] in vowels:
		s = s+"n"
	return s+" "+a+" "+c+" "+n

def ScriptToggled(state):
	return

def Init():
	global settings

	path = os.path.dirname(__file__)
	try:
		with codecs.open(os.path.join(path, configFile), encoding='utf-8-sig', mode='r') as file:
			settings = json.load(file, encoding='utf-8-sig')
	except:
		settings = {
			"liveOnly": False,
			"command": "!insult",
			"permission": "Everyone",
		}

def Execute(data):
	if data.IsChatMessage() and data.GetParam(0).lower() == settings["command"] and Parent.HasPermission(data.User, settings["permission"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
		userId = data.User			
		username = data.UserName
		Parent.SendStreamMessage(username+' '+insult())
	return

def ReloadSettings(jsonData):
	Init()
	return

def OpenReadMe():
	location = os.path.join(os.path.dirname(__file__), "README.txt")
	os.startfile(location)
	return

def Tick():
	return
