# the passoword is 1
x = 3
passoword = input('please input the passoword: ')
passoword = str(passoword)
while x > 0:
	print(passoword)
	if passoword == '1':
		print('your passoword is correct')
		break
	else:
		print('your password is uncorrect, please retype it')
		print('reman', x, 'times you can tryout')
		x = x - 1