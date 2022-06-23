def check_back():
	flag = True
	for i in range(1, 35):
		with open('resources/backstorytables/'+str(i)+'.txt') as f:
			arr = f.readlines()
		for j in arr:
			tarr=arr[j].split(".")
			if tarr[len(tarr)-1]=="" or tarr[len(tarr)-1]=="\n":
				flag= True
			else:
				try:
					t = int(tarr[len(tarr)-1])
				except:
					flag = False
	return flag