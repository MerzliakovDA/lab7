def solve_task():
 
    try:
        A = []
        print("Введите 10 целых чисел:")
        for i in range(10):
            num = int(input(f"Элемент {i+1}: "))
            A.append(num)

        positive_multiples_of_11 = [x for x in A if x > 0 and x % 11 == 0]
        
        count = len(positive_multiples_of_11)
        
        if count > 0:
            difference = max(positive_multiples_of_11) - min(positive_multiples_of_11)
        else:
            difference = 0

        print("\nРезультаты:")
        print("Список A:", A)
        print("Положительные элементы, кратные 11:", positive_multiples_of_11)
        print("Количество таких элементов:", count)
        print("Разность между максимальным и минимальным из них:", difference)

    except ValueError:
        print("Ошибка: Пожалуйста, вводите целые числа.")


if __name__ == "__main__":
    solve_task()
