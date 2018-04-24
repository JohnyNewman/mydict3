dict = {"A":'1', "B":'2', "C":'3', "D":'4'}

def speak(string):
	result=""
	for char in range(0, len(string)):
		character=string[char]
		if character == " ":
			result= result + " "
		elif character in dict:
			result=result + dict[character]
		else:
			result=result + character
	return result
string = str(input("Write something: "))
print(speak(string))