l = [3, 6, 53, 213, 8, 45, 28, 53, 3, 17]

print(sum(l))

s = 0
for i in l:
	s += i
print(s)

s = 0
for i in range(len(l)):
	if i%2 == 0:
		s = s+l[i]
print(s)

n = 0
for k in l:
	if k == 53:
		n += 1
print(n)

def mysum(a):
	s = 0
	for i in a:
		s += i
	return s	

print(mysum(l))

def count(a, number):
	n = 0
	for i in a:
		if i == number:
			n += 1
	return n

print(count(l, 53))
print(count(l, 3))
print(count(l, 128))




