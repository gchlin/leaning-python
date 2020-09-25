# the passoword is 1
password = "aaa111"
i = 3
while i > 0:
	i = i - 1
	pwd = input('please input the password: ')
	print(pwd)
	if pwd == password:
		print('your password is correct')
		break
	else:
		print('your password is uncorrect, please retype it')
		if i > 0:
			print('reman', i, 'times you can tryout')
		else:
			print("no chance anymore")
