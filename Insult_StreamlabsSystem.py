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

sentences = ["no one asked for your opinion, you", "i fail to understand how you've become such a", "get out of my way, you sorry excuse for a", "i cannot believe that you are such a", "you're a", "i'm getting really tired of this shit, you", "i can't believe you are even talking to me, you"]
adjectives = ["actual", "serious", "ultimate", "good", "adorable", "cute", "anxious", "average", "evil", "big", "brainless", "busted", "cheap", "cursed", "smelly", "creepy", "dead", "delicate", "delicious", "dirty", "dusty", "old", "fine", "fresh", "fragile", "furry", "gaping", "gigantic", "hideous", "hot", "hungry", "thirsty", "juicy", "lame", "little", "magical", "meaty", "moldy", "nasty", "nervous", "premium", "repulsive", "ripe", "rotten", "rude", "salty", "savory", "scrawny", "sloppy", "spooky", "stupid", "super", "supreme", "tasty", "teeny-tiny", "thick", "ugly", "wacky", "wild"]
curseWords = ["fuckass", "ass", "as-heck", "bitch", "shit", "shitty", "dumbo", "anime-looking", "frog-looking", "small-eared", "small-faced", "looking", "fucking"]
nouns = ["goon", "bean", "snack", "boy", "anime", "fucker", "weeb", "coward", "headass", "cuck", "donkey"]
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
