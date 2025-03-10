string = "Practice Problems to Drill List Comprehension in Your Head."
words = string.split()
short_word =[ word for word in words if len(word) < 5]
print(short_word)