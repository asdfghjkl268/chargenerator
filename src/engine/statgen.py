import random

def generate_list():
	a=[]
	for i in range(0, 6):
		t=[]
		for i in range(0, 4):
			t.append(random.randint(1, 6))
		a.append(sum(t)-min(t))
	return a
