def SInsertSort(array, length) :
	"""插入排序之直接插入排序，时间复杂度O(n^2)，稳定，适用于基本有序的小数据集，适用于链式结构"""
	for i in range(1, length + 1) :
		array[0]  =array[i]
		if array[i] < array[i-1] :
			j = i-1
			while j >= 1 :
				if array[j] > array[0] :
					array[j+1] = array[j]
				else :
					break
				j -= 1
			array[j+1] = array[0]


def BInsertSort(array, length) :
	"""插入排序之折半插入排序，时间复杂度O(n^2)，稳定，适用于无序的大数据集"""
	for i in range(1, length + 1) :
		array[0] = array[i]
		if array[i] < array[i-1] :
			lowIndex = 1
			highIndex = i-1
			while lowIndex <= highIndex :
				minIndex = int((lowIndex + highIndex) / 2)
				if array[0] < array[minIndex] :
					highIndex = minIndex - 1
				else :
					lowIndex = minIndex +1
			j = i - 1
			while j >= lowIndex :
				array[j+1] = array[j]
				j -= 1
			array[lowIndex] = array[0]


def ShellSort(array, length) :
	"""插入排序之希尔排序，时间复杂度O(n^1.3)，不稳定，适用于无序的大数据集"""
	dk = int(length / 2)	#初始增量设为长度的一半
	while dk >= 0 :
		for i in range(1 + dk, length +1) :
			array[0] = array[i]
			if array[i] < array[i-dk] :
				j = i - dk
				while j >= 1:
					if array[j] > array[0] :
						array[j+dk] = array[j]
					else :
						break
					j -= dk
				array[j+dk] = array[0]
		dk -= 1


def BubbleSort(array, length) :
	"""交换排序之冒泡排序，时间复杂度O(n^2)，稳定，适用于基本有序的小数据集，适用于链式结构"""
	for i in range(1, length) :
		j = length
		flag = False
		while j >= i :
			if array[j] < array[j-1] :
				flag = True
				array[0] = array[j]
				array[j] = array[j-1]
				array[j-1] = array[0]
			j -= 1
		if flag == False:
			break


#重中之重！！！
def QuickSort(array, lowIndex, highIndex) :
	"""交换排序之快速排序， 时间复杂度O(n*log2n)，不稳定，适用于无序的大数据集"""
	if lowIndex < highIndex :
		pivotIndex = Partition(array, lowIndex, highIndex)
		QuickSort(array, lowIndex, pivotIndex - 1)
		QuickSort(array, pivotIndex + 1, highIndex)
def Partition(array, lowIndex, highIndex) :
	"""快排分割子表"""
	array[0] = array[lowIndex]	#lowIndex位置的元素作为初始中枢轴
	while lowIndex < highIndex :
		while lowIndex < highIndex and array[highIndex] >= array[0] :
			highIndex -= 1
		array[lowIndex] = array[highIndex]
		while lowIndex < highIndex and array[lowIndex] <= array[0] :
			lowIndex += 1
		array[highIndex] = array[lowIndex]
	array[lowIndex] = array[0]
	return lowIndex


def SSelectSrot(array, length) :
	"""选择排序之简单选择排序， 时间复杂度O(n^2)，不稳定，适用于基本有序的小数据集，适用于链式结构"""
	for i in range(1, length) :
		minIndex = i
		for j in range(i, length + 1) :
			if array[j] < array[minIndex] :
				minIndex = j
		array[0] = array[i]
		array[i] = array[minIndex]
		array[minIndex] = array[0]


#重中之重！！！
def HeapSort(array, length) :
	"""选择排序之堆排序，时间复杂度O(n*log2n)，不稳定，适用于无序的大数据集"""
	i = int(length / 2)
	while i >= 1 :
		AdjustHeap(array, i, length)
		i -= 1
	i = length
	while i > 1 :
		array[0] = array[i]
		array[i] = array[1]
		array[1] = array[0]
		i -= 1
		AdjustHeap(array, 1, i)
def AdjustHeap(array, lowIndex, highIndex) :
	"""堆排调整堆"""
	leftChild = 2 * lowIndex
	rightChild = 2 * lowIndex + 1
	maxIndex = lowIndex
	if leftChild <= highIndex and array[leftChild] > array[maxIndex] :
		maxIndex = leftChild
	if rightChild <= highIndex and array[rightChild] > array[maxIndex] :
		maxIndex = rightChild
	if maxIndex != lowIndex :
		array[0] = array[lowIndex]
		array[lowIndex] = array[maxIndex]
		array[maxIndex] = array[0]
		AdjustHeap(array, maxIndex, highIndex)	#调整之后只有堆下半部分可能会受影响，上半部分不可能受影响


#重中之重！！！
def MergeSort(array1, array2, lowIndex, highIndex) :
	"""2-路归并排序，时间复杂度O(n*log2n)，稳定，适用于链式结构？"""
	if lowIndex == highIndex :
		array2[lowIndex] = array1[lowIndex]
	else :
		array3 = array2[:]
		midIndex = int((lowIndex + highIndex) / 2)
		MergeSort(array1, array3, lowIndex, midIndex)
		MergeSort(array1, array3, midIndex + 1, highIndex)
		Merge(array3, array2, lowIndex, midIndex, highIndex)
def Merge(array1, array2, lowIndex, midIndex, highIndex) :
	"""2-路归并排序合并子表"""
	#将arra1[lowIndex, midIndex]和array1[midIndex+1, highIndex]合并至array2[lowIndex, highIndex]
	i = lowIndex
	j = midIndex + 1
	k = lowIndex
	while i <= midIndex and j <= highIndex :
		if array1[i] <= array1[j] :
			array2[k] = array1[i]
			k += 1
			i += 1
		else :
			array2[k] = array1[j]
			k += 1
			j += 1
	while i <= midIndex :
		array2[k] = array1[i]
		k += 1
		i += 1
	while j <= highIndex :
		array2[k] = array1[j]
		k += 1
		j += 1