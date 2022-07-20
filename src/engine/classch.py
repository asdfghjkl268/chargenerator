import random
import os

def choose_class():
	classes = os.listdir("engine/resources/classes")[1:]
	return classes[random.randrange(0, len(classes))]

def choose_sub(main):
	subclasses = os.listdir("engine/resources/classes/"+main)[1:]
	try:
		return subclasses[random.randrange(0, len(subclasses))]
	except:
		return ""


def genclass():
	cl = choose_class()
	sub = choose_sub(cl)
	return cl+'.'+sub[:-4]