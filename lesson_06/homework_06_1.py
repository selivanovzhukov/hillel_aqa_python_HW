list_of_symbols = input('Enter some text:')
unique_symbols = set(list_of_symbols)

if len(unique_symbols) >= 10:
    print(True)
else: print(False