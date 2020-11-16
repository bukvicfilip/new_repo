def reverse_vowels(word):
	_list=[]
	word2=[]
	n=-1
	vowels="aeiouAEIOU"
	for w in word:
		if w in vowels:
			_list.append(w)
			_list1=_list[::-1]
	for letter in word:
		if letter not in _list:
			word2.append(letter)
		elif letter in _list:
			word2.append(_list[n])
			n-=1
	return("".join(word2))


print(reverse_vowels("Hello!")) # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"