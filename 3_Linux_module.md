# Task 3

## Задание 1 - Управление доступом к файлам
1.1. Создайте трёх пользователей petersen, meyers, william и объедините их в группу students
```bash
arina@ubuntu:~$ sudo groupadd students
arina@ubuntu:~$ sudo useradd petersen
arina@ubuntu:~$ sudo useradd meyers
arina@ubuntu:~$ sudo useradd william
arina@ubuntu:~$ sudo gpasswd -M petersen,meyers,william students
arina@ubuntu:~$ grep students /etc/group
students:x:1001:petersen,meyers,william
```
 
1.2. Измените пользователям пароли
```bash
arina@ubuntu:~$ sudo -i
[sudo] password for arina:
root@ubuntu:~# passwd petersen
New password:
Retype new password:
passwd: password updated successfully
root@ubuntu:~# passwd meyers
New password:
Retype new password:
passwd: password updated successfully
root@ubuntu:~# passwd william
New password:
Retype new password:
passwd: password updated successfully
```
1.3. Создайте директорию /home/students, где эти три пользователя могут работать совместно с файлами.
```bash
arina@ubuntu:/$ sudo -i
root@ubuntu:~# cd /
root@ubuntu:/# mkdir -p /home/students
root@ubuntu:/# chgrp -R students /home/students
```
1.4. Настройте доступ таким образом, чтобы был возможен только пользовательский и групповой доступ на создание и удаление файлов в /home/students.
```bash
arina@ubuntu:~$ sudo chmod -R 2770 /home/students/
[sudo] password for arina:
arina@ubuntu:~$ cd ../students/
-bash: cd: ../students/: Permission denied
arina@ubuntu://$ touch home/students/file
touch: cannot touch 'home/students/file': Permission denied
```
1.5. Файлы, созданные в этой директории, должны автоматически присваиваться группе студентов.
```bash
arina@ubuntu:~$ sudo -i
[sudo] password for arina:
root@ubuntu:/# cd home/students/
root@ubuntu:/home/students# touch test
root@ubuntu:/home/students# ls -l
total 0
-rw-r--r-- 1 root students 0 Oct 11 19:35 test
```
## Задание 2 - Процессы
2.1. Запустите утилиту sleep четыре раза с разными интервалами в фоновом режиме.
```bash
arina@ubuntu:~$ sleep 1000 &
arina@ubuntu:~$ sleep 1000 &
[1] 1378
arina@ubuntu:~$ sleep 1001 &
[2] 1379
arina@ubuntu:~$ sleep 1002 &
[3] 1380
arina@ubuntu:~$ sleep 1003 &
[4] 1381
```
2.2. Остановите все четыре процесса четырьмя разными способами.
```bash
arina@ubuntu:~$ kill -SIGTSTP 1378
arina@ubuntu:~$ kill -TSTP 1379
arina@ubuntu:~$ kill -19 1380
arina@ubuntu:~$ kill -STOP 1381
```
2.3. Проверьте их статусы, используя команду jobs.
```bash
arina@ubuntu:~$ jobs -l
[1]   1378 Stopped                 sleep 1000
[2]   1379 Stopped                 sleep 1001
[3]-  1380 Stopped (signal)        sleep 1002
[4]+  1381 Stopped (signal)        sleep 1003
```
2.4. Завершите один из этих процессов.
```bash
arina@ubuntu:~$ kill -s TERM 1380
arina@ubuntu:~$ jobs -l
[1]   1378 Stopped                 sleep 1000
[2]   1379 Stopped                 sleep 1001
[3]-  1380 Terminated              sleep 1002
[4]+  1381 Stopped (signal)        sleep 1003
```
2.5. Принудительно завершите (убейте) один из них.
```bash
arina@ubuntu:~$ kill -n 9 1378
arina@ubuntu:~$ kill -s CONT 1378
-bash: kill: (1378) - No such process
[1]   Killed                  sleep 1000
```
 2.6. Возобновите работу в фоновом режиме остальных двух процессов двумя разными способами.
```bash
arina@ubuntu:~$ kill -SIGCONT 1379
arina@ubuntu:~$ kill -18 1381
arina@ubuntu:~$ jobs -l
[1]-  1379 Running                 sleep 1000 &
[2]+  1381 Running                 sleep 1001 &
```
2.7. Завершите оба возобновленных процесса одновременно одной командой.
```bash
arina@ubuntu:~$ disown -a
arina@ubuntu:~$ jobs -l
```
## Задание 3 - lsof
3.1. Запустите утилиту sleep с перенаправлением stdout и stderr в 2 разных файла (да, они будут пустыми, но это лишь для примера).
```bash
arina@ubuntu:~$ cd testdir/
arina@ubuntu:~/testdir$ touch output
arina@ubuntu:~/testdir$ touch output_errors
arina@ubuntu:~/testdir$ sleep 300 > output 2> output_errors
```
3.2. Используя lsof найдите, какие файлы используются вашим sleep-процессом. 
```bash
arina@ubuntu:~/testdir$ pidof sleep
1463
arina@ubuntu:~/testdir$ lsof -p 1463
COMMAND  PID  USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
sleep   1463 arina  cwd    DIR  253,0     4096 403383 /home/arina/testdir
sleep   1463 arina  rtd    DIR  253,0     4096      2 /
sleep   1463 arina  txt    REG  253,0    39256 787491 /usr/bin/sleep
sleep   1463 arina  mem    REG  253,0  3035952 786773 /usr/lib/locale/locale-archive
sleep   1463 arina  mem    REG  253,0  2029224 793554 /usr/lib/x86_64-linux-gnu/libc-2.31.so
sleep   1463 arina  mem    REG  253,0   191472 793514 /usr/lib/x86_64-linux-gnu/ld-2.31.so
sleep   1463 arina    0u   CHR  136,0      0t0      3 /dev/pts/0
sleep   1463 arina    1w   REG  253,0        0 407947 /home/arina/testdir/output
sleep   1463 arina    2w   REG  253,0        0 407948 /home/arina/testdir/output_errors
```

Отдельной командой найдите файл, в который переадресован stdout вашего sleep-процесса.
```bash
arina@ubuntu:/$ readlink /proc/1463/fd/1
/home/arina/testdir/output
```
3.3. Используя только одну команду lsof, выведите на экран все установленные TCP-соединения (ESTABLISHED).
```bash
arina@ubuntu:/$ lsof -n | grep TCP
arina@ubuntu:/$ lsof -n -itcp
```
