import math

def process_list(numbers, C):

    count_greater_than_c = sum(1 for num in numbers if num > C)

    
    if not numbers:  
        product_after_max = 1
    else:
        max_abs_val = max(numbers, key=abs)
        max_abs_index = numbers.index(max_abs_val)
        if max_abs_index == len(numbers) - 1:
            product_after_max = 1  
        else:
            product_after_max = 1
            for num in numbers[max_abs_index + 1:]:
                product_after_max *= num
    
    negative_nums = [num for num in numbers if num < 0]
    positive_nums = [num for num in numbers if num >= 0]
    transformed_list = negative_nums + positive_nums

    return count_greater_than_c, product_after_max, transformed_list


if __name__ == "__main__":
    try:
      
        input_str = input("Введите список вещественных чисел через пробел: ")
        numbers = [float(x) for x in input_str.split()]
        C = float(input("Введите число C: "))

        count, product, transformed = process_list(numbers, C)

        print("Исходный список:", numbers)
        print("Количество элементов, больших C:", count)
        print("Произведение элементов после максимального по модулю:", product)
        print("Преобразованный список:", transformed)

    except ValueError:
         print("Ошибка: Неверный ввод. Пожалуйста, вводите числа.")
