nums =[i for i in range(1,1000)]
div_by_8 = [num for num in nums if num% 8== 0]
print( "prnt all number which is divided by 8 = " ,div_by_8)

print("___Find all numbers from 1–1000 that have a 6 in them.___")
print("\n")

contain_6 =[num for num in nums if '6' in str(num)]
print(contain_6)
print("\n")

print("____Count the number of spaces in a string.___")
print("\n")

string ="Practice Problems to Drill List Comprehension in Your Head."

space_count = sum([1 for char in string if char == ' '])

print(space_count)

print("\n")
print("Print Numbers Divisible by Single Digits (2-9)")

print("\n\n")
divisible_nums = [num for num in nums if any(num % digit == 0 for digit in range(2, 10))]
print(divisible_nums)





