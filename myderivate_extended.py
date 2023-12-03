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
		elif operator == '^':
			base = f[1]
			exponent = f[2]
			if isinstance(exponent, (int, float)):
				return ['*', exponent, ['^', base, exponent - 1]]
			else:
				return ['*', f, ['+', ['*', myderive(exponent, var), ['log', base]], ['*', myderive(base, var), ['/', exponent, base]]]]
		if f[1] != var and type(f[1])!=list:
			return 0
		else:    
			if operator == 'sqrt':
				return ["*", myderive(f[1]), ['/', 1, ['*', 2, ['sqrt', f[1]]]]]
			elif operator == 'exp':
				return ["*", myderive(f[1]), ['exp', f[1]]]  
			elif operator == 'ln':
				return ["*", myderive(f[1]), ['/', 1, f[1]]]
			elif operator == 'sin':
				return ['*', myderive(f[1], var), ['cos', f[1]]]
			elif operator == 'cos':
				return ['-', 0, ['*', myderive(f[1], var), ['cos', f[1]]]]
	return None
