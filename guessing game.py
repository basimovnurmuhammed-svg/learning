def main():
    target = 69
    last_diff = None # Здесь будем хранить предыдущее расстояние
    
    print("--- Игра 'Теплее-Холоднее' ---")
    print("Я загадал число. Попробуй угадать его (это 69, но давай проверим точность)!")

    while True:
        try:
            guess = int(input("\nВведите число: "))
            
            if guess == target:
                print(f"Победа! Это число {target}!")
                break
            
            # Считаем текущее расстояние до цели
            current_diff = abs(target - guess)

            if last_diff is None:
                # Это была первая попытка, сравнивать пока не с чем
                if current_diff <= 5:
                    print("Сейчас горячо, но это только начало!")
                else:
                    print("Холодно! Попробуй другое число.")
            else:
                # Сравниваем: текущее расстояние меньше предыдущего?
                if current_diff < last_diff:
                    print("Теплее! (ты приближаешься)")
                elif current_diff > last_diff:
                    print("Холоднее... (ты уходишь не туда)")
                else:
                    print("Так же! Ты на том же расстоянии, но с другой стороны?")

            # Запоминаем текущее расстояние для следующего шага
            last_diff = current_diff

        except ValueError:
            print("Вводи только целые числа!")

if __name__ == "__main__":
    main()
