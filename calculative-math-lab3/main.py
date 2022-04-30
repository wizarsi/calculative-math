from manage_data_functions import *

if __name__ == '__main__':
    count_method = choose_calculative_method()
    equation = choose_equation()
    a, b = choose_borders()
    accuracy = choose_accuracy()
    try:
        answer, count_partitions = count_method(equation, a, b, accuracy)
        print(f"Ответ:{answer} Число разбиений:{count_partitions}")
    except Exception:
        print("Не получилось найти интеграл")
