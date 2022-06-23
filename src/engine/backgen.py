import random


def background(tabnum = 1):
	with open('resources/backstorytables/'+str(tabnum)+'.txt') as f:
		arr = f.readlines()
	tmp = arr[random.randint(0, len(arr)-1)]
	tarr=tmp.split(".")
	if tarr[len(tarr)-1]=="" or tarr[len(tarr)-1]=="\n":
		return tmp
	else:
		return tmp[:-2]  + background(int(tarr[len(tarr)-1]))