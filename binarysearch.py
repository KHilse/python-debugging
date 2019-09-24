input_list = [1,2,3,5,8,13,21,34,55,61,66,72,74,75,79,81,83,88,91,92,99]
target = 0

def binary_search(ls,target):
    min = 0
    max = len(input_list) - 1
    guess = 0
    guess_count = 1
    while (min <= max):
        guess = (min + max) // 2

        print("Guess #", guess_count, guess)
        guess_count += 1

        if target == input_list[guess]:
            return guess
        elif (input_list[guess] > target):
            max = guess - 1
        elif (input_list[guess] < target):
            min = guess + 1
        else:
            min = max
    return -1

print(binary_search(input_list,target))