user_list = input("Enter numbers separated by spaces: ").split()
numbers = [int(x) for x in user_list]
n = len(numbers)
for i in range(n):
    swapped = False
    
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True       
    if not swapped:
        break
print(f"Sorted list: {numbers}")