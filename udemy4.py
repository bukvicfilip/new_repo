def mode(list_of_nums):
	#prints the number that occurs most times
	dict_of_nums={}
	for num in list_of_nums:
		dict_of_nums[num]=list_of_nums.count(num)
	m=max(dict_of_nums.values())
	list_of_values=([value for value in dict_of_nums.values()]).index(m)
	print(list(dict_of_nums.keys())[list_of_values])


mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4, 8]) # 4