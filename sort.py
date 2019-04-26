#!/usr/bin/env python
# -*- coding: GBK -*-
#
#  sort.py
#
#  Copyright 2018 ChenWeizheng <ChenWeizheng@bupt.edu.cn>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
from my_sort import *


print("Sort Program Beginning... ...")
array1 = [0]	#待排序数字列表；0作为占位数，占位index为0的位置
print("Please input the number list you want to sort (Stop when input 'C') : ")
while True :
	value = input()
	if value == "C" or value == "c":
		break
	else :
		array1.append(int(value))
length = len(array1) - 1	#数字数量，真实长度减1（0是占位数）
print("\n\n")

while True :
	array2 = array1[:]
	algorithm = input("Please select a sort algorithm (Other input will STOP this program!) : \n"
									+	"1.Straight Insertion Sort\n"
									+	"2.Binary Insertion Sort\n"
									+	"3.Shell’s Sort\n"
									+	"4.Bubble Sort\n"
									+	"5.Quick Sort\n"
									+	"6.Simple Selection Sort\n"
									+	"7.Heap Sort\n"
									+	"8.2-Merging Sort\n"
									+	"9.sorted()\n"
									+	"Choice : ")
	if algorithm == "1" :
		SInsertSort(array2, length)
	elif algorithm == "2" :
		BInsertSort(array2, length)
	elif algorithm == "3" :
		ShellSort(array2, length)
	elif algorithm == "4" :
		BubbleSort(array2, length)
	elif algorithm == "5" :
		QuickSort(array2, 1, length)
	elif algorithm == "6" :
		SSelectSrot(array2, length)
	elif algorithm == "7" :
		HeapSort(array2, length)
	elif algorithm == "8" :
		MergeSort(array1, array2, 1, length)
	elif algorithm == "9" :
		array2.sort()
	else :
		break
	print("Result : " + str(array2[1:]))
	print()
print("Sort Program end... ...")