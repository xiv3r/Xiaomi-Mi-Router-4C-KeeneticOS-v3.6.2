import sys
import telnetlib
import ftplib

import gateway
router_ip_address=gateway.get_ip_address()

try:	
	ftp=ftplib.FTP(router_ip_address)
except:
	print ("ftp сервер не запущен")
	print ("Запустите 1 - Connect to router ещё раз")
	sys.exit(1)
try:	
	file=open('data/Breed_Xiaomi4c.bin', 'rb')
except:
	print ("Breed_Xiaomi4c.bin не найден")
	sys.exit(1)
print ("Загружаю Xiaomi4a_breed.bin в роутер")
ftp.storbinary(f'STOR /tmp/Breed_Xiaomi4c.bin', file)
file.close()
ftp.quit()
print ("Загрузка завершена")

tn = telnetlib.Telnet(router_ip_address)
tn.read_until(b"login:")
tn.write(b"root\n")
tn.read_until(b"root@XiaoQiang:~#")
print ("Записываю загрузчик Breed")
tn.write(b"mtd -e Bootloader write /tmp/Breed_Xiaomi4c.bin Bootloader\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"reboot\n")
tn.read_until(b"root@XiaoQiang:~#")
print ("Запись загрузчика завершена")
print ("")
print ("Роутер перезапускаеться в загрузчик Breed, ждите 15 секунд")
print ("")
print ("Заходим в браузере по адрессу 192.168.1.1")
print ("")


