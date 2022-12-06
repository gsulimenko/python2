number_list = []
sum_list = []

for i in range(1, 1001, 2):
    number_list.append(i ** 3)

final_sum = 0
for num in number_list:
    sum = 0
    check_num = num
    while check_num > 0:
        sum += check_num % 10
        check_num //= 10
    if sum % 7 == 0:
        final_sum += num

print(final_sum)

final_sum = 0
for num in number_list:
    sum = 0
    num += 17
    check_num = num

    while check_num > 0:
        sum += check_num % 10
        check_num //= 10
    if sum % 7 == 0:
        final_sum += num

print(final_sum)