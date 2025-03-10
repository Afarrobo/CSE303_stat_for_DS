
nums = [i for i in range(1, 1001)]

divisors = {
    num: max(
       
        (digit for digit in range(2, 10) if num % digit == 0)
         
    )
    for num in nums
  
    if any(num % digit == 0 for digit in range(2, 10))
}


highest_divisor = max(divisors.values())


print(highest_divisor)
