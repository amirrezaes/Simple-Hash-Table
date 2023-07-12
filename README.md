# Simple-Hash-Table
Simple Hash Table Class with python 

A simple hash table class which uses mod 7 as hash operation (can be changed with m arg of HashTable class)
using Linear probing for resolving collisions

```python
t1 = HashTable()
for i in range(1000):
	t1[i] = hex(i) + "^" + str(id(i))  # something random :p

print(t1)
print(t1[2], t1[99])
print(15 in t1)
for i in t1:
	print(i)
del t1[0]
t1.clear()
 ```
