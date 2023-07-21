# brutas

> Wordlists handcrafted (and automated) with ♥

A random passwords sample:

```
1qaz2wsx            | panel197111         | @bcd1234            | Root!22020
1q2w3e4r5t6y        | catalog841@@        | Zaq@#$m,.           | 1Qazxsw@222
qwerty12345         | Asdzxc129191        | testguest           | User@#$12@
password123         | qwerty!@12345       | Guest1120           | ?99998888?
123321!             | Cloud03%%           | rootj               | administrator8,4
p$ssw0rd            | abcdefghi27         | administrator/test  | test3#@121
qweqweqwe           | !1q2w3e4rt|59       | .321Root            | (ASDQWE1)
admin!              | *12shellshell12#$   | root,32020          | Qwas07
pass!               | 00!integration      | Viper               | guest3422!
98989898            | zimbra@273          | Midnight1           | zxccvbnm321
```

Requirements:
* Python 3.9, 3.10
* `hashcat`
* `hashcat-utils`
* GNU tools: `cat`, `awk`, `comm`, `sort`, `uniq`
* `wordz` (pypi)

Recommended:
* `lzop`
* `hashcat` compiled from the master branch

## Usage

### Precompiled

The precompiled lists are located at:

    brutas/wordlists/dns
    brutas/wordlists/http
    brutas/wordlists/passwords
    brutas/wordlists/ports
    brutas/wordlists/usernames

**NOTE: Due to Github limits only the "reasonably" sized lists are precompiled.** You need to run the build scripts yourself to generate the complete set (`compile.sh` and `huge.sh`).

The lists which are not included in this repository are hosted here and get updated occassionally:
- [brutas-passwords-5-l.zip](https://drive.proton.me/urls/5ESDFTKQVC#pTokh18bYyfN) [updated 2023/07/22] (67,037,681 lines - 643MB decompressed)
- [brutas-passwords-6-xl.zip](https://drive.proton.me/urls/Z586VGA1BW#k2mwYceQIJYA) [updated 2023/07/22] (331,973,905 - 3.7GB decompressed)
- [brutas-passwords-7-xxl.zip](https://drive.proton.me/urls/HP5SGW9YEC#ZfdCr6PItCyP) [updated 2022/07/30] (9,048,350,542 lines - 114GB decompressed)
- [brutas-http-paths-all.zip](https://drive.proton.me/urls/FKQVMNNQK0#uofhr9x4pDlA) [updated 2022/07/16]

#### Save bandwidth

If you want to get the latest files only ("a shallow clone with a history truncated to the specified number of commits"):

```
% git clone --depth 1 https://github.com/tasooshi/brutas.git
```

### Building

You need to install `wordz` (the wordlist automation framework) first:

```
% pip install wordz
```

The build process is automated and handled by the scripts located in the root of the project. You may want to keep the temporary files, sometimes they work pretty well on their own, so you don't have to launch the full attack. The following will produce `1-6-*.txt` passwords, as well as subdomains and basic HTTP lists:

```
~/brutas:% ./compile.sh
```

For the rest (`7-xxl.txt` and all HTTP paths) run:

```
~/brutas:% ./huge.sh -t /media/user/ExternalDrive/tmp
```

#### Custom wordlists

##### All batteries-included

If you want to generate a custom wordlist (`wordlists/passwords/custom.txt`) based on keywords in `src/keywords/custom.txt`, use the following:

```
~/brutas:% ./custom.sh -t /media/user/ExternalDrive/tmp -o /media/users/AnotherDrive/new
```

Be aware that building a custom list requires a lot of resources. If you'd like to see what kind of results you may expect, check out the example `wordlists/passwords/custom.txt` based on a single word `love` (generates over 150MB of data and 12,591,796 uniques currently, trimmed to randomly selected 10k lines). A tiny sample below:

```
---LoveLove1!1                  | 2022_|ove!23
love!5`80                       | love!5|79
55!lov607                       | 10v34444@#
Love'10#61                      | 22`Lovelove))
Loveo2020@                      | Love&01,78
love$1$64                       | ()LoveLove+^+
love9/79                        | 2021$lov3111+++
l0ve123212                      | Love+91979
|ove66612345!                   | Loveasd,.
Love^0259                       | l)v#22$#@!
```

##### Optimized for specific targets

You can also generate a custom wordlist optimized for the name of the targeted organization (put the name in `src/keywords/custom.txt`), using the following class:

```
~/brutas:% wordz -p src/classes/passwords.py::OrganizationNamePasswords
```

There's also another version of the class that works well for product names, brands etc:

```
~/brutas:% wordz -p src/classes/passwords.py::OrganizationKeywordsPasswords
```

#### Using specific language

There are two options:
1) either overwrite `lang-int-*.txt` files;
2) or use the `CustomPasswords` class with keywords copied to `src/keywords/custom.txt`.

The first one would cause the build to use the specific language as the base, while other languages would still be used (starting with `wordlists/passwords/6-xl.txt` list). The second option would ignore the normal build process and use the full set of rules on the `src/keywords/custom.txt` file. You should expect a massive output in that case.

#### Common problems

##### Kali Linux hashcat-utils

The hashcat utilities are located at `/usr/lib/hashcat-utils/`, you need to add this `$PATH` to your `.zshrc`.

##### Missing OpenCL / non-GPU setup

In case you are not going to use GPUs (`No OpenCL, HIP or CUDA compatible platform found`), you may find this one helpful:

```
# apt install pocl-opencl-icd
```

## Introduction

Why these password lists are different? The goal here is not to crack every password possible, it is to move forward inside a network. And if cracking is really needed then the bigger lists can be used. However, the assumption here is that it will be done in a reasonable time span and with limited resources (like a VM, hijacked host etc).

A brief introduction to password lists:
* the number of passwords grows with the consecutive file number;
* passwords are not sorted according to the probability, they are combined into groups of probability instead;
* each consecutive file **does not** contain passwords from any of the previous sets.

### `wordlists/passwords`

* `{1-7}-*.txt` - passwords **generated** using international keywords, hashcat rules and string partials
* `classics.txt` - typical admin passwords based on roles (test, admin), words (password, secret) or "funny" ones (like `letmein` or `trustno1`), no patterns
* `patterns.txt` - close key combinations or simple phrases (e.g. `abcd`) combined with capitalization, numbers, repetitions etc.
* `top.txt` - is a list composed of most popular user passwords found in leaks, doesn't contain close keys or any more sophisticated combinations
* `generic-1k.txt` - `1-xxs.txt` plus manually selected passwords from the other sets
* `unique.txt` - passwords which are complex enough to be used as independent passwords and are rarely mixed with any extra characters, usually related to pop-culture or sports (e.g. `apollo13`, `9inchnails`, `ronaldo7`)
* `numbers.txt` - a small list of numbers used in passwords (e.g. dates, math constants)
* `custom.txt` - put your custom keywords here and generate the wordlist using `custom.sh`, the result will be in `wordlists/passwords/custom.txt`

### Other lists

* `wordlists/dns` - a fairly reasonable list for host discovery composed of common conventions, self-hosted software etc.
* `wordlists/http/paths` - HTTP paths/params useful in fuzzing Web applications, generated with subclasses of `HttpWords` *)
* `wordlists/http/files/extensions` - file extensions useful in HTTP discovery
* `wordlists/http/files/biggquery/github` - file names that might be helpful e.g. in IIS short name enumeration, fairly cleaned up of obvious uniques, series and garbage (like MD5 hashes) to reduce file size, maximum 40 chars, a minimum of two occurrences required in case of the bigger files (unless uniques make sense, see `class.csv`), otherwise untouched
* `wordlists/ports` - personal choice of ports used both for scanning internal networks and public services, used instead of nmap's top list
* `wordlists/usernames` - most common usernames, the short, and the long version

*) Some of the pairs in these lists are duplicates or make no sense (e.g. `postsPosts` or `syndication-editor`, although you never know...) This is an expected trade-off. Considering the number of requests usually sent, this is acceptable for now.


### Recommendations

The combined lists `{1,2,3,4}-*.txt` seem to be most effective for general purpose and reasonably fast password cracking. Start with the smallest one and move forward. The lists `{1,2}-*.txt` are designed for a quick win in large networks. If you need something really minimalistic, try using `1-xxs.txt` solely - my highly opinionated view of the top 100.

However, I recommend experimenting on your own and rebuilding these sets depending on the target. You may want to incorporate your native language keywords, too. For example, file or a domain name combined with `numbers.txt` turns out to be pretty effective on encrypted archives and wireless networks. As with everything, a little social engineering comes handy to understand the local approach to the "password policy".

### Statistics

Based on leaks in two categories (social networks and technical forums), the current (2022/05/20) effectiveness is:

|                                      | No. of passwords | Social networks (~1M) | Technical forums (~450K) |
| ------------------------------------ | ---------------- | --------------------- | ------------------------ |
| brutas-passwords-1-xxs.txt (*)       |             100  |       2.16%           |          2.75%           |
| brutas-passwords-2-xs.txt (*)        |           6,549  |       3.05%           |          3.63%           |
| brutas-passwords-3-s.txt (*)         |          24,805  |       3.99%           |          4.32%           |
| brutas-passwords-4-m.txt             |         922,624  |       3.59%           |          5.05%           |
| brutas-passwords-5-l.txt             |      33,278,126  |      13.91%           |         17.10%           |
| brutas-passwords-6-xl.txt            |     162,843,765  |       6.93%           |          9.24%           |
| brutas-passwords-7-xxl.txt           |  10,051,549,134  |      26.08%           |         34.21%           |
| Suitable for online bruteforcing (*) |                  |       9.20% (99,197)  |         10.70% (48,885)  |
| To be used for offline cracking      |                  |      50.51% (544,617) |         65.64% (299,699) |
| TOTAL                                |                  |      59.71% (643,891) |         76.34% (348,757) |


So, the basic three lists (~31K passwords) provide 10% success on average with these fairly diverse and big samples. From my experience, password spraying with the top 100 is guaranteed to yield interesting results. And most often a couple accounts is enough to move forward in almost any network.

### How does it compare to `rockyou.txt`?

The famous `rockyou.txt` dictionary contains 14,344,392 passwords (at least in the Kali Linux "edition"). Against the same sets the results are:

|                                      | No. of passwords | Social networks (~1M) | Technical forums (~450K) |
| ------------------------------------ | ---------------- | --------------------- | ------------------------ |
| rockyou.txt                          |      14,344,392  |      34.99% (377384)  |         39.55% (180665)  |

It seems that with half of the passwords from the first five groups the `rockyou.txt` dictionary is much more effective. How come? Let's see what happens if we mix them:

|                                      | No. of passwords | Social networks (~1M) | Technical forums (~450K) |
| ------------------------------------ | ---------------- | --------------------- | ------------------------ |
| rockyou.txt + brutas-1-3.txt         |      14,375,845  |      44.19% (476578)  |         50.25% (229550)  |
| rockyou.txt + brutas-1-5.txt         |      48,576,595  |      61.90% (667459)  |         72.94% (333231)  |

* 44.19% (social networks) - 34.99% (rockyou) = 9.20% (= 9.20%, brutas-1-3)
* 50.25% (technical forums) - 39.55% (rockyou) = 10.70% (= 10.70%, brutas-1-3)
* 61.90% (social networks) - 34.99% (rockyou) = 26.91% (~= 26.70%, brutas-1-5)
* 72.94% (technical forums) - 39.55% (rockyou) = 33.39% (~= 32.85%, brutas-1-5)

The answer is clear: these sets are somewhat complementary, or rather `brutas` was designed with a different goal in mind than what you would find in the leaks from popular sites. For example, `rockyou.txt` is missing 23,246 passwords from the `brutas-1-3.txt` combo (which is 31,453 in total). To name just a few: `P$SSW)RD`, `Admin123!` or `!root!`. So, if you want to bruteforce or spray in a more corporate environment (i.e. with password policies in place), use `brutas`. For best results in general cracking, combine it with typical leaks. And with the bigger `brutas` lists the "predictable sophistication" grows significantly.

### BigPasswords (`7-xxl.txt`) sample

This is an extended set for typical password cracking purposes, generated by the `src/classes/passwords.py::BigPasswords` class. Those of you who feel the beauty of passwords may find the following sample of 400 random lines somewhat a pleasant picture:

```
thegrudge'356                   | 111Kamikaze__                   | Unix$05^1962                    | 3333saas123@$
Future;197106                   | Thrones7%02                     | army2211357                     | maintainer$9_2024
89letsgo,.11                    | Buster#643                      | rene997-^-                      | Christie2020!!#1984
Cecilia%%96                     | saas'031979                     | ssladmin^12|48                  | Telemark^101956
Germany^0346                    | Pooter7788.,.                   | Libertad2233123!                | 08amazon.12345
havefun1978'1                   | 111mybitch.04                   | Quser%8;91                      | keywest14@08
Sienna1953;4                    | Markus2010;11                   | Franky&197301                   | doctorwho08&1993
Cmp*1#82                        | adminweb^08%42                  | jazzy7%$                        | 45malibu09)(
foxy05;1943                     | yash$194403                     | Permit17@@                      | 999whore.05
puck-031982                     | pulpfiction!092001              | 9191vava,666                    | mammamia3*53
extra,2350                      | 112happyday!@12                 | gino236#edc                     | Conan1290@3@
hsqldb!5#2007                   | creative08111+++                | panasonic11.1984                | Clinton5432&&
sports]51                       | Roman@@@63                      | debian098@97                    | Lin2004^09
lighthouse212o                  | philip-^-1993                   | Silkroad1952/4                  | Poland%21978
Sad!231969                      | Boss/03@2023                    | taipei40|08                     | zebulon#092000
Crusader$71984                  | Evildick2005$06                 | 567Dinner!zaq                   | zaq4455123asd
Cthulhu-821                     | covid765,.555                   | 27creeper.222                   | Titans92'2
Passwort.441959                 | morales!902                     | caesar'101966                   | Destination!4308
miracle34587^                   | leonard1979&06                  | toronto5566,.22                 | gators123.1998
nebula,101974                   | Microwave_8512                  | Polycom_03-1989                 | Lauren-1967
4321Axel2021*                   | Drive;8008                      | stefano%2202                    | Superuser*091970
Octopus09_1972                  | cassandra*07#1956               | vodafone((1981                  | takeshi3#98
Janet64'10                      | 12@pfsense119                   | 123456camels123@@@              | Bobbie8902007
1Outlander03!                   | Alpine*529                      | Windows%5|2024                  | router_1,19
Dolphins333#11                  | Eric|197603                     | mazda$196212                    | Mysql|3.2002
Walter.4441972                  | guizmo'0360                     | Botnet/200505                   | hola/7605
800freebsd0!                    | Phpmyadmin,08-80                | ***Deploydeploy,.666            | wildcat59,10
Cabbage^6410                    | astra.905                       | postmaster;9'1967               | 03Nightmare+123
mag/0619                        | Pearl99909                      | Tintin1981^05                   | Cassandra#07!1983
123Cosworth$#@!                 | 5432sheep098!                   | Shell@06,83                     | Superboy$1508
Automation02^1976               | lillian.7771941                 | 09Joel07!                       | Mountain;778
90fuckher,123                   | sampson13%$                     | claudia0987q1@                  | true1985$9
rascal2020,2021                 | dba_01/72                       | Viper++1959                     | 414Michigan1234!!
Kali7%%55                       | army1966%11                     | Jiong*45615                     | Taemin1192022!!
,45CiscoCisco2;                 | 119vinny2021#                   | Tarzan123.,02                   | ram/2312
Shogun+12356                    | december#0245                   | gordon;966                      | 15cents+
Skyrim!!112004                  | toto2000$7                      | peter75%54                      | Shell&07@1969
Victor#4702                     | sameer123?1960                  | Toon7$1945                      | sacha1945123!@#
1234stimpy,.00                  | Russia92.4                      | Ricky.71998                     | 11Wish***
Fujitsu%72006                   | 65alexander6!                   | 54xanadu++                      | 2332margarita#edc
frances01%04                    | yuki,.7767                      | 34lada!!!                       | Xmen86`3
rico08,1984                     | ying5525%                       | android!*1944                   | goodtime1957^8
vickie2378956*                  | Hiphop1988$7                    | wade3+1979                      | bart2021!1953
333cousin.00                    | Wow03,1999                      | 555finger2020#                  | Nadine65?
112privatef                     | miles333.444                    | Volvic04%50                     | acc456123!!!
echo,1067                       | julius@061952                   | Wpadmin/8`71                    | Mushroom19514%
brandon198144$                  | abel.441983                     | Ppp*03^61                       | 123456cvs#
Boby.468                        | pyramid5*1989                   | prakash~!14                     | Temp%6@64
1111Armagedon.99                | Amazon2233,33                   | Spam&9'1943                     | .77CAMERACAMERAw2w
color`19566                     | First61+01                      | Qamar_91956                     | 234567Donkey@WSX
Grover@2224                     | Shakira1951!7                   | nino$19966                      | money08+2011
courage9010q2@                  | Miriam&41996                    | Noviembre/19713                 | Author*3*2014
34khaled,                       | sultan098712#$%                 | Russell5550%                    | Giants@995
%%55EximExim_12                 | crash,091997                    | Juan70%8                        | rolex*23423
doug.61976                      | Testroot-02;96                  | 99kobe.3                        | 555%Snortsnort-=
joyce9(3                        | 1mememe111!                     | 123)PROFTPDPROFTPD.,.           | hannibal8,1977
maxence246888*                  | lawyer41'04                     | Temp|01`1978                    | Customer;12;2009
Cameroon,ki81968                | Vas04,23                        | chickens2^1991                  | testroot.2$92
Eleven123qwe2007                | 876ness*22                      | kramervfr42012                  | cluster@07@2005
90Thailand*234                  | Small6]                         | rahul$051956                    | bianca6%64
Syslog!6!62                     | cream-92024                     | Openvpn_6+57                    | steam08#1982
impact2003d                     | scoobydoo/.1998                 | App-02!45                       | bottle8_1974
13beans@XSW                     | Teen121123!!!                   | Phi2!1998                       | noman$229
mypassword1948+4                | Alaska#197408                   | 369spectrum+++                  | Leila|209
Bottom810                       | Saif2/1979                      | squirrel400!@4                  | 77Mariela30#
Babygirl4|2014                  | Kill1975/8                      | %$WEBMANAGERWEBMANAGER09@       | 4444zodiac@22
Rapid.123418                    | Surf04.2006                     | Sexxxx&006                      | Elephant3217
init$04'1965                    | umbrella25@456                  | bobo04^03                       | Rooted098)(*51
54Saibaba,45                    | Fabrice1312022,                 | Trisha1963_04                   | boobies1029=321
Crusader989$#                   | Michaela12+1967                 | pepper09.57                     | .234SaltSalt,.999
0jojo5=                         | Diablo123321!!11                | orion234][                      | europa222r4r
skyline$#@!21                   | dumbass_1979                    | k8s%04,1966                     | Adsl/3_94
Debug%12/2015                   | Dreamer2012!02                  | Sparksedc43                     | maro!12341956
119Starfish<                    | Nexus6/1964                     | down1192022@                    | Talent\'94
ci#05'95                        | marines==2024                   | brazil,342013                   | 66blinderscde#
200rome.2                       | 9900hotpussy,77                 | Emo07*76                        | Lionking37098
raza2021$86                     | Webcam-10_07                    | Sadsad7777123//                 | han8888<
oracle&07`2001                  | Adminuser;555                   | 121@WWWUSERWWWUSER/.            | Proxmox*5#1942
benji07&1947                    | Mellon&19759                    | 43Sinbad,99                     | 8888boo?123
151Caprice+++                   | cheetah'101968                  | Pi&08+98                        | Saddam04`72
close42%02                      | 5555Mikrotik.333                | nestle892021@                   | polly2015#02
.098rolerole((99                | 112Katy.2021                    | ludo3333zaq!                    | marine21.02
Bobbie2345.12                   | Sharon678#23                    | rockford01&2024                 | Bloodywsx19
Celia2007;9                     | pornstar|21952                  | _10postmasterpostmaster--       | Denis06#1977
Postmaster!4;                   | Melek12!@99                     | Python1111:                     | Bimmer,331963
Syslog,04!24                    | newuser/07#70                   | deep06-54                       | Roger-196907
Lobster07^^                     | nicola05222@                    | Corn722!                        | Kira90@12
archie7\'                       | 11pixie#                        | Paintball90101,1                | arc4003#
78xavier,22                     | iNetu5erk                       | 7Janazxc                        | scans07&00
Hansen232@1990                  | Chemical=12313                  | smcadmin06,1982                 | Sparrow123$%1986
micron09-2012                   | Budlight#021974                 | ironman'1151                    | assassins!0319
ilovejesus*41958                | zenith^032017                   | Nature_195706                   | carpet^6659
Dude,061946                     | confess*231963                  | Vikings11|1986                  | Naked09_3
Netadmin.01_1978                | liquid02^1971                   | Tongue2345q1q                   | ~!itit123''
Sons,77791                      | jericho19775                    | Jenkins&07!02                   | barney1111,.555
Mystic01-4                      | pcloud.8899                     | spot'19472                      | frisco\'40
Pol04.07                        | Ripper%5906                     | slipknot2020$11                 | Lizzie56/04
rebels&&7714                    | disney.197001                   | hope10!qaz                      | audi!195102
boubou12+16                     | brady6*1991                     | Peacock098!2024                 | Upload.02-83
,666Installinstall)(            | daemon;4'1963                   | 12+BOXBOX,00                    | Jakob900~!
```