def main():
    print("--- Простой калькулятор ---")
    
    try:
        # 1. Ввод чисел
        num1 = float(input("Введите первое число: "))
        operation = input("Выберите действие (+, -, *, /): ").strip()
        num2 = float(input("Введите второе число: "))

        # 2. Алгоритм вычислений
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            # Проверка деления на ноль
            if num2 == 0:
                print("Ошибка: На ноль делить нельзя!")
                return
            result = num1 / num2
        else:
            print("Ошибка: Неверная операция!")
            return

        # 3. Вывод результата
        print(f"Результат: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("Ошибка: Пожалуйста, вводите только числа!")

if __name__ == "__main__":
    main()
