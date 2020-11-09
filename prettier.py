import os,threading,time,sys

desc = r'''
Prettier is an opinionated code formatter. 
It enforces a consistent style by parsing your code 
and re-printing it with its own rules that take the 
maximum line length into account, wrapping code when 
necessary.
'''
print(desc)
time.sleep(0.777)

def path():
	if sys.platform == 'win32':
		inp = input("Enter directory of py file(s): ")
		if inp[-1] == '/' or inp[-1] == '\\':
			src = inp
		else:
			if '/' in inp:
				src = inp + '/'
			else:
				src = inp + '\\'
	elif sys.platform == 'darwin' or sys.platform=='linux':
		inp = input("Enter directory of py file(s): ")
		if inp[-1] == '/':
			src = inp
		else:
			src = inp + '/'
	return src

if sys.platform == 'win32':
	clear = 'cls'
else:
	clear = 'clear'

while True:
	src = path()
	try:
		check = os.listdir(src)
		break
	except (FileNotFoundError, OSError) as err:
		print("Please enter a valid directory path!")
		os.system(clear)
		time.sleep(0.3)

def count_py_files(src):
	ext_list = ['py','c','html','htm','css','txt','cpp','java','jsp','js','rb']
	count = 0
	for k in os.listdir(src):
		if k.split('.')[-1] in ext_list:
			count += 1 
	print(count)
	
	if count == 0:
		return 1
	else:
		return count

def prettier_py(src):
	ext_list = ['py','c','html','htm','css','txt','cpp','java','jsp','js','rb']
	for k in os.listdir(src):
		file = k.split('.')
		if file[-1] in ext_list:
			with open(src+k,mode='w') as edit:
				edit.write('get help!')
				edit.close()

def progressbar():
	count = count_py_files(src)
	min_percent = int(100/count)
	k = min_percent
	percentage = [k]
	while k < 100:
		k += min_percent
		percentage.append(int(k))

	os.system(clear)
	print('Making your code beautiful :)')
	for k in percentage:
		if k == percentage[-1]:
			print('\r' + str(100)+"%")
		else:
			print('\r' + str(k)+"%",end='')
			time.sleep(3/count)

t1 = threading.Thread(target=prettier_py(src))
t2 = threading.Thread(target=progressbar)

t1.run()
t2.run()
