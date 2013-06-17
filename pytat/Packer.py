import sys

class Packer:
	def pack(self, list):
		width = 2
		height = 2
		accross = False
		while self.pack_bin(list, width, height) == False:
			if accross:
				width *= 2
				accross = False
			else:
				height *= 2
				accross = True
			self.root = PackerNode(0, 0, width, height)

	def pack_bin(self, list, width, height):
		self.root = PackerNode(0, 0, width, height)
		list = sorted(list, key=(lambda item: item.width * item.height), reverse = True)
		for item in list:
			node = self.find_node(self.root, item.width, item.height)
			if node != None:
				node.item = item
				self.split_node(node, item.width, item.height)
			else:
				return False
		return True

	def list(self):
		list = []
		self.build_list(list, self.root)
		return list

	def build_list(self, list, node):
		if node != None:
			if node.used:
				list.append(node)
				self.build_list(list, node.down)
				self.build_list(list, node.right)

	def find_node(self, root, width, height):
		if root.used:
			right = self.find_node(root.right, width, height)
			if right != None:
				return right
			down = self.find_node(root.down, width, height)
			if down != None:
				return down
		elif width <= root.width and height <= root.height:
			return root
		else:
			return None

	def split_node(self, node, width, height):
		node.used = True
		node.down  = PackerNode(node.x, node.y + height, node.width, node.height - height)
		node.right = PackerNode(node.x + width, node.y, node.width - width, height)
		return node

	def get_width(self):
		return self.root.width

	width = property(get_width)

	def get_height(self):
		return self.root.height

	height = property(get_height)

class PackerNode:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.used = False
		self.width = width
		self.height = height

class PackerData:
	def __init__(self, width, height):
		self.width = width
		self.height = height

if __name__ == "__main__":
	packer = Packer()
	blocks = [PackerData(10, 10), PackerData(9, 9)]
	packer.pack(blocks)
	list = packer.list()
	print("size {0} {1}".format(len(list), list[0].item.width))
	print('Press any key to continue...')
	sys.stdin.read(1)