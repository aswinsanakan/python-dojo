# Print all prime numbers between a range

lower = int(input("Enter a number (lower) : "))
upper = int(input("Enter a number (upper) : "))

for num in range(lower, upper + 1):
  if num > 1:
    for i in range(2,num):
      if (num % i) == 0:
        break
    else:
      print(num)
