import decimal

# Immutable types:  int, float, complex, str, bool
int_example = 1
float_example = 0.1
decimal_example = decimal.Decimal(0.3)
bool_example = True or False

# Immutable collections
str_example = "1jfashfaks__"
tuple_example = (int_example, float_example, str_example)
frozenset_example = frozenset([])

template = "I am {}, my age is {1}!"
pavel_data = ("Pavel", 12)
igor_data = ("Igor", 40, 3)

# Mutable types - all collections: list, set, dict
list_example = [1, 2, 3]
set_example = {1, 2, 4, 5, 7}
dict_example = {"name": "Example", "Key": "Value"}

# semaphor_map = {"green": "go", "yellow": "wait", "red": "stop"}
# current_semaphore_color = input()
# current_semaphore_color_lowered = current_semaphore_color.lower()
# print(semaphor_map.get(current_semaphore_color_lowered, "I don't know!"))


happy_list = ["Egor", "Mom", "Dad"]

try:
    happy_index = int(input("Who is happy today? "))
except UnicodeDecodeError:
    print()
else:
    try:
        print(happy_list[happy_index])
    except IndexError:
        print("wrong index")


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
