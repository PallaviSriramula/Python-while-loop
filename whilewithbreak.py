"""
Create a simple program that uses a while loop to iterate over a range of numbers from 1 to 10.
Implement a condition to print only the even numbers within this range using the continue statement.
Add another condition that stops the loop when it encounters the number 8, utilizing the break statement.
Ensure your program includes comments explaining the purpose of each segment, especially where break and continue are used.
Execute your program and document the output to verify it meets the expected behavior.
"""
# Start from 1
i = 1

# Loop from 1 to 10
while i <= 10:

    # Stop the loop when the number becomes 8
    if i == 8:
        break

    # Skip odd numbers
    if i % 2 != 0:
        i += 1
        continue

    # Print even numbers
    print(i)

    # Move to the next number
    i += 1    