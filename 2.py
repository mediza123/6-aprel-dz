import math

def main():
    while True:
        print("\nДоступные операции:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Факториал")
        print("7. Квадратный корень")
        print("8. Среднее арифметическое")
        print("exit - Выход")
        
        choice = input("\nВыберите операцию (1-8): ")
        
        if choice == 'exit':
            break
            
        try:
            if choice == '1':
                a = float(input("Первое число: "))
                b = float(input("Второе число: "))
                print(f"Результат: {a + b}")
                
            elif choice == '2':
                a = float(input("Первое число: "))
                b = float(input("Второе число: "))
                print(f"Результат: {a - b}")
                
            elif choice == '3':
                a = float(input("Первое число: "))
                b = float(input("Второе число: "))
                print(f"Результат: {a * b}")
                
            elif choice == '4':
                a = float(input("Делимое: "))
                b = float(input("Делитель: "))
                if b == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    print(f"Результат: {a / b}")
                    
            elif choice == '5':
                a = float(input("Основание: "))
                b = float(input("Степень: "))
                print(f"Результат: {a ** b}")
                
            elif choice == '6':
                n = int(input("Число: "))
                if n < 0:
                    print("Ошибка: факториал отрицательного числа не существует!")
                else:
                    print(f"Результат: {math.factorial(n)}")
                    
            elif choice == '7':
                x = float(input("Число: "))
                if x < 0:
                    print("Ошибка: нельзя извлечь корень из отрицательного числа!")
                else:
                    print(f"Результат: {math.sqrt(x)}")
                    
            elif choice == '8':
                nums = input("Введите числа через пробел: ").split()
                numbers = [float(num) for num in nums]
                print(f"Результат: {sum(numbers)/len(numbers)}")
                
            else:
                print("Неверный выбор операции!")
                
        except ValueError:
            print("Ошибка: введите корректные числа!")

if __name__ == "__main__":
    main()
