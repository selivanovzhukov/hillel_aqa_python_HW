import re
import string

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

task_01 = adwentures_of_tom_sawer.replace("\n", " ")
print(task_01)

# task 02 ==
""" Замініть .... на пробіл
"""

task_02 = task_01.replace("....", "")
print(task_02)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

task_03 = " ".join(task_02.split())
print("task3",task_03)

# task 04
""" Виведіть, скільки разів у тексті зустрічається літера "h"
"""

task_04 = task_03.count("h")
print(task_04)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

task_05 =  task_03.split()
cleaned_words = [word.strip(string.punctuation) for word in task_05]
capitalized_words = [word for word in cleaned_words if word and word[0].istitle()]
print(len(capitalized_words))
print(cleaned_words)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

task_06_first_index = task_03.find("Tom")
second_index = task_03.find("Tom", task_06_first_index + 1)
print(f'Слово том вдруге зустрічається на позиції: {second_index}')


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = re.split(r'[.!?]', task_03)
adwentures_of_tom_sawer_sentences = [sentence.strip() for sentence in adwentures_of_tom_sawer_sentences if sentence.strip()]
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

sentence_4 =  adwentures_of_tom_sawer_sentences[3]
print(sentence_4.lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

task_09 = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        task_09 = True
print(task_09)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

task_10 = adwentures_of_tom_sawer_sentences[-1]
wrds_in_last_sentence = task_10.split()
print(len(wrds_in_last_sentence))
