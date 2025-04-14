def element_sum(list_of_elements: list):
    """Summing elements in the list of strings"""
    for item in list_of_elements:
        try:
            elements = (item.split(','))
            sum_of_elements = sum(int(num) for num in elements)
            print(sum_of_elements)
        except ValueError:
            print("Не можу це зробити")




list_of_elements = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
element_sum(list_of_elements)
