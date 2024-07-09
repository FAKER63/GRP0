#Consider the following Python program to count the total number of digits in a number using a while loop:

python
# Input number
number = 238765

# Initialize count variable to store the count of digits
count = 0

# Loop to count the digits
while number > 0:
    number //= 10
    count += 1

# Output the total number of digits
print(f'Total number of digits: {count}')

#Total number of digits: 6
