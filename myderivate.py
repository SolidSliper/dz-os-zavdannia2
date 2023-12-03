def myderive(f, var):
    if isinstance(f, int) or type(f)==float:
        return 0
    elif type(f)==str:
        return 1 if f == var else 0
    elif isinstance(f, list):
        operator = f[0]
        if operator == '+':
            return ['+', myderive(f[1], var), myderive(f[2], var)]
        elif operator == '-':
            return ['-', myderive(f[1], var), myderive(f[2], var)]
        elif operator == '*':
            return ['+', ['*', myderive(f[1], var), f[2]], ['*', f[1], myderive(f[2], var)]]
        elif operator == '/':
            citatel = ['-', ['*', myderive(f[1], var), f[2]], ['*', f[1], myderive(f[2], var)]]
            menovatel = ['*', f[2], f[2]]
            return ['/', citatel, menovatel]
    return None
