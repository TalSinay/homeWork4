from functools import reduce


class Entry:
	def __init__(self,key,leaf=False):
		self.key = key
		self.leaf = leaf
		self.size = 0
		self.Right = []
		self.Left = []



class Tree:
	def __init__(self, key):
		self.head = Entry(key, True)


	def insert(self,key):
		if self.head.key < key:
			if len(self.head.Right)>1:
				if key < self.head.Right[0].head.key:
					self.head.Right[0].insert(key)
					self.head.Right[0].leaf = False

				elif key < self.head.Right[1].head.key:
					self.head.Right[1].insert(key)
					self.head.Right[1].leaf = False
				else:
					self.head.Right[1].insert(key)
					self.head.Right[1].leaf = False

			elif len(self.head.Right) is 0:
				self.head.Right.append(Tree(key))
			elif len(self.head.Right)== 1:

				if key < self.head.Right[0].head.key:
					self.head.Right.append(self.head.Right[0])
					self.head.Right[0] = Tree(key)
				else:
					self.head.Right.append(Tree(key))
			else:
				self.head.Right.append(Tree(key))
		elif key < self.head.key:
			if len(self.head.Left)>1:
				if key < self.head.Left[0].head.key:
					self.head.Left[0].insert(key)
					self.head.Left[0].leaf = False
				elif key < self.head.Left[1].head.key:
					self.head.Left[1].insert(key)
					self.head.Left[1].leaf = False
				else:
					self.head.Left[1].insert(key)
					self.head.Left[1].leaf = False

			elif len(self.head.Left) is 0:
				self.head.Left.append(Tree(key))

			elif len(self.head.Left) is 1:
				if key < self.head.Left[0].head.key:
					self.head.Left.append(self.head.Left[0])
					self.head.Left[0] = Tree(key)
				else:
					self.head.Left.append(Tree(key))


			else:
				self.head.Left.append(Tree(key))

	def search(self,key):
		tree=self.head.Left+self.head.Right
		if key in tree or key == self.head.key:
			return True
		else:
			return any(map(lambda z:z.search(key),tree))
	def check(self, key):
		"""
		:param key:check the value of the key with the head
		:return: true or false
		"""
		return (self.head.leaf == True) and (not key < self.head.key and not self.head.key < key)

	def delete(self, key):
		if key < self.head.key:
			if len(self.head.Left) > 1:
				if key == self.head.Left[0].head.key:
					if self.head.Left[0].head.leaf:
						x = self.head.Left[0].head
						self.head.Left.remove(self.head.Left[0])
					return x
				elif key < self.head.Left[0].head.key:
					self.head.Left[0]._delete_(key)
				elif key == self.head.Left[1].head.key:
					if self.head.Left[1].head.leaf:
						x = self.head.Left[1].head
						self.head.Left.remove(self.head.Left[1])
					return x
				elif key < self.head.Left[1].head.key:
					self.head.Left[1]._delete_(key)
				else:
					self.head.Left[1]._delete_(key)
			elif len(self.head.Left) == 0:
				return 0
			elif key == self.head.Left[0].head.key:
				if self.head.Left[0].head.leaf:
					x = self.head.Left[0].head
					self.head.Left.remove(self.head.Left[0])
				return x

		elif self.head.key < key:
			if len(self.head.Right) > 1:
				if key == self.head.Right[0].head.key:
					if self.head.Right[0].head.leaf:
						x = self.head.Right[0].head
						self.head.Right.remove(self.head.Right[0])
					return x
				elif key < self.head.Right[0].head.key:
					self.head.Right[0]._delete_(key)
				elif key == self.head.Right[1].head.key:
					if self.head.Right[1].head.leaf:
						x = self.head.Right[1].head
						self.head.Right.remove(self.head.Right[1])
					return x
				elif key < self.head.Right[1].head.key:
					self.head.Right[1]._delete_(key)
				else:
					self.head.Right[1]._delete_(key)
			elif len(self.head.Right) == 0:
				return 0
			elif key == self.head.Right[0].head.key:
				if self.head.Right[0].head.leaf:
					x = self.head.Right[0].head
					self.head.Right.remove(self.head.Right[0])
				return x





	def __repr__(self):
		return f'Tree({self.head.key})'

	def __str__(self):
			return '<' + str(self.head.key) + '>' + str(list(map(str, self.head.Left + self.head.Right))).replace('\\', '')




def main():

	new_tree=None
	x='0'
	while x is not '5':
		x=input('please choose 1 optaion\n 1. to Create a tree\n 2.to Add a value to the tree\n 3.Delete a value from the tree\n 4.to print the tree\n 5.to Exit ')
		if x is '1':
				y=input('enter the root of the tree')
				new_tree=Tree(y)


		elif x is '2':
			if new_tree is None:
				raise UnboundLocalError('there is no tree!')
			else:
				k=input('enter the value you want to add')
				new_tree.insert(k)


		elif x is '3':
			if new_tree is None:
				raise UnboundLocalError('there is no tree!')
			else:
				k=input('enter the value you want to delete')
				if new_tree.delete(k):
					print('deleted succsesfull')
				else:
					print('cant deleted returned false')


		elif x == '4':
			if new_tree:
				print(new_tree)

		else:
			print('wrong input!,please try again')






main()
print('goodbye!')
