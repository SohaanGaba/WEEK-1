user_list = input("Enter numbers separated by spaces: ").split()
numbers = [int(x) for x in user_list]

numbers.sort()
print(f"Sorted list: {numbers}")

target = int(input("Enter the number to search for: "))

low = 0
high = len(numbers) - 1
found_index = -1

while low <= high:
    mid = (low + high) // 2
    
    if numbers[mid] == target:
        found_index = mid
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1 

if found_index != -1:
    print(f"Found {target} at index {found_index} in the sorted list.")
else:
    print(f"{target} was not found in the list.")