lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 = []
for item in lst1:
    if type(item) == str:
        lst2.append(item)
print(lst2)

lst2 = [item for item in lst1 if isinstance(item, str)]
print(lst2)
