num_list = [x for x in range(1, 21)]
print(num_list)
num_pair_sum = []
for num in num_list:
    if num % 2 == 0:
        num_pair_sum.append(num)
print('Сума парних чисел:', sum(num_pair_sum))
