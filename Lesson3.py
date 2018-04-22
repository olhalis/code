a = 1
b = 2
a,b = 1,2

def sum(x, y):
	return (x + y, x - y)

a, b = sum(2,3)

print(a)
print(b)


d = {'name':'Andrew', 'age':30, 'country':'USA', 'status':'married'}

print(d['name'])	
d['pet'] = 'dog'

print(d)

print('age' in d)

if 'ages' in d:
	print(d['ages']) 

print (d.keys())

for k in d.keys():
	print(k, d[k])
	