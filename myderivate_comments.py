def myderive(f, var):
    if isinstance(f, int) or isinstance(f, float):
        # Якщо f - константа, то похідна від константи - нуль
        return 0
    elif isinstance(f, str):
        # Якщо f - змінна, то похідна від змінної - 1, якщо змінна співпадає з var
        return 1 if f == var else 0
    elif isinstance(f, list):
        # Якщо f - список, то розглядаємо різні арифметичні операції
        operator = f[0]
        if operator == '+':
            # Правило суми
            return ['+', myderive(f[1], var), myderive(f[2], var)]
        elif operator == '-':
            # Правило різниці
            return ['-', myderive(f[1], var), myderive(f[2], var)]
        elif operator == '*':
            # Правило множення
            return ['+', ['*', myderive(f[1], var), f[2]], ['*', f[1], myderive(f[2], var)]]
        elif operator == '/':
            # Правило ділення
            numerator_derivative = ['-', ['*', myderive(f[1], var), f[2]], ['*', f[1], myderive(f[2], var)]]
            denominator_derivative = ['*', f[2], f[2]]
            return ['/', numerator_derivative, denominator_derivative]
    # Якщо f - невідомий випадок, повертаємо None
    return None

# Приклади використання
#print(myderive(1, "x"))               # 0
#print(myderive("y", "x"))              # 0
#print(myderive("x", "x"))              # 1
#print(myderive(["-", 2, "x"], "x"))    # ['-', 0, 1]
#print(myderive(["*", 2, "x"], "x"))    # ['+', ['*', 0, 'x'], ['*', 2, 1]]
#print(myderive(["*", "x", "x"], "x"))  # ['+', ['*', 1, 'x'], ['*', 'x', 1]]
#print(myderive(["*", "x", "x"], "y"))  # ['+', ['*', 0, 'x'], ['*', 'x', 0]]
#print(myderive(["*", ["-", "x", 1], "x"], "x"))  # ['+', ['*', ['-', 1, 0], 'x'], ['*', ['-', 'x', 1], 1]]
#print(myderive(["+", "x", "x"], "x"))  # ['+', 1, 1]
#print(myderive(["+", "y", "x"], "x"))  # ['+', 0, 1]
#print(myderive(["/", "x", "y"], "y"))  # ['/', ['-', ['*', 0, 'y'], ['*', 'x', 1]], ['*', 'y', 'y']]
