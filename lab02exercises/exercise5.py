string = "Practice Problems to Drill List Comprehension in Your Head."
words = string.split()
word_lengths ={ len(word) for word in words}
print("lengths of each word = " , word_lengths)
print("\n")
print("another way")
print("\n")
word_lengths ={word :  len(word) for word in words }
print("lengths of each word = " , word_lengths)
