# Task 2
## Задание 1 - RegExps
1.1. Скопируйте текстовый файл task_1_data на свою виртуальную машину. Это можно сделать, например, с использованием протокола SCP - https://ru.wikipedia.org/wiki/SCP

```bash
C:\Users\Arina.Merkulova> 
scp C:/Userdocuments/Study/Linux/task_data/task_1_data arina@192.168.56.102:/home/arina/task_data
arina@192.168.56.102's password:
task_1_data   100%   31KB  10.2MB/s   00:00
```
С использованием grep из файла task1 выведите на экран только целые слова (т.е. вывод только результатов поиска, а не всего содержимого файла с подсвеченными найденными результатами), содержащие 5 и более символов и состоящие только из букв верхнего регистра.

```bash
arina@ubuntu:~/task_data$ grep -Po '[A-Z]{5}[A-Z]{0,}' task_1_data
WVWKZ
DAHVM
PSCYR
VAUSS
OYZBV
BJYEH
BREEWH
ZUOFY
RNXOL
SYCWU
PCAYBM
JKMRFT
ZBEDQ
XIRLPD
LKSNL
ZDAFMV
PNDIB
WGKUF
CZOMNHK
BDDHA
WBULW
NMHOX
RDSJQ
EYXPS
NNRNFWNB
ROUBHYH
UQYKO
GBDFC
GYEYB
YIDEU
KWRANS
TOLNG
PPEQH
QEXLVTW
CLWYSO
XUHJB
BIEUQQ
GEFIP
LCWTGSG
UHKGV
QRRYB
LAEVFS
VYLZG
GMXAUS
QTSVWJCQJ
PEGLI
UEUKH
BDKPHG
VFAICW
WBPLB
FGISJ
DMYSEB
GKIBV
BCHRK
OOAOM
MNJSX
ZTJRK
WTCOY
VXCMZ
MPEANH
DUASU
UWOOO
HFMQOC
XGXAS
AMAVQI
DUHCZ
PRGWT
XIULU
YFEWYII
LVEDWY
EUVWE
OVMGGD
DDFIL
KSKDL
RDTEO
JXLOB
```
1.2. Создайте на своей виртуальной машине текстовый файл следующего содержания:
Moscow
Saint-Petersburg
Novosibirsk
Yekaterinburg
Nizhny Novgorod
Kazan
Chelyabinsk
Omsk
Samara
Rostov-on-Don
Ufa
Krasnoyarsk
Perm
Voronezh
Volgograd

```bash
arina@ubuntu:~/task_data$ touch cities
arina@ubuntu:~/task_data$ cat >> cities
Moscow
Saint-Petersburg
Novosibirsk
Yekaterinburg
Nizhny Novgorod
Kazan
Chelyabinsk
Omsk
Samara
Rostov-on-Don
Ufa
Krasnoyarsk
Perm
Voronezh
Volgograd
```
Выведите на экран только те города, в названии которых нет буквы a.

```bash
arina@ubuntu:~/task_data$ grep -v 'a' cities
Moscow
Novosibirsk
Nizhny Novgorod
Omsk
Rostov-on-Don
Perm
Voronezh
```
## Задание 2 - AWK
Скопируйте файл access_log на вашу виртуальную машину - ваш датасет для заданий 2 и 3. Это пример лога веб-сервера, в который записываются все обращения к сайту. Формат этого файла следующий: IP - - [DATE] "method query protocol" answer-code answer-weight-in-bytes "from-where-did-user-came" "user agent"

```bash
C:\Users\Arina.Merkulova>scp C:/Userdocuments/Study/Linux/task_data/access_log arina@192.168.56.102:/home/arina/task_data
arina@192.168.56.102's password:
access_log  100% 5980KB  53.2MB/s   00:00
```
2.1. Выведите на экран наиболее часто встречающийся user agent (браузер) и число его вхождений в логе.
Пример вывода: 248 Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.9.168 Version/11.51 (здесь: 248 - число вхождений, остальная строка - содержимое поля user agent).

```bash
arina@ubuntu:~/task_data$ cat access_log | awk -F '"' '{if (count[$6]++ >= max) max=count[$6]} END {for (n in count) if(max == count[n]) print count[n], n}'
9787 Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)
```
## Задание 3 - sed

3.1. При выводе на экран замаскируйте все IP-адреса фразой "IP address" для всех запросов со смартфона Nexus 5X.

!NB: чтобы не копировать весь вывод всего файла, скопировала небольшую часть из середины, по которой видно, что все сработало. Аналогично для следующего задания

```bash
arina@ubuntu:~/task_data$ sed -r '/'Nexus'/s/([0-9]{1,3}\.){3}[0-9]{1,3}'/'IP address'/ access_log

37.9.113.153 - - [21/Feb/2018:10:44:12 +0300] "GET / HTTP/1.1" 200 6 "-" "Mozilla/5.0 (compatible; YandexMetrika/2.0; +http://yandex.com/bots yabs01)"
IP address - - [21/Feb/2018:10:49:42 +0300] "GET / HTTP/1.1" 200 6 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
5.164.210.236 - - [21/Feb/2018:10:51:07 +0300] "GET / HTTP/1.0" 200 6 "http://example.ru/" "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0"
5.164.210.236 - - [21/Feb/2018:10:51:07 +0300] "GET / HTTP/1.0" 200 6 "http://example.ru/" "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0"
91.200.12.185 - - [21/Feb/2018:11:18:24 +0300] "GET / HTTP/1.0" 200 6 "http://example.ru/" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
91.200.12.185 - - [21/Feb/2018:11:18:24 +0300] "GET / HTTP/1.0" 200 6 "http://example.ru/" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
94.180.3.63 - - [21/Feb/2018:13:11:17 +0300] "GET / HTTP/1.0" 200 6 "http://example.ru/" "Mozilla/5.0 (Windows NT 10.1; rv:37.0) Gecko/20100101 Firefox/37.0"
94.180.3.63 - - [21/Feb/2018:13:11:17 +0300] "GET / HTTP/1.0" 200 6 "http://example.ru/" "Mozilla/5.0 (Windows NT 10.1; rv:37.0) Gecko/20100101 Firefox/37.0"
37.9.113.153 - - [21/Feb/2018:13:40:20 +0300] "GET / HTTP/1.1" 200 6 "-" "Mozilla/5.0 (compatible; YandexMetrika/2.0; +http://yandex.com/bots yabs01)"
66.249.64.21 - - [21/Feb/2018:13:47:09 +0300] "GET / HTTP/1.1" 200 6 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.64.89 - - [21/Feb/2018:14:02:28 +0300] "GET / HTTP/1.1" 200 6 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
IP address - - [21/Feb/2018:15:04:50 +0300] "GET / HTTP/1.1" 200 6 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
IP address - - [21/Feb/2018:15:29:02 +0300] "GET / HTTP/1.1" 200 6 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
37.9.113.153 - - [21/Feb/2018:16:25:48 +0300] "GET / HTTP/1.1" 200 6 "-" "Mozilla/5.0 (compatible; YandexMetrika/2.0; +http://yandex.com/bots yabs01)"
46.161.9.50 - - [21/Feb/2018:16:46:51 +0300] "GET / HTTP/1.0" 200 6 "http://example.ru/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
46.161.9.50 - - [21/Feb/2018:16:47:02 +0300] "GET / HTTP/1.0" 200 6 "http://example.ru/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
```
3.2. Замените все наименования user agent на "EPAM" с перезаписью файла access_log

```bash
arina@ubuntu:~/task_data$ awk -F '"' '{OFS=FS}{$6="EPAM";print}' access_log > access_log2
arina@ubuntu:~/task_data$ cat access_log2
91.250.15.69 - - [19/Oct/2017:20:46:00 +0300] "GET / HTTP/1.0" 200 6 "-" "EPAM"
91.250.15.69 - - [19/Oct/2017:20:46:01 +0300] "GET / HTTP/1.0" 200 6 "-" "EPAM"
91.250.15.69 - - [19/Oct/2017:20:46:01 +0300] "GET /http:/ HTTP/1.0" 404 281 "-" "EPAM"
95.108.129.196 - - [19/Oct/2017:20:47:37 +0300] "GET / HTTP/1.1" 200 6 "-" "EPAM"
46.161.9.55 - - [19/Oct/2017:20:52:52 +0300] "GET / HTTP/1.0" 200 6 "http://example.ru/" "EPAM"
46.161.9.55 - - [19/Oct/2017:20:52:52 +0300] "GET / HTTP/1.0" 200 6 "http://example.ru/" "EPAM"
37.9.118.28 - - [19/Oct/2017:21:36:52 +0300] "GET / HTTP/1.1" 200 6 "-" "EPAM"
66.249.66.75 - - [19/Oct/2017:22:30:47 +0300] "GET /?C=D;O=A HTTP/1.1" 200 6 "-" "EPAM"
66.249.66.76 - - [19/Oct/2017:22:30:48 +0300] "GET /?C=D;O=A HTTP/1.1" 200 6 "-" "EPAM"
93.72.51.208 - - [19/Oct/2017:23:57:26 +0300] "GET / HTTP/1.0" 200 6 "http://example.ru/" "EPAM"
93.72.51.208 - - [19/Oct/2017:23:57:26 +0300] "GET / HTTP/1.0" 200 6 "http://example.ru/" "EPAM"
193.169.52.154 - - [20/Oct/2017:00:53:30 +0300] "GET / HTTP/1.1" 304 0 "-" "EPAM"
67.215.230.90 - - [20/Oct/2017:01:01:58 +0300] "HEAD / HTTP/1.1" 200 0 "http://uptime-alpha.net/example.ru" "EPAM"
67.215.230.85 - - [20/Oct/2017:01:01:59 +0300] "GET / HTTP/1.1" 200 6 "-" "EPAM"
178.154.224.71 - - [20/Oct/2017:01:19:19 +0300] "GET / HTTP/1.1" 200 6 "-" "EPAM"
40.77.167.101 - - [20/Oct/2017:02:07:59 +0300] "GET / HTTP/1.1" 200 6 "-" "EPAM"
46.161.9.55 - - [20/Oct/2017:02:52:38 +0300] "GET / HTTP/1.0" 200 6 "http://example.ru/" "EPAM"
46.161.9.55 - - [20/Oct/2017:02:52:39 +0300] "GET / HTTP/1.0" 200 6 "http://example.ru/" "EPAM"
95.108.129.196 - - [20/Oct/2017:02:54:09 +0300] "GET / HTTP/1.1" 200 6 "-" "EPAM"
```
