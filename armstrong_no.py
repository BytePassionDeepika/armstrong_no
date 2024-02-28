def is_armstrong(num):
    order = len(str(num))
    temp = num
    sum_of_digits = 0
    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit ** order
        temp //= 10
    return num == sum_of_digits

def print_armstrong_numbers(start, end):
    for num in range(start, end + 1):
        if is_armstrong(num):
            print(num, end=' ')

start_range = 100
end_range = 1000

print(f"Armstrong Numbers between {start_range} and {end_range}:")
print_armstrong_numbers(start_range, end_range)
