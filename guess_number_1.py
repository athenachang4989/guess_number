import random
r = random. randint(1,100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請猜數字：')
	num = int(num)
	if num == r:
		print('猜中了！')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('小一點')
	elif num < r:
		print('大一點')
	print('這是你猜的第', count, '次')