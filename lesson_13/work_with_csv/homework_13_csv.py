import csv

# def read_csv_file(csv_file_path):
#     with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile)
#         headers = next(reader)
#         file_data = list(reader)
#         return headers, file_data
#
# def write_csv_file(csv_file_path, headers, file_data):
#     with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(headers)
#         writer.writerows(file_data)
#
# def find_duplicates(csv_file_1, csv_file_2, result_file):
#     headers1, data1 = read_csv_file(csv_file_1)
#     headers2, data2 = read_csv_file(csv_file_2)
#
#     if headers1 != headers2:
#         raise ValueError("Файли мають різні заголовки")
#
#     set1 = set(map(tuple, data1))
#     set2 = set(map(tuple, data2))
#
#     duplicates = list(set1 & set2)
#
#     write_csv_file(result_file, headers1, duplicates)
#
#
# find_duplicates('random.csv', 'random_2.csv', 'result_selivanov.csv')

def finding_duplicates(csv_file_1=None, csv_file_2=None, result_file=None, *args, **kwargs):
    def read_csv_file(csv_file_path):
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            file_data = list(reader)
            return headers, file_data

    def write_csv_file(csv_file_path, headers, file_data):
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(file_data)

    headers1, data1 = read_csv_file(csv_file_1)
    headers2, data2 = read_csv_file(csv_file_2)

    if headers1 != headers2:
        raise ValueError("Файли мають різні заголовки")

    set1 = set(map(tuple, data1))
    set2 = set(map(tuple, data2))

    duplicates = list(set1 & set2)

    write_csv_file(result_file, headers1, duplicates)


finding_duplicates('random.csv', 'random_2.csv', 'result_selivanov.csv')