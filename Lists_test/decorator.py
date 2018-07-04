def bread(func):
    def wrapper():
        print
        "</------\>"
        func()
        print
        "<\______/>"

    return wrapper

def ingredients(func):
    def wrapper():
        print
        "#помидоры#"
        func()
        print
        "~салат~"

    return wrapper

def sandwich(food="--ветчина--"):
    print
    food

sandwich()
# выведет: --ветчина--
sandwich = bread(ingredients(sandwich))
sandwich()
# выведет:
# </------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>


#И используя  синтаксис декораторов:

@bread
@ingredients
def sandwich(food="--ветчина--"):
    print
    food


sandwich()
# выведет:
# </------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>



#Передача(«проброс») аргументов в декорируемую функцию

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):  # аргументы прибывают отсюда
        print
        "Смотри, что я получил:", arg1, arg2
        function_to_decorate(arg1, arg2)

    return a_wrapper_accepting_arguments


# Теперь, когда мы вызываем функцию, которую возвращает декоратор,
# мы вызываем её "обёртку", передаём ей аргументы и уже в свою очередь
# она передаёт их декорируемой функции

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print
    "Меня зовут", first_name, last_name


print_full_name("Питер", "Венкман")
# выведет:
# Смотри, что я получил: Питер Венкман
# Меня зовут Питер Венкман
# *