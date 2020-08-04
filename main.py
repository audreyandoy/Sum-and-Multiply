#1) Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers.

# 2) For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.


def sum(nums):
  result = 0 
  for i in nums:
    result += i
  return result

def multiply(nums):
  result = 1 
  for i in nums:
    result *= i
  return result


print(sum([1,2,3,4]))
print(multiply([1,2,3,4]))