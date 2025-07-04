# # Example 1: Using range() to loop through numbers
# print("Example 1: Looping through range")
# for i in range(5):  # range(5) generates numbers from 0 to 4
#     print(i)

# print("\n")  # Adds a blank line for separation

# # Example 2: Loop through a list
# print("Example 2: Looping through a list")
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# print("\n")

# # Example 3: Loop through a string
# print("Example 3: Looping through a string")
# for char in "hello":  # Iterates through each character in the string
#     print(char)

# print("\n")

# # Example 4: Using else with for loop
# print("Example 4: Using else with for loop")
# for i in range(3):
#     print(i)
# else:
#     print("Loop finished!")  # This runs when the loop completes normally

# print("\n")

# # Example 5: Using break to exit loop early
# print("Example 5: Using break inside for loop")
# for i in range(5):
#     if i == 3:
#         break  # Exits the loop when i == 3
#     print(i)

# print("\n")

# # Example 6: Using continue to skip an iteration
# print("Example 6: Using continue inside for loop")
# for i in range(5):
#     if i == 2:
#         continue  # Skips the rest of the loop when i == 2
#     print(i)

# print("\n")

# # Example 7: Loop through list of tuples
# print("Example 7: Looping through list of tuples")
# points = [(1, 2), (3, 4), (5, 6)]
# for x, y in points:  # Unpacks each tuple into x and y
#     print(f"x: {x}, y: {y}")

# print("\n")

# # Example 8: Loop using enumerate to get index and value
# print("Example 8: Using enumerate()")
# for index, fruit in enumerate(fruits):  # Gets both index and value from the list
#     print(f"{index}: {fruit}")

a = int(input("Enter the number of u want table = "))
for i in range(10):
    print(a*i)






