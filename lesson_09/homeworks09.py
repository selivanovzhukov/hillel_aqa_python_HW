"""Homework 8"""
def element_sum(list_of_elements: list):
    """Summing elements in the list of strings"""
    result = []
    for item in list_of_elements:
        try:
            elements = (item.split(','))
            sum_of_elements = sum(int(num) for num in elements)
            result.append(sum_of_elements)
        except ValueError:
            result.append("Не можу це зробити")
    return result

element_sum(["1,2,3","4,5,6"])

"""Homework 6.4"""
def sum_of_even_nums(num_list: list):
    even_num_list = []
    for num in num_list:
        if num % 2 == 0:
            even_num_list.append(num)
    return sum(even_num_list)


"""homework_06_1 """
def unique_symbols_count(symbols_list: list):
    """Collecting only unique symbols"""
    unique_symbols = set(symbols_list)
    """Counting unique symbols and comparing ot the set condition"""
    if len(unique_symbols) >= 10:
        return True
    else:
        return False