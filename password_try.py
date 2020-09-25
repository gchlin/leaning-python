# the passoword is 1
x = 3
passoword = input('please input the passoword: ')
passoword = str(passoword)
while True:
	print(passoword)
	if passoword == '1':
		print('your passoword is correct')
		break
	else:
		print('your password is uncorrect, please retype it')
		print('reman', x, 'times you can tryout')
		x = x - 1
		if x == 0:
			print('No more chance')
			break
		passoword = input('please input the passoword: ')