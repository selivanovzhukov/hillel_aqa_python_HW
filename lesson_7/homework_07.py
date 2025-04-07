# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def int_sum(first_num: int, second_num):
    sum_result = first_num + second_num
    print(sum_result)
int_sum(2, 90)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def int_medium(num_list: list):
    result = sum(num_list) / len(num_list)
    print(result)

int_medium(num_list=[20,40,95,4])

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

# def string_reverser():
#     some_string = input('input string: ')
#     print(some_string[::-1])

def string_reverser(some_string: str):
    print(some_string[::-1])

string_reverser('some string')

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word_in_list(word_list: list):
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

word_list = ['cat', 'dog', 'rabbit', 'monkey', 'horse', 'giraffe']
print(longest_word_in_list(word_list))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""
homework_06_1 
# list_of_symbols = input('Enter some text:')
# unique_symbols = set(list_of_symbols)
# 
# if len(unique_symbols) >= 10:
#     print(True)
# else: print(False)
"""

def unique_symbols_count():
    """User types any text"""
    list_of_symbols = input('Enter some text:')
    """Collecting only unique symbols"""
    unique_symbols = set(list_of_symbols)
    """Counting unique symbols and comparing ot the set condition"""
    if len(unique_symbols) >= 10:
        print(True)
    else:
        print(False)

unique_symbols_count()

# task 8
"""
Homework 6.3
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 = []
for item in lst1:
    if type(item) == str:
        lst2.append(item)
print(lst2)

lst2 = [item for item in lst1 if isinstance(item, str)]
print(lst2)

"""

def string_taker(list1: list):
    """Taking only string type objects from the list"""
    list2 = []
    for item in list1:
        if type(item) == str:
            list2.append(item)
    print(list2)


lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
string_taker(lst1)

# task 9

"""
Homework 6.4
num_list = [x for x in range(1, 21)]
print(num_list)
num_pair_sum = []
for num in num_list:
    if num % 2 == 0:
        num_pair_sum.append(num)
print('Сума парних чисел:', sum(num_pair_sum))
"""

def sum_of_even_nums(num_list: list):
    even_num_list = []
    for num in num_list:
        if num % 2 == 0:
            even_num_list.append(num)
    return sum(even_num_list)

num_list1 = [x for x in range(1, 21)]
print("Сума парних чисел: ", sum_of_even_nums(num_list=num_list1))


# task 10

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

my_name = ('Kyrylo', 'Selivanov', 31, 'QA Engineer', 'Odesa')

def add_user_to_records(records, user):
    """adding new user in the beginning of the list"""
    new_records = records.copy()
    new_records.insert(0, user)
    return new_records

def swap_people(records, index1, index2):
    """swapping records places"""
    records[index1], records[index2] = records[index2], records[index1]

def check_ages_by_indexes(records, rec_indexes, min_age=30):
    """finding users with min age 30"""
    people = [records[i] for i in rec_indexes if records[i][2] >= min_age]
    return len(people) == len(rec_indexes), people

# Основна логіка
new_people_records = add_user_to_records(people_records, my_name)
swap_people(new_people_records, 1, 5)

indexes = [6, 10, 13]
print(new_people_records[6], new_people_records[10], new_people_records[13])

result, people_above_30 = check_ages_by_indexes(new_people_records, indexes)
print(result, people_above_30)


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""