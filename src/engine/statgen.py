import random

def generate_list():
	a=[]
	for i in range(0, 6):
		t=[]
		for i in range(0, 4):
			t.append(random.randint(1, 6))
		a.append(sum(t)-min(t))
	return a


def stats(order):
	a = generate_list() 
	a.sort(reverse = True)
	t = [0,0,0,0,0,0]
	for i in range(0, 6):
		t[order[i]]=a[i]
	return t

def mod(a):
	return int((a-10)/2)