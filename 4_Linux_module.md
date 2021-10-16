# Task 4
## Задание 1 - Logging
1.1. Используя journalctl, одной командой отобразите все записи журнала за последние сутки, которые оставлены пользователем с id 100.
```bash
arina@ubuntu:/$ journalctl --since "24 hours ago" -e _UID=100
Oct 12 16:30:34 ubuntu systemd-networkd[619]: enp0s8: DHCPv4 address 10.0.3.15/24 via 10.0.3.2
Oct 12 16:30:35 ubuntu systemd-networkd[619]: enp0s3: Gained carrier
Oct 12 16:30:35 ubuntu systemd-networkd[619]: enp0s3: DHCPv4 address 192.168.56.102/24
Oct 12 16:30:35 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 16:30:36 ubuntu systemd-networkd[619]: enp0s8: Gained IPv6LL
Oct 12 16:30:37 ubuntu systemd-networkd[619]: enp0s3: Gained IPv6LL
Oct 12 16:35:35 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 16:40:36 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 16:45:36 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 16:50:36 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 16:55:36 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 17:00:36 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 17:05:36 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 17:10:36 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 17:15:35 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 17:20:35 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 17:25:35 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 17:30:34 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 17:35:33 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 17:40:33 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 17:45:33 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 17:50:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 17:55:33 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 18:00:33 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 18:05:33 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 18:10:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 18:15:33 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 18:20:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 18:25:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 18:30:33 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 18:35:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 18:40:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 18:45:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 18:50:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 18:55:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 19:00:31 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 19:05:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 19:10:33 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 19:15:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 19:20:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 19:25:33 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 19:30:33 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 19:35:33 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 19:40:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 19:45:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 19:50:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 19:55:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 20:00:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 20:05:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 20:10:32 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 20:15:31 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 20:20:30 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 20:25:31 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
Oct 12 20:30:30 ubuntu systemd-networkd[619]: enp0s3: DHCP: No gateway received from DHCP server.
```
## Задание 2 - File system & Links
2.1. Одной командой создайте отчет по размерам всех файлов, находящихся в директории /usr/sbin, имя которых начинается с xfs.
```bash
arina@ubuntu:/usr/bin$ touch ~/testdir/report
arina@ubuntu:/usr/bin$ du -ah /usr/bin | grep 'xfs' > ~/testdir/report
arina@ubuntu:/usr/bin$ cat ~/testdir/report
4.0K    /usr/bin/xfs
0       /usr/bin/xfs_test
0       /usr/bin/xfsrrr_test
```
2.2. Для пользователей petersen и meyers, которых вы создавали в системе в рамках предыдущего домашнего задания, создайте общую папку и два общих файла. 
```bash
arina@ubuntu:/home$ sudo mkdir shared_dir
arina@ubuntu:/home$ sudo groupadd metersen
arina@ubuntu:/home$ sudo gpasswd -M petersen,meyers metersen
arina@ubuntu:/home$ cat /etc/group | grep metersen
metersen:x:1005:petersen,meyers
arina@ubuntu:/home$ sudo chgrp -R metersen /home/shared_dir/
arina@ubuntu:/home$ sudo chmod -R 2770 /home/shared_dir
arina@ubuntu:/home$ sudo touch shared_dir/file0
arina@ubuntu:/home$ sudo touch shared_dir/file1
arina@ubuntu:/home$ sudo ls -laR shared_dir/
shared_dir/:
total 8
drwxrws--- 2 root metersen 4096 Oct 13 17:51 .
drwxr-xr-x 7 root root     4096 Oct 13 17:38 ..
-rw-r--r-- 1 root metersen    0 Oct 13 17:50 file0
-rw-r--r-- 1 root metersen    0 Oct 13 17:51 file1
```
Создайте в их домашних директориях все виды ссылок на этих объекты. Удалите эти объекты и выведите результаты обращения к ссылкам. Удалите все ссылки.
```bash
arina@ubuntu:/home$ cd home/petersen
arina@ubuntu:/home/petersen$ sudo ln /home/shared_dir/file0 file0_hardlink
arina@ubuntu:/home/petersen$ cd /home/meyers/
arina@ubuntu:/home/meyers$ sudo ln -s /home/shared_dir/file1 file1_symbollink
```
```bash
arina@ubuntu:/home/meyers$ sudo -i
root@ubuntu:~# rm /home/shared_dir/file0
root@ubuntu:~# rm /home/shared_dir/file1
root@ubuntu:~# cat /home/petersen/file0_hardlink
root@ubuntu:~# cat /home/meyers/file1_symbollink
cat: /home/meyers/file1_symbollink: No such file or directory

root@ubuntu:~# rm /home/petersen/file0_hardlink
root@ubuntu:~# rm /home/meyers/file1_symbollink
``` 
## Задание 3 - Networking 
3.1  Запустите свою виртуальную машину. Сгенерируйте новую пару SSH-ключей.
```bash
arina@ubuntu: ssh-keygen -t rsa
```
3.2. Настройте возможность аутентификации по ключам, созданным в предыдущем пункте, так чтобы вы имели возможность подключаться к вашей виртуальной машине из хост-системы без ввода пароля.
```bash
Authenticating with public key "arina@ubuntu"
    ┌──────────────────────────────────────────────────────────────────────┐
    │                 • MobaXterm Personal Edition v21.4 •                 │
    │               (SSH client, X server and network tools)               │
    │                                                                      │
    │ ➤ SSH session to arina@192.168.56.102                                │
    │   • Direct SSH      :  ✔                                             │
    │   • SSH compression :  ✔                                             │
    │   • SSH-browser     :  ✔                                             │
    │   • X11-forwarding  :  ✔  (remote display is forwarded through SSH)  │
    │                                                                      │
    │ ➤ For more info, ctrl+click on help or visit our website.            │
    └──────────────────────────────────────────────────────────────────────┘

Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-88-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sat 16 Oct 2021 10:56:34 AM UTC

  System load:  0.0                Processes:               116
  Usage of /:   36.4% of 13.71GB   Users logged in:         1
  Memory usage: 10%                IPv4 address for enp0s3: 192.168.56.102
  Swap usage:   0%                 IPv4 address for enp0s8: 10.0.3.15

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

29 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

Last login: Sat Oct 16 10:56:26 2021
arina@ubuntu:~$ 
```

3.3. Используя командные утилиты, работающие с протоколами SCP/SFTP, загрузите на свой домашний компьютер файл с виртуальной машины.
```bash
Arina.Merkulova@RU-SPB-413-05 MINGW64 /c/Program Files/PuTTY
$ pscp arina@192.168.56.102:/home/arina/test C:/Userdocuments/Study/Linux/task_data/
Server refused our key
arina@192.168.56.102's password: 1

Arina.Merkulova@RU-SPB-413-05 MINGW64 /c/Program Files/PuTTY
$ ls C:/Userdocuments/Study/Linux/task_data/
access_log  task_1_data  test
```
