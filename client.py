import requests
from ast import literal_eval


def send_text_scan(text):
    r = requests.post("http://127.0.0.1:21987/upload",json={"type" : "text", "content" : f"{text}"})
    print(r.text)


def send_file(file_path):
    files = {'files': open(file_path,'rb')}
    r = requests.post("http://127.0.0.1:21987/upload", files = files)
    print(r.text)


def send_keystrokes(text):
    r = requests.post("http://127.0.0.1:21987/upload",json={"type" : "keystrokes", "content" : {"text" : f"{text}"}})
    print(r.text)

def send_barcode(text):
    r = requests.post("http://127.0.0.1:21987/upload",json={"type" : "isbn", "content" : f"{text}"})
    print(r.text)


def send_wifi(ssid, encryption, key):
    r = requests.post("http://127.0.0.1:21987/upload",json={"type" : "wifi", "content" : {"ssid" : f"{ssid}", "encryption" : f"{encryption}", "key" : f"{key}"}})
    print(r.text) 


def send_email(dest_addr,subject,content):
    r = requests.post("http://127.0.0.1:21987/upload",json={"type" : "email", "content" : {"address" : f"{dest_addr}", "subject" : f"{subject}", "content" : f"{content}"}})
    print(r.text) 

def send_url(url):
    r = requests.post("http://127.0.0.1:21987/upload",json={"type" : "url", "content" : f"{url}"})
    print(r.text) 

#send_email("unrealsoft.dev@gmail.com","test","test of email body")
#send_barcode("test")
#send_file("static/qr.jpeg")
#send_text_scan("test of text scan")
#send_wifi("This_is_a_wifi_name","wpa","password")
#send_url("https://www.google.com")
