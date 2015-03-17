import requests
from ctypes import windll

def popup(msg,title="",timeout=0):
	windll.user32.MessageBoxTimeoutA(None,msg,title,0,0,timeout)

#print '-'*31+"\n- Auto logging into ResNet... -\n"+'-'*31
url = 'http://securelogin.net.cuhk.edu.hk/cgi-bin/login'
pwd='12341234'
data = {'user' : 's1155000123' , 'password' : pwd , 'cmd' : 'authenticate' , 'Login' : 'Log+In'}
try:
	r = requests.post(url, data, allow_redirects=False)
except Exception,e:
	popup(str(e),title="!!! Exception occurred !!!")

if 'Welcome' in r.text:
    popup("Login Successful!",timeout=2000)
else:
    popup("Login Failed!\nResponse Code: "+str(r.status_code))
    #print s
    #raw_input()
