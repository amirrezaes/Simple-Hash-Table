from typing import Any


class HashTable:
	def __init__(self, m=7) -> None:
		self.data = [None]*100
		self.size = 0
		self.m = m

	def __setitem__(self, key: int, item: Any) -> None:
		pair = (key, item) # this will be saved in memmory
		hash_k = self.hash_of(key);

		if self.size-1 == len(self.data):
			self.expand()

		if self.data[hash_k] is not None:  # implemention of Linear probing to resolve collisions.
			if self.data[hash_k][0] == key: # replacing new item if key is the same.
				self.data[hash_k] = pair
				return
			else:
				for i in range(hash_k, len(self.data)):
					if self.data[i] is None:
						self.data[i] = pair
						break
				else:
					last_index = len(self.data) # first free spot after expansion.
					self.expand()  # if no free spot exists we expand the array.
					self.data[last_index] = pair
		else:
			self.data[hash_k] = pair
		self.size += 1

	def __getitem__(self, key) -> Any:
		hash_k = self.hash_of(key)
		if self.data[hash_k][0] == key:
			return self.data[hash_k][1]
		else:
			for i in range(hash_k+1, len(self.data)):  # Linear probing search.
				if self.data[i][0] == key:
					return self.data[i][1]
			raise KeyError(f"key: {key} does not exist !")

	def __contains__(self, key) -> bool:
		for i in self.data[self.hash_of(key):]:
			if i is not None and i[0] == key:
				return True
		return False
	
	def __delitem__(self, key) -> None:
		for i in range(self.hash_of(key), len(self.data)):
			if i is not None and self.data[i][0] == key:
				self.data[i] = None
				self.size -= 1
				break
				
	
	def __repr__(self) -> str:
		return f"< HashTable with length of {self.size} >"
	
	def __str__(self) -> str:
		return str([f"{i[0]}-> {i[1]}" for i in self.data if i is not None])
	
	def __iter__(self):
		return iter([i[0] for i in self.data if i is not None])
	
	def __len__(self):
		return self.size

	def hash_of(self, item:int or tuple) -> int:
		if type(item) == tuple:
			return item[0] % self.m
		else:
			return item % self.m

	def expand(self, s=100):
		self.data.extend([None]*s)
	
	def clear(self):
		self.data = 0
		self.size = 0



if __name__ == "__main__":
	t1 = HashTable()
	for i in range(1000):
		t1[i] = hex(i) + "^" + str(id(i))  # something random :p
	
	print(t1)
	print(t1[2], t1[99])
	print(15 in t1)

