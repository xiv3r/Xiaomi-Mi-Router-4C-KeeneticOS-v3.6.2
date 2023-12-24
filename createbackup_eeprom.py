import sys
import telnetlib
import ftplib

import gateway
router_ip_address=gateway.get_ip_address()
	
try:	
	tn = telnetlib.Telnet(router_ip_address)
except:
	print ("")
	print ("telnet сервер не запущен")
	print ("")
	print ("Запустите 0.start_main.bat ещё раз")
	print ("")
	sys.exit(1)
tn.read_until(b"login:")
tn.write(b"root\n")
tn.read_until(b"root@XiaoQiang:~#")
print ("Считываю eeprom.bin")
tn.write(b"dd if=/dev/mtd3 of=/tmp/eeprom.bin\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"exit\n")
print ("Файл eeprom.bin создан")

ftp=ftplib.FTP(router_ip_address)
file=open('data/eeprom.bin', 'wb')
print ("Сохраняю файл eeprom.bin на компьютер")
ftp.retrbinary(f'RETR /tmp/eeprom.bin', file.write)
file.close()
ftp.quit()
print ("Выполнено")

tn = telnetlib.Telnet(router_ip_address)
tn.read_until(b"login:")
tn.write(b"root\n")
tn.read_until(b"root@XiaoQiang:~#")
print ("Удаляю временные файлы")
tn.write(b"rm /tmp/eeprom.bin\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"exit\n")
print ("")
print ("")

