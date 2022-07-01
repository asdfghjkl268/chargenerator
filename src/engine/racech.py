import random
import os

def choose_race():
	races = os.listdir("resources/races")
	return races[random.randrange(0, len(races))]