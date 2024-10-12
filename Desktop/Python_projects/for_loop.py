#create a loop of fruit
fruits =["orange", "mango", "apple"]

for fruit in fruits:

    print(fruit)

#Create a list of fruits. Check if "apple" is in the list, and print "Yes" if it is, otherwise print "No"
fruits = ["orange", "mango", "apple"]
if "apple" in fruits:
    print("Yes, apple is in the fruits list")
else:
    print("No")


#Given a list of numbers [4, 2, 9, 1, 5, 6], sort the list in ascending order and print it.
numbers = [4, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)

#Given a list of strings ["a", "b", "c", "d", "e"], reverse the list and print it
#Method: Using slicing
strings = ["a", "b", "c", "d", "e"]
reversed_strings = strings[::-1]
print(reversed_strings)

strings = ["a", "b", "c", "d", "e"]
print( strings[::-1])

#Create a nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]. Access and print the element 5 from this list.

#ANSWER
#nested_list[1] accesses the second sublist [4, 5, 6].
#nested_list[1][1] then accesses the second element in that sublist, which is 5.

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
element = nested_list[1][1]
print(element)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][1])



prices = [10, 20, 30]  # A list of prices
total_sum = 0  # Initialize the total sum

for price in prices:
    total_sum += price  # Add each price to the total sum

print("Total sum:", total_sum)  # Print the total sum



