#去除有序数组的重复元素
class popDuplicateElement(object):
	def __init__(self):
		pass

	def popDuplicateElement(self, array:list):
		if not array: return None
		n = len(array)
		if n == 1: return array
		slow, fast = 0, 1
		while  fast < n:
			if array[slow] != array[fast]:
				slow += 1
				array[slow] = array[fast]
			fast += 1
		return slow + 1
