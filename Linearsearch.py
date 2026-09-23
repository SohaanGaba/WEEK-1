numbers = [10, 23, 45, 70, 11, 15]
target = 70

found_index = -1

for index, element in enumerate(numbers):
    if element == target:
        found_index = index
        break


if found_index != -1:
    print(f"Found {target} at index {found_index}")
else:
    print(f"{target} is not in the list")