"""
03. создать 5-и элементный словарь, где ключи – сампловые 10 элементные числовые подстроки (
как бы номера телефонов), а значения – None . Далее вручную через input вводить (заполнять)
по номеру тефона какое- то имя, пусть Петя, Маша, Коля... а при заполнении этот получившийся
уже заполненный словарь записать в json - формате уже в json-файл с соответствующ. расширением?
"""
from random import sample
import json

nums_in_line = "0123456789"
dict = {}

for _ in range(5):
    dict["".join(sample(nums_in_line, 10))] = None

print(dict)

for obj in dict:
    name = str(input("Input name: "))
    dict[obj] = name

print(dict)

json_obj = json.dumps(dict, indent=4)

with open("num_3_result.json", "w") as f:
    f.write(json_obj)
