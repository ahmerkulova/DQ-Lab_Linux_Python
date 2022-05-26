# Task 1
## Задание 1 - ls
1.1. Одной командой выведите на экран все файлы, содержащие в имени слово update, из директорий /usr/bin и /usr/sbin.
```bash
arina@ubuntu:/$ ls -la usr/bin/ usr/sbin/ | grep "update"

-rwxr-xr-x  1 root   root       14480 Jun 11  2020 dbus-update-activation-environment
-rwxr-xr-x  1 root   root       72200 Jul 23 07:14 fwupdate
-rwxr-xr-x  1 root   root        6320 Jun 25  2020 linux-update-symlinks
-rwxr-xr-x  1 root   root       72216 Apr 27 11:15 nsupdate
-rwxr-xr-x  1 root   root       55712 Mar 23  2020 update-alternatives
-rwxr-xr-x  1 root   root       59768 Mar 24  2020 update-mime-database
-rwxr-xr-x  1 root   root       26696 Jan 24  2019 xdg-user-dirs-update
-rwxr-xr-x  1 root root     20335 Jul 21  2020 pam-auth-update
-rwxr-xr-x  1 root root     43168 Apr  8 11:06 pam_extrausers_update
-rwxr-xr-x  1 root root     43160 Apr  8 11:06 unix_update
-rwxr-xr-x  1 root root      5300 Sep 22 11:46 update-ca-certificates
-rwxr-xr-x  1 root root        64 Aug 12 09:18 update-grub
lrwxrwxrwx  1 root root        11 Aug 12 09:18 update-grub2 -> update-grub
-rwxr-xr-x  1 root root       301 Mar 27  2015 update-grub-gfxpayload
-rwxr-xr-x  1 root root      1700 Oct 10  2019 update-info-dir
-rwxr-xr-x  1 root root      7419 Mar 18  2021 update-initramfs
-rwxr-xr-x  1 root root      3063 Dec 16  2020 update-locale
-rwxr-xr-x  1 root root      9402 Oct 18  2019 update-mime
-rwxr-xr-x  1 root root     35392 Dec 16  2019 update-passwd
-rwxr-xr-x  1 root root      1752 Mar 31 22:55 update-pciids
-rwxr-xr-x  1 root root     17161 Jun 21  2019 update-rc.d
```
1.2. Одной командой выведите на экран все файлы, которые расположены в дочерних каталогах /usr/share/man/manX (хранилище встроенной документации, разбитое по секциям разделов помощи - man1, man2 ...) и содержат в своем имени слово mount.
```bash
arina@ubuntu:/$ ls -R usr/share/man/man*/ | grep "mount"

fusermount.1.gz
grub-mount.1.gz
mountpoint.1.gz
systemd-mount.1.gz
systemd-umount.1.gz
systemd.automount.5.gz
systemd.mount.5.gz
mount_namespaces.7.gz
mount.8.gz
mount.fuse.8.gz
mount.lowntfs-3g.8.gz
mount.ntfs-3g.8.gz
mount.ntfs.8.gz
systemd-remount-fs.8.gz
systemd-remount-fs.service.8.gz
umount.8.gz
umount.udisks2.8.gz
```
1.3. Одной командой выведите на экран все файлы, содержащие в своем имени слово read, хранящиеся только в трех директориях: /usr/share/man/man1, /usr/share/man/man3 и /usr/share/man/man7.
```bash
arina@ubuntu:/$ ls -lah usr/share/man/man{1,3,7} | grep "read"

-rw-r--r--  1 root root 6.6K Sep  9 11:42 git-read-tree.1.gz
-rw-r--r--  1 root root 1012 Sep  5  2019 readlink.1.gz
-rw-r--r--  1 root root 7.5K Feb 25  2020 history.3readline.gz
-rw-r--r--  1 root root 1.2K Nov  3  2019 readdir.3am.gz
-rw-r--r--  1 root root 1.2K Nov  3  2019 readfile.3am.gz
-rw-r--r--  1 root root  15K Feb 25  2020 readline.3readline.gz
-rw-r--r--  1 root root 1016 May 28 17:27 readproc.3.gz
-rw-r--r--  1 root root  847 May 28 17:27 readproctab.3.gz
-rw-r--r--  1 root root 7.3K Feb  9  2020 pthreads.7.gz
-rw-r--r--  1 root root 1.1K Feb  9  2020 thread-keyring.7.gz
```
## Задание 2 - find
2.1. Изучите утилиту find, предназначенную для поиска файлов по заданным критериям. С помощью find найдите в /usr/share/man все файлы, содержащие в своем названии слово change.
```bash
arina@ubuntu:/$ find /usr/share/man -type f -name "*change*"

/usr/share/man/man1/git-whatchanged.1.gz
/usr/share/man/man8/pvchange.8.gz
/usr/share/man/man8/vgchange.8.gz
/usr/share/man/man8/lvchange.8.gz
```
 
2.2. С помощью find найдите в /usr/share/man все файлы, имя которых начинается с time.
```bash
arina@ubuntu:/$ find /usr/share/man -type f -name "time*"

/usr/share/man/man5/time.conf.5.gz
/usr/share/man/man5/timesyncd.conf.5.gz
/usr/share/man/man1/timeout.1.gz
/usr/share/man/man1/time.1.gz
/usr/share/man/man1/timedatectl.1.gz
/usr/share/man/man7/time.7.gz
/usr/share/man/man3/time.3am.gz
```
2.3. С помощью find найдите все скрытые файлы по пути, начинающемся с /etc/cron.
```bash
arina@ubuntu:/$ find /etc/cron* -type f -name ".*"

/etc/cron.d/.placeholder
/etc/cron.daily/.placeholder
/etc/cron.hourly/.placeholder
/etc/cron.monthly/.placeholder
/etc/cron.weekly/.placeholder
```
2.4. Какие ещё действия можно выполнять с найденными файлами (не способ поиска, а действия, применяемые к результатам поиска), используя find? Приведите любой пример с комментарием.
Есть целый ряд действий, которые можно произвести с результатами поиска (actions в мануале к команде). Например, удалить, переместить найденное, вывести список с результатами, записать имена/пути в файл и т.п.
```bash
arina@ubuntu:~/testdir$ find . -type f -ok mv '{}' ~/ \;

< mv ... ./test > ? y
arina@ubuntu:~/testdir$ cd ~
arina@ubuntu:~$ tree -R
.
├── test
└── testdir

1 directory, 1 file
```
Например, в данном случае мы ищем все файлы в текущей папке (testdir/) и перемещаем их в домашнюю директорию. Команда находит файл test, спрашивает разрешение (тк мы используем -ok, -exec делает то же без разрешения) и перемещает файл в home/arina.
 
## Задание 3 - head&tail
3.1. Изучите утилиты head и tail, предназначенные для вывода первых и последних строк указанных файлов соответственно. Выведите на экран первые шесть строк файла /etc/apt/sources.list. 
```bash
arina@ubuntu:/$ head /etc/apt/sources.list -n 6

# See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to
# newer versions of the distribution.
deb http://ru.archive.ubuntu.com/ubuntu focal main restricted
# deb-src http://ru.archive.ubuntu.com/ubuntu focal main restricted

## Major bug fix updates produced after the final release of the
```
Выведите на экран последние две строки файла /etc/fstab.
```bash
arina@ubuntu:/$ tail /etc/fstab --lines=2

/dev/disk/by-uuid/aa78beb8-afe3-4ab2-b89a-4ed7720dce69 /boot ext4 defaults 0 1
/swap.img       none    swap    sw      0       0
```
3.2. Что произойдёт, если мы попытаемся запросить вывести больше строк, чем есть в файле? Попробуйте выполнить это на примере с помощью команды wc для файла /etc/apt/apt.conf.d/70debconf.
Команда выведет максимально возможное количество строк ( то есть все, в файле из задания 3 строки)
```bash
arina@ubuntu:/$ wc /etc/apt/apt.conf.d/70debconf -l
3 /etc/apt/apt.conf.d/70debconf
arina@ubuntu:/$ head /etc/apt/apt.conf.d/70debconf --lines=100
// Pre-configure all packages with debconf before they are installed.
// If you don't like it, comment it out.
DPkg::Pre-Install-Pkgs {"/usr/sbin/dpkg-preconfigure --apt || true";};
```
## Задание 4 - cd
4.1. Находясь в вашей домашней директории, перейдите в каталог /opt. Перечислите как можно больше различных вариантов, с помощью которых вы сможете вернуться обратно в ваш домашний каталог. Разными вариантами также будут считаться различные относительные пути.
```bash
arina@ubuntu:/opt$ cd ~
arina@ubuntu:/opt$ cd ~arina/
arina@ubuntu:/opt$ cd
arina@ubuntu:/opt$ cd $HOME
arina@ubuntu:/opt$ cd /home/arina
arina@ubuntu:/opt$ cd ../home/arina
```
## Задание 5 - mv
5.1. В вашем домашнем каталоге создайте директорию task5 и поместите в неё следующие файлы: chapter1.txt, chapter2.txt, chapter3.txt и chapter4.txt. Используя {}, выполните следующие переименования файлов, находясь в домашней директории:
```bash
arina@ubuntu:~/task5$ find -name 'chapter*' -delete
arina@ubuntu:~/task5$ touch chapter{1..4}.txt
arina@ubuntu:~/task5$ tree -R
.
├── chapter1.txt
├── chapter2.txt
├── chapter3.txt
└── chapter4.txt

0 directories, 4 files

arina@ubuntu:~/task5$ mv -v {chapter1.txt,chapter1.md} && mv -v {chapter2.txt,chapter2} && mv -v {chapter3.txt,testfile3.txt} && mv -v {chapter4.txt,file.log}
renamed 'chapter1.txt' -> 'chapter1.md'
renamed 'chapter2.txt' -> 'chapter2'
renamed 'chapter3.txt' -> 'testfile3.txt'
renamed 'chapter4.txt' -> 'file.log'
arina@ubuntu:~/task5$ tree -R
.
├── chapter1.md
├── chapter2
├── file.log
└── testfile3.txt

0 directories, 4 files
```
