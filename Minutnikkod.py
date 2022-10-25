import time

def Minutnik(czas):
	
	while czas:
		mins, secs = divmod(czas, 60)
		minutnik = '{:02d}:{:02d}'.format(mins, secs)
		print(minutnik, end="\r")
		time.sleep(1)
		czas -= 1
	
	print('koniec czasu')

czas = input("podaj czas w sekundach: ")

Minutnik(int(czas))
