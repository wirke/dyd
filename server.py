#parameters
api_key = "yourapikey" #api.ocr.space
tty_number = '4' #tty number for fbgrab
import requests
import urllib.request
import os
from base64 import b64encode
os.system('fbgrab -c ' + tty_number + ' tty.png')
f = open('tty.png','rb')
base = b64encode(f.read())
url="https://api.ocr.space/parse/image"
data = {'apikey':api_key, 
        'base64Image':b'data:image/png;base64,'+base, 
        'language':'eng', 
        'isTable':'true'}
r = requests.post(url = url, data = data)
a = str(r.text)
x = 0
while(len(a)>x+7):
    if(a[x] == 'n'):
        if(a[x+1] == 'g'):
            if(a[x+2] == 'r'):
                if(a[x+3] == 'o'):
                    if(a[x+4] == 'k'):
                        if(a[x+5] == '.'):
                            break
    x += 1
if(a[x] == 'n'):
    if(a[x+1] == 'g'):
        if(a[x+2] == 'r'):
            if(a[x+3] == 'o'):
                if(a[x+4] == 'k'):
                    if(a[x+5] == '.'):
                        endletter=x+7
                        while(a[x] != '/'):
                            x-=1
                        startletter=x
                        addr=a[startletter+1:endletter+1]
                        print(addr)
                        req='https://ngroksync.000webhostapp.com/index.php?func=1&pass=yourpass&addr='+addr
                        response = urllib.request.urlopen(req)

else:
    print('err')
