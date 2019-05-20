#!-*- conding: utf8 -*-
import socket
import sys
import os
import requests
import OpenSSL
import ssl
import signal

info_string = \
r"""
███████╗██████╗     ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔════╝██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
███████╗██████╔╝    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║ 1.3 beta 
╚════██║██╔══██╗    ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
███████║██║  ██║    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
                              
 ALERT!!! ADMIN FINDER & CMS FINDER & DOMAIN FINDER PODE SER DEMORADOS!
 ALERT!!! DEVIDO TER UMA LONGA BIBLIOTECA!                                                                 
 Desevolvido por SrBlue.
 Publicada no 5ubTools
 Eficiencia de 80% e diversão de 100% 
"""

print(info_string)

def IpPublico(andress): 
        
        #Essa função verifica se o ip é publico ou privado.
        #IpPublico("192.168.0.1")
        #return: False
        
        if re.match(r'^(?:10)(?:\.\d+){3}|(?:172\.(?:[1]:?[0-9]|[2]:?[0-9]|[3]:?[0-1]))(?:\.\d+){2}|(?:192.168)(?:\.\d+){2}|(?:127)(?:\.\d+){3}$', andress):
            return False
        return True


        
if len(sys.argv) < 2:
        print("[?] Use: ipRecon.py [IP/URL]")
        sys.exit()

host = sys.argv[1]


try:
        ip = socket.gethostbyname(host)
except:
        print("[x] FALHA AO PEGAR HOST")
        print("[x] TENTE TIRAR O HTTPS/HTTP")
        sys.exit()


print(" ")

try:
        print("[?] HOST: %s"%host)
except:
        print("[x] HOST: ERRO")

try:
        servidor = socket.gethostbyaddr(ip)
        print("[?] SERVIDOR-DNS: %s"%(servidor[0]))
except:
        print("[x] SERVIDOR-DNS: ERRO ")

try:
        public = IpPublico(ip)
        print("[?] TIPO DE SERVIDOR: PUBLICO")
except:
        print("[x] TIPO DE SERVIDOR: PRIVADO")
       

try:
        print("[?] IP: %s"%(ip))
except:        
        print("[x] IP: ERRO ")

try:
	url = requests.get("https://" + host)
	SSL = "https://"
	print("[?] HTTPS: SIM") 
except:
	print("[?] HTTPS: NAO")
	SSL = "http://"


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	sock.connect((host,443))
	sock.settimeout(2)
	sslsock = ssl.wrap_socket(sock)
	cert_der = sslsock.getpeercert(True)
	cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, cert_der)
	print ("[?] SSL CRIPTROGRAFIA: %s"%(cert.get_signature_algorithm()))

except socket.error:
	print("[x] SSL CERTIFICADO: ERROR")



try:
	context = ssl.create_default_context()
	with socket.create_connection((host, 443)) as sock:
		with context.wrap_socket(sock, server_hostname=host) as sock:
			print("[?] SSL VERSÃO: %s"%(sock.version()))
except:
	print("[x] SSL VERSAO: ERROR")

headers = requests.get(SSL+host).headers

print("[?] Linguagem: %s "%(headers["content-type"]))
try:
	print("[?] Servidor: %s "%(headers["server"]))
except:
	print("[x] Servidor: ERROR")
############################################
def Portas_Check(host):
	print(" ")
	print("Listando as Portas: ")

	portas = [21,22,23,25,80,81,110,113,143,443,587,2525,3306,8080]
	portasdebug = 1
	portas_abertas=0
	for i in portas:
	    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    client.settimeout(1.5)
	    try:
	        response = client.connect_ex((ip, i))
	        if response == 0:
	                print("[?] PORTA: %s ABERTA"%(str(i)))
	                portas_abertas = portas_abertas + 1
	    except:
	        portasdebug = 0
	print("[?] Portas abertas: %s"%(portas_abertas))
##############################################
# CMS:
# 1 = Wordpress
# 2 = Joomla
# 3 = Mambo
# 4 = Drupal
# 5 = Magento
# 6 = Jekyll

CmsDetectar = [0,1,2,3,4,5,6] #detector de CMS by SrBlue


CmsDetectar[0] = 0
CmsDetectar[1] = 0
CmsDetectar[2] = 0
CmsDetectar[3] = 0
CmsDetectar[4] = 0
CmsDetectar[5] = 0
CmsDetectar[6] = 0


# Como adicionar um diretorio?

# url = requests.get(SSL+host+"/diretorio/")#/diretorio/ é pra botar o diretorio que o arquivo do CMS esta. 
# if url.status_code <= 207: # Se esta com pagina nao esta erro
#       CmsDetectar[1] = 1                   # CmsDetectar[CMS] = Sim ou Nao ( 1 = sim | 2 = nao)

try: #tentando a conexao com o servidor.
        url = requests.get(SSL+host+"/wp-content/")#Cms WordPress .
        if url.status_code <= 207:
                CmsDetectar[1] = 1
                

        url = requests.get(SSL+host+"/wp-admin/")#Cms WordPress .
        if url.status_code <= 207:
                CmsDetectar[1] = 1
                

        url = requests.get(SSL+host+"/wp-login.php")#Cms WordPress .
        if url.status_code <= 207:
                CmsDetectar[1] = 1
                

        url = requests.get(SSL+host+"/wp-includes")#Cms WordPress .
        if url.status_code <= 207:
                CmsDetectar[1] = 1
                

        url = requests.get(SSL+host+"/wp-config.php")#Cms WordPress .
        if url.status_code <= 207:
                CmsDetectar[1] = 1
                print("ALERT: WP-CONFIG.PHP DETECTADO!!!")
                

        ############

        url = requests.get(SSL+host+"/joomla/")#Cms Joomla .
        if url.status_code <= 207:
                CmsDetectar[2] = 1
                
                                
        url = requests.get(SSL+host+"/language/")#Cms Joomla .
        if url.status_code <= 207:
                CmsDetectar[2] = 1
                
                                
        url = requests.get(SSL+host+"/Template_preview.png/")#Cms Joomla .
        if url.status_code <= 207:
                CmsDetectar[2] = 1
                
                
        url = requests.get(SSL+host+"/template_thumbnail.png/")#Cms Joomla .
        if url.status_code <= 207:
                CmsDetectar[2] = 1
                
                        
        url = requests.get(SSL+host+"/error.php/")#Cms Joomla .
        if url.status_code <= 207:
                CmsDetectar[2] = 1
                
        ############
        ############
        url = requests.get(SSL+host+"/administrator/backups/")#Cms Mambo .
        if url.status_code <= 207:
                CmsDetectar[3] = 1
                
                
        url = requests.get(SSL+host+"/administrator/")#Cms Mambo .
        if url.status_code <= 207:
                CmsDetectar[3] = 1
                
                
                                
        url = requests.get(SSL+host+"/mambots/")#Cms Mambo .
        if url.status_code <= 207:
                CmsDetectar[3] = 1
                
        ############
        ############
                                        
        url = requests.get(SSL+host+"/sites/all/")#Cms Drupal .
        if url.status_code <= 207:
                CmsDetectar[4] = 1
                
                                                
        url = requests.get(SSL+host+"/sites/all/libraries/")#Cms Drupal .
        if url.status_code <= 207:
                CmsDetectar[4] = 1
                
                                                        
        url = requests.get(SSL+host+"/sites/all/themes/")#Cms Drupal .
        if url.status_code <= 207:
                CmsDetectar[4] = 1
                
                                                        
        url = requests.get(SSL+host+"/sites/all/modules/custom/")#Cms Drupal .
        if url.status_code <= 207:
                CmsDetectar[4] = 1
                
                                                        
        url = requests.get(SSL+host+"/site/all/modules/contrib")#Cms Drupal .
        if url.status_code <= 207:
                CmsDetectar[4] = 1
                
        ############
        ############
        url = requests.get(SSL+host+"/app/code/")#Cms Magento .
        if url.status_code <= 207:
                CmsDetectar[5] = 1
                

        url = requests.get(SSL+host+"/app/design/")#Cms Magento .
        if url.status_code <= 207:
                CmsDetectar[5] = 1
                

        url = requests.get(SSL+host+"/app/etc/")#Cms Magento .
        if url.status_code <= 207:
                CmsDetectar[5] = 1
                

        url = requests.get(SSL+host+"/downloader/")#Cms Magento .
        if url.status_code <= 207:
                CmsDetectar[5] = 1
                

        url = requests.get(SSL+host+"/app/")#Cms Magento .
        if url.status_code <= 207:
                CmsDetectar[5] = 1
                
        ############
        ############
        ############

        url = requests.get(SSL+host+"/jekyll/")#Cms Jekyll .
        if url.status_code <= 207:
                CmsDetectar[6] = 1
                

        url = requests.get(SSL+host+"/_config.yml")#Cms Jekyll .
        if url.status_code <= 207:
                CmsDetectar[6] = 1

        url = requests.get(SSL+host+"/.jekyll-metadata")#Cms Jekyll .
        if url.status_code <= 207:
                CmsDetectar[6] = 1

        url = requests.get(SSL+host+"/_layouts")#Cms Jekyll .
        if url.status_code <= 207:
                CmsDetectar[6] = 1

        url = requests.get(SSL+host+"/404.md")#Cms Jekyll .
        if url.status_code <= 207:
                CmsDetectar[6] = 1

        url = requests.get(SSL+host+"/about.md")#Cms Jekyll .
        if url.status_code <= 207: 
                CmsDetectar[6] = 1
                
                
                
except: #Se falhar a conexao com o servidor.
        print("[x] FALHA AO CONECTAR A SERVIDOR HTTP/HTPPS")
        
        

# Definição dos CMS
# IF CmsDetectar[CMS] == 1: # Se a CMS for true 
# CMS  =  " NOME DA CMS "   # retorna CMS = "nome dela"


CMS = "ERROR"

if CmsDetectar[1] == 1:   # Se CMS 1 for = 1 
        CMS = "Wordpress"
        
elif CmsDetectar[2] == 1: # or CMS 2 For = 1
        CMS = "Joomla"
        
elif CmsDetectar[3] == 1: # or CMS 3 For = 1
        CMS = "Mambo"
        
elif CmsDetectar[4] == 1: # or CMS 4 For = 1
        CMS = "Drupal"
        
elif CmsDetectar[5] == 1: # or CMS 5 For = 1
        CMS = "Magento"

elif CmsDetectar[6] == 1: # or CMS 6 For = 1
        CMS = "Jekyll"
        
        
print("[?] CMS: %s "%(CMS))
############################333




Portas_Check(host)

print(" ")
print("Listando paginas admins:")

passe = ('admin/','administrator/','login.php','administration/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp','/login.aspx',
'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','administration','pages/admin/admin-login.html','admin/admin-login.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
'admin/adminLogin.asp','home.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm','adminLogin/','admin_area/','panel-administracion/','instadmin/','login.aspx',
'memberadmin/','administratorlogin/','adm/','admin/account.aspx','admin/index.aspx','admin/login.aspx','admin/admin.aspx','admin/account.aspx',
'admin_area/admin.aspx','admin_area/login.aspx','siteadmin/login.aspx','siteadmin/index.aspx','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.aspx','bb-admin/index.aspx','bb-admin/login.aspx','bb-admin/admin.aspx','admin/home.aspx','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.aspx','admin.aspx','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.aspx','cp.aspx','administrator/index.aspx','administrator/login.aspx','nsw/admin/login.aspx','webadmin/login.aspx','admin/admin_login.aspx','admin_login.aspx',
'administrator/account.aspx','administrator.aspx','admin_area/admin.html','pages/admin/admin-login.aspx','admin/admin-login.aspx','admin-login.aspx',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.aspx','modelsearch/login.aspx','moderator.aspx','moderator/login.aspx',
'moderator/admin.aspx','acceso.aspx','account.aspx','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.aspx','admincontrol.aspx',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.aspx','adminarea/index.html','adminarea/admin.html',
'webadmin.aspx','webadmin/index.aspx','webadmin/admin.aspx','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.aspx','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.aspx','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.aspx','wp-login.aspx','adminLogin.aspx','admin/adminLogin.aspx','home.aspx','admin.aspx','adminarea/index.aspx',
'adminarea/admin.aspx','adminarea/login.aspx','panel-administracion/index.aspx','panel-administracion/admin.aspx','modelsearch/index.aspx',
'modelsearch/admin.aspx','admincontrol/login.aspx','adm/admloginuser.aspx','admloginuser.aspx','admin2.aspx','admin2/login.aspx','admin2/index.aspx','usuarios/login.aspx',
'adm/index.aspx','adm.aspx','affiliate.aspx','adm_auth.aspx','memberadmin.aspx','administratorlogin.aspx','memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',
'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi','admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf','cpanel','cpanel.php','cpanel.html',)


a = 1
achar_finder = 0
for hani in passe :
    try :
    	url = requests.get(SSL+host+"/"+hani)# 
    	url2 = SSL+host+"/"+hani
    	if url.status_code <= 207:
    		print("[?] Finder Admin: %s"%(url2))
    		achar_finder = achar_finder + 1
    	else:
    		a=a
    except:
       a = a

if achar_finder == 0:
	print("[x] Nenhuma pagina encontrada.")
else: 
	print("[?] Paginas encontradas: %s "%(achar_finder))



domain = ("www","mail","ftp","localhost","webmail","smtp","pop","ns1","webdisk","ns2","whm","autodiscover","autoconfig","m","imap",
	"test","ns","blog","pop3","dev","www2","admin","forum","news","vpn","ns3","mail2","new","mysql","old","lists","support",
	"mobile","mx","static","docs","beta","shop","sql","secure","demo","cp","calendar","wiki","web","media","email","images","img","www1",
	"intranet","portal","video","sip","dns2","api","cdn","stats","dns1","ns4","www3","dns","search","staging","server","mx1","chat","wap",
	"my","svn","mail1","sites","proxy","ads","host","crm","cms","backup","mx2","lyncdiscover","info","apps","download","remote","db",
	"forums","store","relay","files","newsletter","app","live","owa","en","start","sms","office","exchange","ipv4","mail3","help","blogs",
	"helpdesk","web1","home","library","ftp2","ntp","monitor","login","service","correo","www4","moodle","it","gateway","gw","i","stat","stage",
	"ldap","tv","ssl","web2","ns5","upload","nagios","smtp2","online","ad","survey","data","radio","extranet","test2","mssql","dns3","jobs",
	"services","panel","irc","hosting","cloud","de","gmail","s","bbs","cs","ww","mrtg","git","image","members","poczta","s1","meet","preview",
	"fr","cloudflare-resolve-to","dev2","photo","jabber","legacy","go","es","ssh","redmine","partner","vps","server1","sv","ns6","webmail2",
	"av","community","cacti","time","sftp","lib","facebook","www5","smtp1","feeds","w","games","ts","alumni","dl","s2","phpmyadmin",
	"archive","cn","tools","stream","projects","elearning","im","iphone","control","voip","test1","ws","rss","sp","wwww","vpn2","jira","list","connect",
	"gallery","billing","mailer","update","pda","game","ns0","testing","sandbox","job","events","dialin","ml","fb","videos","music","a",
	"partners","mailhost","downloads","reports","ca","router","speedtest","local","training","edu","bugs","manage","s3","status","host2",
	"ww2","marketing","conference","content","network-ip","broadcast-ip","english","catalog","msoid","mailadmin","pay","access","streaming",
	"project","t","sso","alpha","photos","staff","e","auth","v2","web5","web3","mail4","devel","post","us","images2","master","rt","ftp1","qa",
	"wp","dns4","www6","ru","student","w3","citrix","trac","doc","img2","css","mx3","adm","web4","hr","mailserver","travel","sharepoint","sport",
	"member","bb","agenda","link","server2","vod","uk","fw","promo","vip","noc","design","temp","gate","ns7","file","ms","map","cache","painel","js",
	"event","mailing","db1","c","auto","img1","vpn1","business","mirror","share","cdn2","site","maps","tickets","tracker","domains","club","images1",
	"zimbra","cvs","b2b","oa","intra","zabbix","ns8","assets","main","spam","lms","social","faq","feedback","loopback","groups","m2","cas","loghost",
	"xml","nl","research","art","munin","dev1","gis","sales","images3","report","google","idp","cisco","careers","seo","dc","lab","d","firewall","fs",
	"eng","ann","mail01","mantis","v","affiliates","webconf","track","ticket","pm","db2","b","clients","tech","erp","monitoring","cdn1","images4",
	"payment","origin","client","foto","domain","pt","pma","directory","cc","public","finance","ns11","test3","wordpress","corp","sslvpn","cal",
	"mailman","book","ip","zeus","ns10","hermes","storage","free","static1","pbx","banner","mobil","kb","mail5","direct","ipfixe","wifi",
	"development","board","ns01","st","reviews","radius","pro","atlas","links","in","oldmail","register","s4","images6","static2","id","shopping",
	"drupal","analytics","m1","images5","images7","img3","mx01","www7","redirect","sitebuilder","smtp3","adserver","net","user","forms","outlook",
	"press","vc","health","work","mb","mm","f","pgsql","jp","sports","preprod","g","p","mdm","ar","lync","market","dbadmin","barracuda","affiliate",
	"mars","users","images8","biblioteca","mc","ns12","math","ntp1","web01","software","pr","jupiter","labs","linux","sc","love","fax","php",
	"lp","tracking","thumbs","up","tw","campus","reg","digital","demo2","da","tr","otrs","web6","ns02","mailgw","education","order","piwik",
	"banners","rs","se","venus","internal","webservices","cm","whois","sync","lb","is","code","click","w2","bugzilla","virtual","origin-www","top",
	"customer","pub","hotel","openx","log","uat","cdn3","images0","cgi","posta","reseller","soft","movie","mba","n","r","developer","nms","ns9",
	"webcam","construtor","ebook","ftp3","join","dashboard","bi","wpad","admin2","agent","wm","books","joomla","hotels","ezproxy","ds","sa","katalog",
	"team","emkt","antispam","adv","mercury","flash","myadmin","sklep","newsite","law","pl","ntp2","x","srv1","mp3","archives","proxy2","ps","pic",
	"ir","orion","srv","mt","ocs","server3","meeting","v1","delta","titan","manager","subscribe","develop","wsus","oascentral","mobi","people","galleries",
	"wwwtest","backoffice","sg","repo","soporte","www8","eu","ead","students","hq","awstats","ec","security","school","corporate","podcast","vote","conf",
	"magento","mx4","webservice","tour","s5","power","correio","mon","mobilemail","weather","international","prod","account","xx","pages","pgadmin","bfn2",
	"webserver","www-test","maintenance","me","magazine","syslog","int","view","enews","ci","au","mis","dev3","pdf","mailgate","v3","ss","internet","host1",
	"smtp01","journal","wireless","opac","w1","signup","database","demo1","br","android","career","listserv","bt","spb","cam","contacts","webtest",
	"resources","1","life","mail6","transfer","app1","confluence","controlpanel","secure2","puppet","classifieds","tunet","edge","biz","host3","red",
	"newmail","mx02","sb","physics","ap","epaper","sts","proxy1","ww1","stg","sd","science","star","www9","phoenix","pluto","webdav","booking","eshop",
	"edit","panelstats","xmpp","food","cert","adfs","mail02","cat","edm","vcenter","mysql2","sun","phone","surveys","smart","system","twitter","updates",
	"webmail1","logs","sitedefender","as","cbf1","sugar","contact","vm","ipad","traffic","dm","saturn","bo","network","ac","ns13","webdev","libguides",
	"asp","tm","core","mms","abc","scripts","fm","sm","test4","nas","newsletters","rsc","cluster","learn","panelstatsmail","lb1","usa","apollo","pre",
	"terminal","l","tc","movies","sh","fms","dms","z","base","jwc","gs","kvm","bfn1","card","web02","lg","editor","metrics","feed","repository","asterisk",
	"sns","global","counter","ch","sistemas","pc","china","u","payments","ma","pics","www10","e-learning","auction","hub","sf","cbf8","forum2","ns14",
	"app2","passport","hd","talk","ex","debian","ct","rc","2012","imap4","blog2","ce","sk","relay2","green","print","geo","multimedia","iptv","backup2",
	"webapps","audio","ro","smtp4","pg","ldap2","backend","profile","oldwww","drive","bill","listas","orders","win","mag","apply","bounce","mta",
	"hp","suporte","dir","pa","sys","mx0","ems","antivirus","web8","inside","play","nic","welcome","premium","exam","sub","cz","omega","boutique",
	"pp","management","planet","ww3","orange","c1","zzb","form","ecommerce","tmp","plus","openvpn","fw1","hk","owncloud","history","clientes",
	"srv2","img4","open","registration","mp","blackboard","fc","static3","server4","s6","ecard","dspace","dns01","md","mcp","ares","spf","kms",
	"intranet2","accounts","webapp","ask","rd","www-dev","gw2","mall","bg","teste","ldap1","real","m3","wave","movil","portal2","kids","gw1",
	"ra","tienda","private","po","2013","cdn4","gps","km","ent","tt","ns21","at","athena","cbf2","webmail3","mob","matrix","ns15","send","lb2",
	"pos","2","cl","renew","admissions","am","beta2","gamma","mx5","portfolio","contest","box","mg","wwwold","neptune","mac",
	"pms","traveler","media2","studio","sw","imp","bs","alfa","cbf4","servicedesk","wmail","video2","switch","sam","sky","ee",
	"widget","reklama","msn","paris","tms","th","vega","trade","intern","ext","oldsite","learning","group","f1","ns22","ns20","demo3","bm","dom","pe",
	"annuaire","portail","graphics","iris","one","robot","ams","s7","foro","gaia","vpn3","smtp02","www11","calendario","h","ipv6","ua","mini","ims",
	"camera","test5","dragon","ariel","vdi","prueba","export","vps1","eduroam","true-ip-ga8-rtr","servicios","hg","true-ip-ork-rtr","staging2",
	"rdp","bc","cbf3","jpkc","acm","radius2","dev4","products","lt","xxx","i2","mail7","statistics","gh","fi","tp","virt-gw","bbb","golf","mysql1",
	"speed","pi","mymail","mkt","license","central","nexus","neo","mysite","imaps","sec","io","courses","ea","webftp","dk","dr","build","mailout",
	"co","cd","demos","msg","gold","j","fotos","hotspot","outbound","webinars","ids","ls","ns16","fw2","car","presse","alt","expo","wow","cv","c2",
	"s8","chem","testmail","acc","recruit","domino","db3","museum","personal","med","res","out","web7","db01","mirrors","energy","desarrollo","push",
	"sl","shell","root","thor","webmaker","black","kr","cafe","alex","pki","guide","webmakerl","mtest","t1","noticias","si","webinar","eco","mailtest",
	"ns18","mailbox","acs","space","2011","web03","listes","cf","ks","enterprise","nat","blue","faculty","ic","sas","pix","fp","vcs","cis","down","cars",
	"check","translate","dealer","s9","stock","xcb","reporting","torrent","odin","rms","hades","edi","about","moodle2","fa","v4","bd","sis","ict",
	"gestion","ms1","ag","poseidon","p1","campaign","radius1","cursos","ugc","teszt","study","bookstore","apple","dating","company","get","ie","elearn",
	"k","hera","hydra","house","europa","glpi","act","ping","adsl","moon","no","mk","cb","webshop","extra","minecraft","com","error","its","cams","biblio",
	"notes","idea","backup1","3g","windows","wms","money","be","news2","a1","center","qr","aaa","bip","netflow","neu","la","www0","img5","vm1","webadmin",
	"ubuntu","fun","zs","japan","tiger","nova","as2","audit","culture","webstats","uc","dp","voice","ebooks","buy","livechat","bwc","sirius","autos","world",
	"india","filter","jenkins","ga","et","dns5","securemail","widgets","pruebas","o","rds","konkurs","samara","dns02","oc","source","mi","tfs","ns17",
	"fashion","charge","jw","eagle","scm","canada","gr","gb","prtg","em","campaigns","fire","hrm","selfservice","ti","image2","bug","oracle","desktop",
	"vps2","ny","new2","smtps","foundation","max","smail","cabinet","crl","player","task","sentry","d1","server5","tom","sus","mail10","node1","epay",
	"ae","pegasus","loja","checksrv","ph","parking","lyncweb","catalogue","sql2","offers","webmaster","ice","flv","messenger","youth","answers","ed",
	"media1","vision","ondemand","d2","cg","cr","cw","gitlab","bk","sdc","mx10","cbf7","p2","dev6","hercules","broadcast","nursing","roundcube","mailx",
	"sap","sol","album","beauty","aws","mailers","ba","review","results","rm","cwc","artemis","logos","stu","angel","password","testweb","poll","mdev",
	"ws2","hu","nano","web10","ep","typo3","webhost","relay1","production","cards","www-old","class","webvpn","ads2","dev7","ns51","vod2","host4","www12",
	"web04","d-view","imgs","lk","img6","accounting","html","d-app","sem","d-click","blackberry","german","family","encuestas","el","ja","sim","openid",
	"3","do","t2","sr","admission","support2","uploads","bj","france","mysql3","telnet","realestate","hb","mobiletest","vmail","smetrics","callcenter",
	"mailrelay","triton","articles","tube","pop2","dl2","ws1","galaxy","pandora","aurora","gp","sympa","london","uninett-gw","kino","d-image","fox","node2",
	"msk","rp","schedule","ufa","trans","pptp","discovery","nsk","ox","course","nm","ns52","mf","inventory","sigma","telecom","formation","ib","hi",
	"front","gc","w4","wc","sig","redir","wholesale","webcon","helios","tst","upgrade","testvb","cdn5","srv3","wwwdev","meteo","video1","ns19",
	"journals","sps","shop2","mail8","malotedigital","realty","lotus","web11","express","static4","marketplace","academy","stream2","devwiki","ts2","novo",
	"lion","statistik","union","apt","m4","release","squid","recherche","myaccount","app3","webdesign","inf","managedomain","ad1","ns03","proxy3","i1",
	"sale","speedtest2","gm","xsc","f2","csg","dev10","ns23","upl","su","mbox","weblog","tourism","netmon","q","documents","xen","ts1","hosting2","admin1",
	"guest","2010","templates","nc","alfresco","stun","special","lc","vm0","ideas","subversion","i3","imail","download2","wedding","chat2","invest",
	"property","secure1","ad2","galeria","icq","s0","uranus","visio","stream1","testwww","europe","grid","advertising","az","test6","style","elections",
	"leo","pk","andromeda","planning","pje","eip","deliver","dev5","expert","dev01","antares","isp","sql1","ns31","vm2","ref","gatekeeper","ftps","ccc",
	"yahoo","best","kronos","webct","plesk","wa","mo","friends","api2","donate","delivery","cerberus","org","webcast","sipexternal","cyber","url","classic",
	"ms2","asia","deals","ts3","pf","nsa","rsync","trial","os","active","moderator","retail","nz","sv2","sv1","gemini","123","testsite","ctrl",
	"website","gandalf","arch","kiosk","mails","hn","lpse","gt","dev11","cit","dav","football","r1","d3","tj","3d","console","server6","ns24","earth",
	"pool","dealers","oma","minerva","tests","sbc","pd","ip-us","bio","yjs","magazin","dolphin","terra","eva","www-new","landing","ns30","trd-gw7","mta1",
	"voicemail","webchat","ops","atlantis","safety","um","call","awards","next","jjc","bob","ftp4","tb","webtv","spider","ns25","so","air","horizon","chinese",
	"mysql5","euro","bonus","workflow","city","cs2","show","proyectos","reservations","dev9","dev8","sip2","nn","nt","n2","dallas","www13","alerts","m5",
	"mw","dummy","thankyou","gay","s12","java","pb","kvm1","plan","gd","dev12","vk","s11","avia","park","mail0","erasmus","perm","application","silver",
	"csr","bw","server01","smtp5","al","chicago","yoda","spamfilter","sendmail","astro","arts","ace","themes","dev0","farm","apc","sjc","oasis","arc","old2",
	"mas","baby","sample","ras","mcu","film","kp","publish","emploi","server10","ocean","ia","external","hs","xb","fs1","sos","party","ft","dev13","www01",
	"kyc","webstat","tzb","mexico","template","4","server7","insight","sonic","ics","mail11","sz","re","mailin","index","atlanta","sqladmin","catalogo",
	"computer","alice","tasks","schools","cloud1","keys","bank","dream","www-a","isis","web9","chemistry","price","darwin","mail9","mysqladmin","xy",
	"conferences","ge","w5","wf","fx","vw","enquete","innovation","resource","homer","autoreply","image1","developers","bridge","collab","trinity","rb",
	"todo","ai","sametime","epsilon","etc","mx6","athletics","websrv","mh","cam1","manual","oss","eventos","publications","kz","credit","mta2","emergency",
	"s13","s10","luna","panda","il","mytest","gl","bart","cms2","dev15","dev14","vs","man","pet","dj","dns6","poker","demo4","bp","linux2","aa","af","olimp",
	"csi","ok","inter","obs","ironport","psy","webboard","stud","vod1","galileo","sophos","avatar","transport","ns32","www-b","light","st1","foros","ko","src",
	"rabota","yx","action","tesla","revistas","fsimg","ess","mu","itc","config","fe","dev17","newton","exch","product","horde","dg","tn","te","oscar","soap",
	"voyager","ruby","rock","imc","engineering","scan","magic","1c","10","news1","mailsrv","cs1","splunk","metro","creative","bmw","cctv","nb","smokeping","cart","rose","crystal","webalizer","crm2","dev16","lite","mail03","seminar","pilot","spa","dropbox","ssl2","patch","if","ht","integration","extern","we","fl","dev18","vn","dag","common","teacher","alert","jc","apache","serv","ns26","investor","nfs","datacenter","coupon","sss","bn","dw","relay3","plaza","a2","l2tp-us","sistema","ged","employment","p3","nsb","cse","knowledge","op","summer","umfrage","hzctc","install","quotes","cinema","sorry","host5","shared","taurus","eos","dsl","lm","ojs","graduate","budget","s14","nhko1111","rwhois","h1","imode","jaguar","gg","train","whatsup","dc1","buzz","dev19","vb","polladmin","twiki","builder","david","mx03","tk","ns29","cds","xyh","dvd","b2","mysql4","ifolder","backups","ab","mailhub","smtpout","test7","mysql01","compras","tsg","win2","ava","ag-hinrichs","apps2","ghost","ips","idm","depot","ovpn","newsroom","mr","www-1","iframe","paynow","fly","www02","portal1","za","bms","tokyo","white","hpc","deploy","pop3s","email2","hal","quizadmin","dcp","ipc","fast","vt","my2","documentos","web12","rus","president","espanol","zh","debug","housing","commerce","bv","promotion","rh","img01","imagenes","agency","simg","ecm","wolf","files2","bookings","kalender","kjc","quiz","turismo","ebay","csc","australia","touch","maillist","psi","db4","brand","pass","dss","fish","img7","hospital","virus","bpm","s15","hm","fileserver","photos2","cad","projetos","yp","dl1","statistiche","test01","soccer","albums","tomcat","festival","chat1","vendor","sugarcrm","wt","activesync","formacion","oslo-gw7","smc","webhosting","b1","pimg","focus","lyncdiscoverinternal","er","sage","lisa","dh","dynamic","ftp5","tg","t3","correoweb","wiki2","toyota","ns27","storm","ups","echo","cloud2","back","desk","kazan","astra","ot","gazeta","moscow","sparemx","webaccess","cam2","ng","search2","falcon","packages","eservices","platinum","libra","www-2","cj","lynx","bes","russia","message","tumblr","jy","s16","civil","server11","ccs","fhg","aff","san","discover","abs","polaris","rainbow","iso","web05","dialup","ocw","elibrary","ve","vp","french","saratov","web13","correo2","e1","ford","ui","eprints","mail-out","image3","archiv","water","ibank","adam","drm","centos","prime","pac","pan","casino","eval","mail12","mobile2","ssp","xxgk","pictures","samba","r2","testshop","ios","vid1","college","super","zenoss","cbf5","eps","diamond","idc","ats","load","nod32","err","dhcp","engine","meetings","florida","pixel","www14","graph","devphp","wlan","fusion","dev100","lv","informatica","solar","newyork","rep","economics","watch","i5","i4","cag","kvm2","fisheye","m6","gov","v5","ez","insurance","ecampus","agora","postfix","legal","ta","egroupware","ns28","loki","happy","c3","om","wcp","wcs","dis","compass","demo5","medical","rr","ds1","nuevo","vid2","test-www","pw","simcdnws","osiris","logon","toronto","postmaster","vps3","kiev","servizi","srv01","houston","smtp-out","berlin","groupware","l2","afisha","spanish","img0","clicks","homologacao","mahara","us2","ag-kopf-moertz","zp","torrents","cash","marvin","cap","martin","esx1","esx2","pmb","rest","charon","channel","brain","gz","ww5","kit","libproxy","hot","bsd","2008","madrid","smtp-in","f3","issues","customers","tag","win1","jazz","spell","mailfilter","df","livehelp","td","secure3","pad","g2","asset","amur","dotproject","victor","fund","cwa","inet","viper","stagingphp","jgdw","pulse","custom","rostov","women","epp","cancer","krasnodar","kerberos","dev-www","thor-mx960","admin3","dt","slave","srv4","gopher","sgs","anime","all","john","st2","graphite","carbon","ns33","texas","kt","smtp03","omsk","dev-chat-service","release0000","mts","aplicaciones","sea","photos3","photos1","monitor2","release-chat","avto","solutions","dl3","unix","nginx","wss","miss","staging-chat","release-chat-service","h2","paper","russian","gf","y","site2","wd","mls","printer","registrar","ff","dell","va","vl","avalon","bugtracker","offline","ppc","ppp","r25","e2","psql","releasephp","submit","backup3","tel","dns0","staging-chat-service","postfixadmin","ck","s20","sauron","econ","liste","save","perlbal-release","lan","graphics2","dev-chat","ana-dev","shadow","savvis-dev-commondata","holiday","reader","exmail","hosting1","solr","database2","name","ads1","3img","coregw1","che","mx7","aries","devwowza","np","n1","zsb","mod","technology","vod5","host6","parents","imgup-lb","portaltest","jwgl","setup","reservation","img8","enquetes","ns34","classified","mpa","leads","urchin","nav","ces","mike","casper","99","tula","photos4","microsoft","thumb","temp2","sandd-dev-commondata","sci","fs2","sac","drweb","elib","mir","asa","tool","wh","seguro","parts","tcs","teknobyen-gw2","bid","transparencia","cic","vi","www15","baza","ip118","emails","promos","pec","sit","www21","release-commondata","showcase","devphp64","d7","cache1","mailgateway","ajax","smarthost","agents","cx","s21","sq","wall","whmcs","publisher","james","staging-commondata","documentation","chef","dot","savvis-admin-commondata","aqua","contents","ak","a3","bus","vid3","data1","direct2","logo","egw","podcasts","forex","rma","forum1","p2p","biology","exp","m7","piclist","spark","youtube","sitemap","inscription","tester","friend","firma","tennis","future","rec","gifts","hyperion","communication","imap2","tftp","moe","pollux","tuanwei","pop1","mapa","photos5","praca","kiwi","scs","cricket","line","condor","w6","wb","0","fz","geobanner","vr","oas","tts","http","gift","meta","splash","media3","tf","homes","grad","uni","mds","5","mobility","cy","anunturi","ceres","sx","sj","29","altair","tim","singapore","count","msa","rw","dn","fin","sbe","iis","estadisticas","stolav-gw4","chaos","vancouver","eis","database1","neptun","openfire","find","sip1","std","rpc","leon","outgoing","gauss","notify","destiny","emc","remote2","mv","core2","nf","enroll","grace","checkrelay","oldwebmail","deal","k2","seattle","s18","toolbar","turing","allegro","s30","helpcrew","photos0","photos6","kutuphane","mark","victoria","esx3","crs","request","saprouter","oberon","script","jxjy","membership","cp1","gk","ww4","soc","site1","subs","logistics","vladimir","testbed","vo","questionnaire","da1","tax","ski","samsung","timesheet","44","time2","sia","pds","easy","logger","vhost","stblogs","dv","t4","page","ntp3","castor","philosophy","krang","migration","c5","s22","s28","disk","fitness","coop","phobos","stars","observium","profil","italy","tip","demeter","l2tp-uk","dmz","test8","testm","nas1","simon","atom","to","pomoc","ldap3","atc","shark","polycom","wwwcache","ig","descargas","skin","chat-service","siga","servidor","robin","origin-user","stc","xmail","aleph","kursk","eportfolio","ssltest","host7","ut","reserve","mn","pesquisa","mrtg2","phplist","web20","ds2","ld","s32","interface","ils","dance","dhcp2","annonces","leto","smtpauth","moto","cognos","s17","boss","region","eclipse","webmailtest","ieee","nemesis","sunrise","s34","s31","ses","ip-uk","photos7","photos8","photos9","nissan","voronezh","profiles","uptime","cod","volgograd","dominios","facilities","ssc","sat","quality","koha","mario","vidthumb","cp2","cps","imcservices","g1","esp","oslo-gw4","vcse","goto","msdnaa","sakura","mailer2","teamspeak","dc2","vc1","rs1","cdp","ttt","web14","neon","backup01","micro","bologna","buffalo","server02","itunes","ical","nemo","perpustakaan","dx","tec","swf","activate","s23","s29","safe","registry","eros","s01","by","horus","ftp01","switch1","wwwnew","eas","vod102","vod101","article","election","opt","forward","washington","smile","vestibular","data2","jade","pv","2009","tablet","miami","rides","win3","beta1","paul","default","mmm","flow","embed","comunidad","monitor1","read","m9","smtp6","thunder","pdc","svc","35","gms","websites","cie","olymp","iron","ibm","helium","app4","stats2","imagens","s35","www16","recruitment","communications","akademik","vault","contests","adwords","invoice","jx","callisto","eposta","flirt","text","s33","austin","entertainment","maint","adult","pol","mx20","xg","mailsv","smpp","vprofile","jm","repos","cmc","liberty","router1","empresas","salon","wx","turbo","67","cultura","pdns","fd","ns41","prelive","www22","gsa","sitios","key","nice","eo","eg","ef","rekrutacja","bitrix","sid","unsubscribe","rent","bravo","monit","hybrid","tz","39","ias","hirlevel","servers","server8","comp","police","first","king","s24","s25","snmp","stories","bamboo","cool","janus","stage2","saas","perseus","germany","rome","mst","mse","cbs","ri","was","eoffice","sdo","content2","testportal","hongkong","ln","testblog","matrixstats","sbs","phones","nieuwsbrief","merlin","streamer","mycp","p4","novosibirsk","c2i","revista","destek","bib","bis","videoconferencia","tender","projets","ntp0","techsupport","psc","coupons","new1","eve","infra","anket","nyc","ns50","m8","argentina","mat","r2d2","cameras","m-dev","dse","aruba-master","zeta","mysql02","ns35","volunteer","rs2","vm3","sti","checkout","core1","zero","concours","mediawiki","postoffice","gapps","host2123","irkutsk","sp2","puma","s19","srs","ssl1","s36","dnstest","controller","atrium","denver","zebra","cts","temp1","db02","scc","he","try","octopus","spaces","tutorials","kim","60","chess","supervision","hello","f4","teens","shop1","edoc","styx","wptest","e3","as1","cma","www20","tours","pluton","projekt","d6","d4","gw3","cache2","chile","chris","boston","server9","comm","maxwell","stores","mirage","s26","rails","grupos","registro","mobile1","xyz","visit","border","rugby","deportes","elite","server21","server20","freebsd","ao","ec2","pascal","oxygen","cnc","estore","test10","biotech","static5","vsp","monster","px","alaska","nss","hc","testserver","anubis","rideofthemonth","fbapps","platform","dmc","date","workspace","general","two","playground","psp","chi","ap1","comet","cdn6","pat","na","model","spec","amazon","ars","genesis","bot","barcelona","rad","aist","digilib","dsi","renewal","rcs","academic","wwws","mail04","img9","directorio","relaunch","ns36","ns37","kf","ky","rex","homepage","webtrends","cisco-capwap-controller","archivo","failover","pogoda","6","www03","sp1","oldweb","asian","ipplan","vid","ccm","charlie","bell","krasnoyarsk","server15","servicos","yum","cobalt","egov","x1","webstore","pearl","cpa","zen","guides","mega","lesbian","big5","import","cms1","imap1","sme","ivan","fk","partenaires","ns40","51","50","cdc","proto","shops","musica","web15","charlotte","sentinel","hosted","asc","sie","bilder","eye","origin-cdn","stat2","live2","blade","bar","chelyabinsk","hardware","einstein","hrd","ganymede","rhea","mediaserver","siemens","rbl","evaluation","aulavirtual","turkey","assets2","c4","resellers","ais","arena","24","oz","misc","mailgw1","pacs","dvr","ejournal","lxy","kav","ums","jeux","zakaz","argon","prof","videoconf","server23","server22","cube","panorama","care","auctions","vestnik","atmail","mailgate2","cobra","arquivos","origin-images","immo","frontend","on","dialog","quote","aps","phd","dbs","total","s50","eclass","empleo","montreal","point","maths","isa","web06","diary","spain","lithium","university","web16","camp","flower","phys","newweb","db5","mcc","medicine","horo","personel","7","s38","suppliers","step","100","sakai","dhcp1","util","iibf","blog1","apex","inv","informer","zm","zz","server19","cos","pops","ryazan","calypso","tnt","gen","office2","zoom","sex","bounces","yz","ys","bacula","pod","wcm","orel","primary","ha","cosmos","test02","sar","licensing","nebula","911","m0","michael","sms2","director","smp","fh","bestdeal","clubs","advert","cip","v6","jack","apis","diana","ns101","hqjt","pps","vvv","radar","lamp","services2","saga","medias","maya","columbus","dante","edge1","dd","ty","tl","italia","zmail","smtp11","jerry","s27","appstore","ota","diz","demo6","bz","tver","ventas","msp","img02","pizza","enter","11","15","avatars","ak-gw","stargate","envios","fit","dedicated","test9","gzc","gorod","dns8","lasvegas","deimos","bioinfo","vds","domaincp","lucky","california","csp","motor","joker","ottawa","a-dtap","woman","t-dtap","rank","assistance","citrix2","progress","servis","sphinx","medusa","nj","limesurvey","panther","zazcloud3","zazcloud2","zazcloud1","infinity","orientation","tunnel","sn","apolo","emp","wap2","maple","eol","bak","techno","crawler","apitest","keyserver","concurso","calgary","li","wise","sydney","speedtest1","peter","toto","gala","trading","dept","vpnssl","cem","xen1","query","zt","computers","adx","tango","webadvisor","server18","good","picture","spokes","proba","set","pharmacy","newsletter2","warehouse","rating","response","dexter","partnerapi","con","heart","xs","target","ast","recipes","trend","sierra-db","est","soa","lib2","recette","ekaterinburg","watchdog","loopback-host","melbourne","dcc","dcs","smg","vtiger","mailold","gsm","ris","dam","web17","elephant","ngwnameserver","yeni","auth2","samples","guru","live1","felix","des","ftp6","sw1","dns7","spirit","s47","affiliation","sup","cq","sv3","25","eden","support1","argos","ebiz","bear","ssb","ecom","demo7","foo","upload2","bl","img10","host11","bsc","la2","ehr","smtp7","oms","yellow","ecs","qt","qc","ip176-194","relay02","vnc","diablo","polls","barnaul","luke","ultra","nsc","sony","bit","h3","solo","pink","bigbrother","forest","ftpserver","qa1","music-hn","applications","challenge","publicapi","netlab","asterix","ns53","egresados","sender","alliance","minsk","warszawa","hawaii","ali","alf","leonardo","popmail","squirrel","cheetah","dsp","exchange2","jordan","lx","gonghui","str","cisco-lwapp-controller","vms","coffee","kc","kg","kv","hestia","christmas","speedy","vpn01","result","cronos","advertise","leadership","identity","ticketing","impact","watson","nat1","api1","sga","das","zy","js1","anywhere","mercurio","server12","gdocs","daily","img11","capacitacion","casa","etherpad","hz","notebook","webs","login2","shibboleth","download1","warez","ws3","newspaper","clock","restaurant","psychology","email1","trk","xk","graphs","tic","itv","dash","gate2","west","discuss","snake","aus","cpp","lambda","broker","wl","socrates","ptc","tomsk","bulletin","promotions","paypal","python","qzlx","f5","ns42","portale","da2","usuarios","muse","dictionary","branch","nature","fbe","kaluga","reporter","brazil","specials","hit","edge2","mailweb","ns04","di","ftp7","tes","breeze","secure4","egitim","proxy01","mumble","12","guardian","peru","workshop","administration","personnel","zoo","smtp10","hzcnc","dist","hawk","aim","pets","eforms","gwmail","test123","ss1","showroom","gfx","unicorn","b3","bh","node3","youraccount","webprint","maven","sdm","mx11","mysql7","relay4","zpanel","ids1","lms2","server24","cuba","kirov","ece","klm","redes","cnt","test11","test12","messages","vendors","mssqladmin","buscador","albert","www23","mic","mix","cls","izhevsk","att","nv-ad-hn","fhg3","fhg2","deti","gta","wine","obelix","utility","activity","leopard","solaris","ps3","fantasy","ap2","grants","garant","apps3","dba","s51","skynet","soho","bird","purchasing","ekb","bioinformatics","vpn4","ocsp","murmansk","host8","www17","self","mj","dining","uk2","fenix","nameserver","search1","spare","mediacenter","tyb","rap","projekty","web22","vodafone","pulsar","ects","lj","cname","maestro","dds","fred","s37","ibs","nv-img-hn","tbms","scp","redesign","ns39","hope","mps","ka","kh","frank","navi","human","pioneer","consulting","pliki","honda","hyundai","portal3","phpbb","macduff","wapmail","server16","yellowpages","bdsm","cook","madison","audi","cde","ii","payroll","xenapp","member2","kalendarz","ctx","cte","nod","wellness","hw","hl","x2","hudson","sav","nagios2","emarketing","proton","jump","isc","reset","devtest","red5","sql3","mssql2","mailer1","phil","webmasters","ring","amateur","andrew","euler","smt","prestashop","vc2","vd","vmware","repositorio","ycbf1","domreg","tac","sks","mailings","irk","adm2","sklad","vip2","iec","akamai","ev","bender","jg","jb","ns61","scheduler","wip","boards","pdb","east","cmstest","media4","globus","us1","home2","theta","bat","films","tea","s41","s42","e-mail","indian","japanese","arizona","plato","chip","agro","xuebao","lyon","dps","quake","flex","incoming","20","windowsupdate","mailgw2","igor","sexshop","server14","lista","roma","mss","korea","tutor","streams","wac","war","13","moss","dokuwiki","fis","s-dtap","teams","devblog","testy","dotnet","qs","abiturient","01","kepler","outbound1","copy","penguin","inbound","tab","sunny","svn2","tx","seminars","immobilien","epo","lady","timeline","iam","franchise","select","teen","eportal","vista","bim","rio","demo10","rewards","win4","win5","hideip-usa","treinamento","testlink","jeu","lppm","cell","metal","aphrodite","vps4","mmc","dev02","apm","timetable","mx8","ni","jxcg","calls","socialmedia","titanium","old1","ns54","mxs","front2","iss","designer","interactive","photobook","arabic","bulk","offer","bap","experience","helix","web21","surf","ovpn-us","serenity","webmail4","reading","mysql03","myportal","face","wlc","sta","stm","holidayoffer","fortune","mel","usage","ns38","firmy","stella","synergy","livestream","ayuda","brasil","humor","davinci","panama","j2","migrate","cable","sgc","zx","front1","cci","dnn","proxy4","euro2012","toolbox","apc1","winter","agriculture","geology","nimbus","electronics","tyumen","aero","perso","webconference","georgia","ctl","tempo","mypage","marc","win10","kvm3","crc","palm","construction","blast","api-test","h4","scdn","cri","demo01","present","abo","mango","bandwidth","esc","painelstats","gjs","topaz","kia","colombia","priem","children","lena","2007","smf","smb","mail33","mail30","fg","virt","rnd","prm","zcc","ns45","scholar","zip","wdc-mare","tau","healthcare","bastion","summit","parceiros","jj","jd","mail-gw","ug","savebig","stalker","www24","worldcup","bscw","ipsec","mirror1","vesta","spot","vybory","dz","gateway2","s45","s40","cpm","deneb","intl","wmv","adp","agri","tor","teddy","selfcare","mail13","sy","verify","tuan","ssd","avs","basket","router2","resume","sfx","eureka","eservice","freedom","emba","anketa","update2","drama","mysql6","smtp8","newwww","room","opros","server27","server28","biznes","an","mc2","monitoramento","nas2","qb","beast","ethics","admindev","myfiles","tas","environment","note","relay01","s02","files1","clienti","pns","orlando","uucp","information","moda","memphis","fef","seer","lyris","csm","cygnus","era","time1","realtime","tv2","win7","lpm","cleveland","beta3","kirk","deneme","socialize","violet","reklam","lotto","usedcars","bryansk","itsupport","smtpin","nw","testtest","mon1","filr","fw01","abuse","radyo","telefon","kyoto","rigel","ark","kappa","gaming","indiana","ist","amber","mstage","indigo","mumbai","smtprelay","bbtest","websvn","land","assist","nina","mcs","video3","entry","example","investors","beijing","vm01","capital","glass","backupmx","s52","wwwx","ulyanovsk","fat","ku6","dspam","cjxy","mp2","mp1","fallback","owl","click3","losangeles","move","barracuda2","lipetsk","stash","renault","area","collection","jt","comment","kultura","ins","mx04","frodo","voip2","add","snoopy","cce","ebs","gal","sep","change","devwww","mebel","afp","netstorage","shanghai","ya","nokia","eds","dl4","ctc","bts","tlc","test22","africa","sce","mail20","economia","encuesta","cpc","pic2","xa","virgin","roman","clips","cwcx","hardcore","portland","dubai","evaluacion","paste","webserver2","chat3","gi","reference","ww7","ww9","esb","lyncav","mssql3","vas","exit","venezuela","ilearn","smartrelay","groupwise","xsh","yaroslavl","conferencia","ur","nyalesund-gw","montana","odyssey","istanbul","365","sexy","virtual2","rsa","ric","portals","ews","spp","vintage","patrick","ei","rtc","archiwum","ilias","apptest","osaka","helm","sic","campusvirtual","operations","mirror2","oslo","odessa","oem","img03","document","jiuye","emerald","navigator","junior","homepages","rbs","queen","subscriptions","xenon","duke","assets1","prensa","ismart","icm","router-us","ob","dic","doctor","win12","webmin","rtr","im1","nike","mail32","b4","b5","bu","jpk","switch2","msc","stream3","standard","viking","xiaobao","iweb","joe","quest","snap","fix","server26","server25","collections","canvas","saml","testadmin","morgan","urban","symantec","webhard","ranking","client2","dns03","tsc","tss","enigma","clk","clc","see","tambov","diendan","plm","rrhh","cvsup","frog","win8","lp2","lp1","szkolenia","sunshine","sapphire","livestats","rehber","qa2","eta","lb01","stp","vps5","biblioteka","livesupport","info2","bidb","nx","ifi2-gw","gry","evo","mgmt","cosmo","myip","cisco1","industrial","ara","srv5","oslo-gw","crowd","server13","kitchen","detroit","web08","quad","shoutcast","phototheque","rts","sysadmin","owa2","comic","everest","totem","comercial","opensource","captcha","horoscope","dali","bigtits","vps01","lh","theme","proteus","gts","galerie","tds","s53","vm4","columbia","bali","ben","bee","smtp04","presentation","m10","launch","proposal","mta3","maia","manga","opal","anal","cet","z3950","timeclock","xen2","stavropol","zj","studyabroad","vic","server17","cca","gear","rdns2","busca","icon","marathon","web18","web0","kanri","raven","avon","cab","download3","snort","tempus","ns102","economie","advertiser","bcs","supplier","rdweb","hcm","coe","jss","xj","volga","proveedores","blackhole","jk","dbserver","ssi","draft","sad","thai","austria","sede","cmp","wap1","penza","webserver1","dnsseed","copyright","hydrogen","ural","devadmin","php5","ivr","spring","wg","wi","van","zhaosheng","extreme","pim","trip","tick","climate","referencement","tenders","vlad","klub","ipm","fj","stuff","vg","vv","milan","ns44","celebrity","www18","return","fbs","ken","hideip","reservas","97","ul","eris","vegas","calc","auth1","his","openerp","korean","sw2","arthur","voyeur","bbs2","static0","pear","kaliningrad","s43","s48","moodletest","ddns","30","multi","savenow","quantum","anna","qmail","coyote","amd","appserver","smtpgw","c6","krakow","colorado","zzz","111","mediakit","voip1","win11","lifestyle","taxi","bergen-gw7","sfa","mail36","demo8","itunesu","xinli","kpi","nntp","r3","extranet2","discountfinder","newserver","hqc","industry","tutorial","mysites","mx12","metric","ids2","vologda","bruno","like","andy","sims","virgo","v2-ag","www-staging","blogtest","lbtest","poznan","jam","lider","tu","test15","animation","postgresql","led","boletin","p5","ip-usa","ucc","greece","laptop","atm","dokumenty","outreach","tweets","adserv","genius","scott","hosting3","darkorbit","wind","kunden","pine","prototype","mailserver2","marina","benefits","fichiers","postgres","fan","fad","houqin","rpm","cdn7","mx9","nv","piranha","filemaker","puppetmaster","cron","draco","depo","srv02","acces","emm","varnish","retailer","prepaid","office365","shs","lucy","sandbox2","web07","birmingham","als","xerox","sandiego","bas","quebec","factory","retracker","34","ldap01","dorm","hockey","operator","mama","ant","sociology","dict","oxford","clinic","s57","s55","s54","photo2","surgut","mec","karta","visa","tmail","xmas","hobby","colo","bet","suzuki","kj","kw","app5","orenburg","biuro","council","matt","office1","gourmet","jwxt","flc","orca","merchant","mercure","port","spc","jz","jr","mom","svpn","us3","secureftp","zb","srv6","batman","holdingpattern","apc2","mature","iq","iw","idp2","can","koala","dl5","wsc","wowza","gcal","golden","cxzy","kurgan","elena","geoportal","letter","nps","esx4","titanic","mailb","hy","dns10","fs3","orient","sustainability","photography","www-cache","maria","eski","ykt","vpngw","xlzx","val","mlm","correu","connect2","sound","2006","jason","farabi","vanilla","pastebin","stlouis","mail31","energie","mailarchive","qrcode","mng","quarantine","ns43","wads","taiwan","aquarius","dan","ipam","gadget","web19","volta","s123","service2","ppa","ppm","nick","chrome","hostel","eb","asg","turizm","ped","teach","sanfrancisco","ora","tgp","prova","s64","stat1","trace","brown","hip","jsj","rg","lis","image4","dem","s46","webcache","noah","lol","hindi","hotline","mail-relay","freegift","wetter","topics","empire","spin","daniel","derecho","atendimento","discount","mambo","iota","smolensk","sarah","e-resultats","icc","mail14","saruman","22","23","cdr","geoip","mailmx","rdc","rabbit","axis","lcs","hobbit","mail35","hunter","demo9","b6","thomas","rk","linux1","starwars","caldav","webwork","match","cookie","postman","dtc","flights","prog","labor","metis","rproxy","ninja","chronos","9","erotic","recrutement","node","internacional","mitsubishi","ecc","alumnos","virginia","fiat","honors","sarg","mouse","think","s-dtap2","e-shop","object","bibliotheque","lime","xserve","svn1","404","test13","test14","athens","immobilier","les","pj","fes","dart","pwc","zinc","imss","shiva","unity","demo11","skoda","scorpion","game1","vulcan","wins","aca","comics","fisher","farmerama","or","classificados","pergamum","lupus","toys","consulta","don","cluster1","display","louisville","courriel","iws","qm","fas","psa","wallpapers","mm2","epic","newsfeed","new3","pasca","pap","nk","nd","n3","server31","webcams","steve","newtest","apps1","webdb","db6","uniform","mon2","tourisme","s58","fc2","swift","ns55","sweden","camel","sante","plasma","alexander","smtp12","ism","opera","extend","automotive","islam","building","risk","www30","lang","indonesia","emma","missouri","sv4","convert","testnet-seed","retro","dora","ly","ana","profkom","vss","bang","ozone","sophia","toy","st3","stb","s56","poster","aragorn","photo1","ns46","mes","dean","vjud","ki","kl","ren","rem","wns1","tech2","webportal","domaindnszones","voting","srm","forestdnszones","nauka","gap","cec","remont","holidays","acme","yes","myweb","nag","nam","employee","mgw","mail15","bilbo","www-prod","shortlinks","spock","www04","testforum","editorial","nat2","giving","tower","sgb","sg1","ftp8","safari","vela","98","fleet","ekonomi","rdns1","jurnal","historia","irm","cas1","case","hh","fileshare","imagine","guia","evolution","i6","krypton","dione","suche","server32","server33","yy","eda","helsinki","tls","marx","wsp","hemeroteca","donald","backup02","portugal","professional","mercedes","tsweb","aruba","mech","h5","edocs","nis","contracts","encore","gv","meteor","massmail","esx","uran","w7","wr","admintest","kid","mz","assessment","scanner","memo","gimli","evasys","stolav-gw2","picard","sms1","prince","smi","ltx","xpam","csf","esx01","vz","jiwei","host14","ns49","ns48","gs1","gs2","proof","spo","skc","pagos","srv11","iep","consult","asl","jf","ns62","works","u2","eric","experts","s63","home1","mbs","helpdesk2","belgorod","abel","sgp","sgw","d5","beer","sql01","sogo","3w","federation","mapas","filex","aol","bb2","sondage","osc","ovh","store2","assets3","reunion","explore","js2","language","www66","remoto","disney","bilet","ica","jakarta","models","mind","quran","naruto","21","cdm","ogloszenia","xyy","blogger","purchase","testapp","diy","bibliotecas","pc1","garfield","basin","seven","talent","im2","mail34","collaboration","kostroma","b7","perl","server04","rz","rj","richmond","chel","utils","testnet","dog","lodz","17","16","18","connections","mysql8","nelson","update1","mssql4","nord","toledo","cpanel2","kamera","calendrier","spanking","ah","aw","ecp","sso2","vpnserver","cdn01","reportes","mobile-test","publicidad","omni","iii","trust","l2tp","nevada","cns","eee","lincoln","cup","acceso","cherry","lex","norway","s49","firmware","other","webauth","aap","outmail","platon","inbox","goods","mia","desenvolvimento","dino","seg","mmail","song","boris","cs3","ria","demo12","thailand","ohio","o2","program","yjsc","browse","intel","insite","sysmon","voyage","prism","bkp","ddh","mailserver1","aims","hammer","cyclops","citrix1","newdev","sls","reply","access2","kaltura","dev03","chs","rhino","ape","forge","academics","pathfinder","tux","nu","geography","vidyo","serwis","illiad","kontakt","idb","puzzle","finances","arm","jim","filetransfer","workplace","porsche","file2","s119","distance","odp","ban","lightning","pochta","south","warranty","daisy","store1","success","ldap02","military","umu","admision","exchange1","db0","sonar","lu","mobiledev","nessus","vader","mcafee","vs1","term","jasper","pcs","bkd","noc2","phpadmin","s39","vera","discussion","fortuna","heritage","fetish","antispam2","m11","castle","tags","dwh","webapi","mgm","mta4","cambridge","trash","ceo","kayako","spt","sph","spm","xena","blogg","j1","win01","moa","da25","us4","mizar","inc","argo","ncc","z1","ad3","alan","mapserver","corporativo","selene","vtest","skb","woody","more","placement","nara","recursos","cast","romeo","sed","location","ik","i7","ecology","romania","opel","hep","cac","yb","belarus","poc","pmc","edt","resolver1","you","block","dwgk","nnovgorod","sca","qlikview","delhi","vps10","h6","cups","dns11","babel","mozart","xz","blogdev","fst","digi","76","emailing","sae","itm","utah","lyrics","cme","asd","pharos","pissing","vol","chat4","finaid","ww6","ww8","mail-1","mail-2","esd","victory","smtp-gw","lemon","doors","delphi","mssql1","seoul","wu","wy","bewerbung","mobileapps","george","spectrum","tv1","baltimore","peace","tcm","smu","ip1","modules","validclick","lux","facturacion","hairy","homolog","partner2","kxfzg","www29","ivanovo","kemerovo","translator","rancid","googleapps","dac","jiaowu","spi","tao","xray","ftp02","fbl","zope","mentor","gadgets","vietnam","author","agencia","as3","memberpbp","ns60","sib","env","ub","www25","ori","speech","42","symposium","titania","periodicos","notice","lic","s101","s102","s103","ebusiness","finearts","purple","async","libweb","poisk","bac","dy","gw4","lyra","anuncios","olive","dep","pravo","t5","promociones","statics","s44","validation","drc","copper","zc","ray","bosch","filer","tps","lobby","relatorio","cruise","sacramento","pers","pal","vconf","drop","hoytek-gw4","imgsrv","nitrogen","hall","halo","bulgaria","phonebook","mail17","storage1","storage2","mysql10","mine","architecture","clamav","flashchat","advance","c3po","bds","api-dev","testapi","stage1","calender","ss2","sst","chevrolet","win13","win14","sochi","admins","zephyr","denis","mail37","messagerie","switch3","vladivostok","clip","eset","femdom","rv","img04","img05","xgb","host13","host12","host10","14","8","eproc","gdi","dts","mysql9","smtpa","supernova","timeserver","server29","menu","sccm","garden","oldftp","smoke","candy","signin","tmg","q3","qh","story","members2","seguridad","input","uae","uag","mxbackup","bestbuy","ogrenci","marine","azs","tsm","tsa","referat","wp1","wp2","deutsch","bookmark","memberall","vibe","domeny","avdesk","radius3","fermi","popup","publicaciones","tranny","papercut","spss","teamcity","brian","jcc","puskom","ege","aster","csd","csa","webmail01","big","bic","flux","vm02","jokes","balancer","sipinternal","melody","economy","avl","toons","camping","oyun","tccgalleries","app01","bazar","courrier","premier","listen","html5","dave","weber","coco","mmt","mmi","mweb","ofertas","imchat","vivaldi","aldebaran","names","rps","logic","scholarships","young","santiago","simple","gip","cisco2","smith","ide","serveur","arp","srv7","host9","remote1","irc2","sh2","sql5","mq","pisces","kelly","aura","rtmp","mak","dev40","markets","doska","afiliados","pdm","ods","printers","policy","hokkaido","raf","ankiety","ankieta","ost","electro","dingo","svr","royal","web23","web24","morpheus","gas","ecuador","ovpn-uk","relax","dsc","phantom","forumtest","mcm","ll","mysql04","urano","ns1a","julia","rwxy","astrakhan","flowers","stl","standby","prod1","gcc","s59","ilahiyat","spam2","demoshop","amadeus","lexington","mail05","asp2","fca","correo1","foro2","ku","smtp05","virtual1","mazda","beacon","exodus","fido","jackson","bible","barney","ill","syzx","nac","mgr","amsterdam","ksp","mrm","cee","ced","bgp","tiny","tina","locator","performance","www05","tromso-gw4","incubator","webext","becas","da3","mx00","zf","z2","philips","oral","cyclone","ada","philadelphia","ccr","tips","unesco","yoga","mailinglist","financialaid","mailgate1","sei","nmc","activation","i0","nashville","electronica","second","gis2","server36","cargo","ym","dlc","crmtest","salt","sonicwall","inscriptions","sviluppo","kenny","opencart","wood","zsjy","hideip-uk","nov","invite","oauth","cod4","cop","cob","m-test","dns12","test03","willow","x3","faxserver","fsm","zurich","serv1","tis","ecards","lexus","libanswers","itp","edu2","ftp10","ftp12","juegos","pbx1","flora","theatre","midia","opendata","ham","zion","subaru","perpus","polit","rain","gx","g3","avasin","cptest","gcalendar","ata","linda","ogr","wk","wj","wz","messaging","antigo","websearch","var","a66","marge","sife","linkedin","greatdeal","admitere","beheer","ldaptest","avaya","dc3","wwwww","sma","ip2","arcade","karriere","volvo","mail38","wstest","corpmail","girls","underwear","procurement","prc","pubsub","counseling","onyx","nil","vh","ns47","oai","54","tornado","webspace","gsf","converter","integra","nospam","dump","newjersey","bin","crmdev","trd-gw1","service1","ies","iem","ingenieria","90","pbs","asu","rtx","tele","lenta","smtpmax","rocky","webdata","disco","40","s108","s104","s106","s107","saransk","clone","secure5","amc","horse","wendy","contenidos","ns05","devportal","jacksonville","gr-mbpc1","oldman","idaho","backup5","alexandria","de1","deb","bisexual","dns9","phoebe","banking","static7","static6","kas","hollywood","file1","filez","calvin","mdb","lyncedge","zend","ftp9","server42","ebill","c7","moodledev","mint","cdb","fuji","icinga","weekend","piranha-all","trackit","pc2","mypc","s03","wlan-switch","regina","buyersguide","wilson","demon","radio2","bf","hornet","budapest","pin","secret","server03","rl","rn","sql02","seth","xiaoban","outlet","streaming2","leader","ufo","hasp","interior","news3","mus","anzeigen","buh","lgc","jeff","sba","alabama","aiesec","arwen","juno","magma","midget","dns04","raptor","tsp","test16","spamfilter1","epg","pay2","horoscop","py","batch","betty","atenea","vdo","mim","mil","min","cla","magnolia","bcc","cso","cst","xavier","klient","libcat","testing2","collaborate","gti","pobeda","acp","encoder","xml2","mustang","give","magnet","salud","microsite","religion","poems","ps2","lineage","dos","tsunami","incest","word","prague","hamburg","monitoreo","devs","fap","shipping","demosite","intranet3","locations","eu1","ps1","vps6","phy","cdn9","666","info1","airport","nh","pregnant","server30","webcam2","webcam1","lastminute","grc","church","db9","db8","medicina","eweb","labo","uis","staging1","printserver","automail","srv8","ns56","swan","ismtp","bos","offsite","interracial","smtp15","stop","sql4","educacion","combo","cam3","s118","s116","s112","s111","magellan","bull","omicron","cactus","apogee","hamilton","libraries","prisma","sponsor","posta2","cougar","corona","systems","svm","infocenter","webtools","rental","django","uma","acesso","psych","web25","lw","consultant","chaosm-th","speedtest3","canon","ddc","c9","staffmail","wyoming","wwwb","wwwt","indus","cgs","adobe","webcalendar","kn","srv03","neuro","crawl","ssh1","interview","m12","programs","laser","meridian","testdns","imac","lead","mrc","xiaoyou","fmp","dhl","afrodita","www06","the","trends","nyx","clasificados","epayment","jl","peugeot","origin-staging","as400","org-www","mx05","rencontre","lina","via","old-www","mti","mtc","ccp","hive","callback","ari","img12","switch7","epi","karen","dna","vle","netadmin","adams","edison","cas2","pharma","ser","insider","glxy","regions","afs","robotics","samson","bouncer","ns91","extension","cyprus","bookmarks","startup","server35","cai","cae","storelocator","host20","archivio","hvac","orchid","zap","ws4","media01","memory","radon","preview2","sch","sync2","newdesign","zhuanti","ubs","pxe","deco","npm","pskov","pmo","ithelp","www19","apidev","person","score","devsite","xf","ssa","sao","samuel","simba","nowy","provisioning","gate1","dirac","howard","hao","nsw","atlantic","mie","suboffer","foreign","webgis","cpt","tpl","kiss","quark","gj","wwx","ssl-vpn","esa","hans","novel66","ida","w8","issue","mickey","seafight","nigeria","aviation","classes","merkur","ukraine","archivos","bliss","tice","s114","s110","opennms","cms3","intranet1","publinet","mooc","short","frankfurt","smm","ipa","webmeeting","mail39","pubs","fo","freemail","360","prd","prs","pr1","hms","denmark","knowledgebase","cloudfront","cim","tampa","saulcy-gw","elk","elc","elf","my1","www28","ttc","ycbf8","frontpage","testcms","da4","da5","shop3","tap","myspace","antivir","iro","hugo","franklin","49","45","s120","s121","s124","s125","vip1","remus","ns100","spacewalk","israel","theater","cmt","adimg","enq","emprego","politics","ux","ferrari","volkswagen","www27","orb","48","46","teststore","sir","charity","juniper","s60","s61","thumbnails","sushi","s109","s105","s100","ns121","secured","fonts","lewis","jura","north","milano","ind","zakupki","jgxy","testdb","de2","del","dial","server06","files3","gateway1","addons","hilfe","secondary","33","31","priv","annualreport","scores","pas","writing","analysis","remedy","marte","comet2","sofia","imtest","klm2","minnesota","tcdn","sptest","zone","strasbourg","muz","weddings","router-uk","krs","award","alba","tf2","esl","oil","26","28","olga","cdo","mailhost2","rdg","wcf","chewbacca","dip","nts","yjsh","elektro","zcgl","holding","rich","resultats","win16","lc2","mhs","grey","paiement","hss","typo","switch4","alien","bach","msi","server05","wan","dok","ontario","tot","scd","whitelabel","host06","utm","manhattan","du","smtp9","smtp0","fil","ucenter","mijn","seat","seal","dex","vma","malaysia","tools2","ax","a4","sesame","mc1","dmm","cdn02","empleos","ireland","teachers","qq","qd","02","viejo","bangalore","prestige","testdev","broadband","agk","age","mosaic","airwatch","da17","girl","birthday","ticker","extmail","barcode","sm2","jay","pumpkin","qgzx","salsa","tsi","test18","test17","parser","online2","lee","gsites","resolver2","pn","lrc","elmer","bunny","nsm","mii","nalog","ldap0","firefly","interno","c21","mailout2","demo13","tony","prep","pres","soleil","cartman","win9","win6","listserver","newwebmail","szczecin","tucson","transit","compare","pride","cfnm","stavanger-gw4","avp","avg","sanantonio","sign","admin4","regis","pss","bindmaster","weboffice","csf1","app02","prima","wikis","satellite","ads3","projeto","qam","skyline","ntp4","your","sla","slc","wallpaper","deva","devweb","minneapolis","apk","finanzas","infos","testdrive","pm2","intra2","nr","prod2","rpt","aion","sapporo","gems","grs","argus","dnsadmin","marseille","mtv","db7","bangkok","scooter","idefix","forum3","fcc","certificados","ltc","pippin","katowice","calculator","mov","illinois","iportal","pantyhose","boc","estate","host21","rob","roy","newyear","vector","ud","pov","spiceworks","sunset","ydyo","s117","s115","monkey","podpiska","shrek","liga","mad","livedata","rt1","hero","pr2","prewww","bam","tuyensinh","rdns","stockholm","testes","recovery","wydawnictwo","hertz","skyrama","exams","cake","podarki","ds3","anton","aria","mca","video4","lf","l3","mimi","projet","vs2","game2","charts","stk","michigan","lancaster","academia","mem","chart","languages","egypt","vm5","jan","volleyball","bem","logging","studenti","wns2","handjob","host01","pedro","formazione","srt","printing","yar","brest","regist","cartoon","cours","zhaopin","ftpweb","ftptest","trunk","mail21","genetics","ksm","cel","cep","universal","fmc","netacad","oud","www07","spy","advisor","squirrelmail","jh","werbung","ftp-eu","ait","lbs","vienna","legend","dodo","inb","real2","zk","fzgh","pinger","vis","sputnik","cc2","calcium","pozycjonowanie","casting","serial","crash","zenwsimport","aida","karaoke","mapy","socks","fbapp","ariane","walmart","mevlana","cadastro","nickel","paradise","ns92","welfare","tomato","lily","server34","nutrition","maine","yc","delaware","host22","edc","edd","univ","ctt","cti","provision","syllabus","new-www","wsb","bison","w01","cpan","sc2","invoices","now","conges","chrysler","racktables","pic1","hamster","esxi","maila","dima","fog","hf","planck","hkbnpatch","trailers","pm1","s221","elektra","mandarin","sun1","futbol","furniture","75","74","72","70","blocked","pma2","sai","sal","pager","ite","educ","expresso","just","diversity","zd","henry","moose","cooking","musik","simpeg","cmd","battle","bursa","pkg","mailscanner","qtss","cpi","cpk","cpd","cpe","cpr","bhs","oficina","77","gu","g4","moodle1","wwp","transfert","bruce","acct","hukuk","pustaka","commercial","maryland","kevin","maverick","2005","pip","pbx2","ima","eup","pw20024358","post2","redirector","sm1","ipb","ipo","ip4","oldforum","symphony","cib","cia","cheboksary","tmc","ifs","nestle","rs3","host15","planeta","publica","jewelry","oak","els","logserver","55","57","53","52","s219","doktoranci","vmscanus","mgate","asta","polar","webserv","srv10","srv12","isletme","s122","s126","elastix","flight","pipeline","timehost","mailstore","ash","mongo","porno","bookshop","ns63","ns64","redis","wisconsin","bnc","uz","poczta2","ipphone","oregon","www26","guatemala","profit","aut","edms","dpstar","s65","s62","ns122","stream01","ns-2","penelope","eventum","reach","amy","amp","mysql11","jjh","erp2","oes","gforge","weekly","ripe","redirects","route","backup4","docushare","media5","crazy","staff2","coral","admanager","financial","qmailadmin","enet","contatos","spravka","veranstaltungen","nantes","webdemo","karate","milk","stumail","melon","server41","cfd","bbc","rbt","crux","smtp14","gus","resolver","cu","c8","maui","wxy","sendy","upd","upc","curriculum","optimus","nfl","mfc","krd","sv5","27","supporto","mail-backup","otp","dig","dia","wellington","stocks","electra","webfiles","rape","114","win18","testcrm","partage","pub2","xfer","pack","urp","sava","cnki","harry","upload1","b8","node4","switch8","fort","msm","ms3","server07","cbt","rx","linux3","sdk","log1","redaktion","top100","eat","dod","bss","host02","qis","jet","b2c","innova","sd1","sdh","sts1","classroom","prov","qeyo","aec","chopin","greetings","keyan","blade1","lenny","vhs","hurricane","nws","mycampus","tlbr","citroen","xew","intratest","discovirtual","cws","qp","hoteles","maggie","yandex","domino2","psicologia","carl","calendars","value","psycho","sara","03","09","personals","iie","wagner","googleffffffffa5b3bed2","whale","gpweb","thumbs2","etu","daphne","lima","picasso","liferay","aaron","client1","comet1","comet4","vadim","eec","lea","spamfilter2","epc","epa","hoytek-gw","mode","gollum","band","smarty","mlib","fed","dark","refer","onlineshop","pie","biomed","nsx","nst","mib","nest","atp","massage","sharp","drakensang","calidad","demo15","lemlit","mail-old","firewall2","reg1","ceng","pentaho","label","iut","prem","iae","professor","engage","daytona","terminator","fate","listings","mks","cjy","color","beta4","2014","bmail","terms","s214","s210","s213","hiroshima","lyncaccess","qab","kuku","maxim","ramses","slx","queens","handel","kariyer","ipweb","si1d","fac","srv20","lvs","netapp","elms","membres","vps8","vps7","mmf","mma","obiwan","apl","devel2","phi","rural","cdn8","bordeaux","academico","ne","n7","dublin","server38","goblin","formosa","policies","hovedbygget-gw","dzb","gordon","fcs","s133","imperia","privacy","okna","nestor","srv9","know","otrs2","ns58","ns57","chemlab","emu","elearning2","vpn5","vpnc","prometheus","investigacion","boa","sponsors","manila","cna","hrms","mole","cnet","keyword","bme","web09","street","infoweb","s113","ukr","fzghc","mar","rt3","siac","siam","met","river","elgg","newforum","camera2","spike","tlkp","botany","rootservers","test20","remotesupport","kaspersky","miranda","sv6","stan","web26","elpaso","milton","chita","dst","aula","consultation","webmail5","pure","lo","eprint","weibo","webteam","bc1","bc2","delfin","bcp","mein","alertus","gamer","kentucky","tera","informatics","www-5","liverpool","dyn","st4","savannah","summerschool","distributor","assistenza","gals","deepolis","photon","otto","spam1","spamd","as2test","tattoo","gw01","cirrus","node01","mail07","imgx","oa2","backstage","men","mex","asp1","chico","pressroom","gutenberg","weihnachten","mezun","mp4","student2","token","kk","kx","srv04","signups","m13","polo","inventario","app6","ssh2","dbtest","amanda","sr2","101","helen","aukcje","residence","akademia","honey","ycbf2","elan","mntr","outdoor","test19","recruiter","manchester","zoomumba","mktg","spam01","125","jn","legolas","bilety","usc","tucows","polymer","sgd","jacob","tron","financeiro","italian","ssotest","engineer","js3","caiwu","b2btest","mtt","img13","democms","humanities","connecticut","xtxp","font","traf","lyncrp","proxy5","generator","link2","aide","probe","gea","gem","fw3","fwd","mapi","devapi","apc3","wikitest","yakutsk","gcdn","i8","okinawa","aquila","cluster2","static01","cedar","server37","srv13","po2","oyp","80","dls","provider","temp3","menstruation","db04","bcm","iprint","scr","sync1","dc01","riverside","butler","formations","memberold","otc","vps12","vps11","econom","trs","siteadmin","lublin","hx","who","pmp","arnold","niagara","trc","32","xi","xl","xm","xp","csf1-4","csf1-1","csf1-2","csf1-3","hospitality","harmony","sa2","volunteers","ftp15","eole","indianapolis","boletines","nowa","chimera","smsgateway","viva","portaldev","ase","howto","relais","proposals","s204","s203","s200","lottery","adi","ise","monaco","g5","alpha2","esf","path","pharm","imanager","fishing","php4","gabvirtual","wo","lwj","consumer","callpilot","kis","daum","ens","vita","65","69","ptk","pta","formula","nudist","poland","rqd","certification","trio","plone","sqlserver","hiphop","lost","webex","oslo-gw1","peach","duck","inform","smr","smk","ip3","origin-m","agate","bohr","voltaire","titus","esx02","cid","strateji","v7","baike","authors","millenium","wis","pg2","pg1","announce","59","58","56","arcgis","groupsex","designs","carlos","ns201","uruguay","kermit","momo","fizik","elvis","bshs","47","colibri","s129","actu","veeam","finder","rsvp","vortex","wroclaw","cacti2","codex","asi","ru2","oleg","viajes","blogs2","work2","enc","baku","finanse","kvm01","u1","uy","uf","bike","zenith","look","remoteaccess","orc","41","voeux","sif","turtle","publishing","mailservice","xbox","s68","gyno","lit","vino","ns-1","presence","myphp","memberlite","tehran","ami","bolsa","image5","oec","smalltits","kassa","d8","d0","gw5","cache3","vlon","autodiscovery","browser","topic","kam","gama","37","espana","tardis","mailbck","context","devshop","chase","lb02","leeds","aoc","idiomas","lyncsip","rdv","vrn","newmedia","server44","server43","wildcat","int1","nuclear","smtp13","sources","pittsburgh","rho","galeri","comet3","webform","nonnude","shitting","sacs","rector","bobcat","hill","miller","strapon","psd","dpr","dpi","mail16","voyages","eform","origin2","fresh","guangzhou","idol","item","distribution","reestr","ois","bel","cdt","flv1","m2m","stages","irbis","finland","repair","win19","win15","gfs","comunicacion","s04","akira","lc1","stary","basic","plugins","sft","imm","mx30","diffusion","tulsa","kps","nudesport","openapi","switch6","switch5","laura","vns","www-origin","w9","brad","clio","foxtrot","cbc","codereview","txt","screen","img06","asgard","stream4","log2","protocollo","magnesium","19","fukuoka","kuwait","msdn","132","host03","mailbackup","css1","antonio","sd2","sdb","crossdressers","advent","biologia","proj","honduras","metalib","webshare","blade2","planetarium","august","cpanel1","nw1","mud","milwaukee","questions","documentacion","library2","eca","dme","dmt","tmn","esales","nueva","riga","q1","qy","country","masa","marius","stuttgart","quartz","lab2","vince","sorbete","wpdemo","nlp","persona","sqmail","platforma","ns81","outsourcing","lviv","darkstar","helena","data3","vps02","lims","boron","nmail","senior","turystyka","boleto","lock","peer","eem","olivier","phenix","wpb","icare","directories","olsztyn","origen-www","sword","ironport2","minfin","pacific","edergi","bronze","p7","magazines","leave","acervo","roku","records","extras","seed","vdp","nsp","iserver","ibook","ati","dresden","plt","force","webmail02","ayniyat","phorum","framework","rid","artem","letters","erc","airwave","velocity","reg2","arte","pfsense","nhl","prev","include","pony","edmonton","webfarm","aluno","og","od","cuda","electron","av2","memories","ppp2","branding","contribute","capella","s216","s211","s212","lenovo","concursos","animals","ets","css2","hris","devdb","nats","stroy","slm","sendgrid","nobel","curie","idisk","devm","wild","access1","ryan","vps9","mordor","mm1","standards","apa","ap3","rpg","gewinnspiel","xms","eko","taipei","tur","bmt","pmi","1000","aris","rmt","gra","snies","molly","domaincontrolpanel","merak","graphic","abakan","kate","sj2","warp","fw02","puck","yamato","gif","lts","cine","starfish","s135","s137","s136","s131","s130","s132","prelive-admin","kansai","backuppc","army","mos","moo","moc","bacchus","bb1","rrd","srv0","mailscan","dynamics","pf1","giga","webclasseur","videoteca","bok","bod","monitoring2","rod","juridico","ns22266","ajuda","eedition","senat","uk1","mortgage","fedora","drivers","n4","vicon","rti","resnet","tema","beasiswa","catering","chennai","recruiting","mrtg1","ns24331","reports2","ran","ram","rai","rat","hastane","abacus","www31","media-1","sina","skywalker","door","svt","svs","pcdn","metadata","web27","crm1","iowa","maxx","cloud3","zaphod","senate","nec","mce","romulus","lr","l1","ans","nucleus","cross","mason","pbl","igra","vsa","apteka","alpda","daemon","inst","rc1","gtc","gtw","www-3","badger","observatorio","ddt","ddd","www-devel","pasteur","tdm","tdc","training2","stf","hokbygget-gw","zyz","ricoh","jocuri","jumbo","photo3","gw02","mpi","songs","gjxy","secureweb","raovat","mail06","imgn","imgm","maritime","tecnologia","vpdn","estudiantes","mpp","olympic","server50","diet","e4","ventura","opsview","rev","stats1","k4","torg","sr1","carto","stem","ent2","s134","s139","s138","wyx","livecams","survey2","ntop","faraday","devil","ilc","wintest","crypto","gallery2","ricardo","smtpmail","sell","ox-i","pdu1","zags","mira","nuke","tops","lebanon","archive2","gtm2","gtm1","ksiegarnia","mf2","matricula","xszz","mailguard","espace","sri","warren","dar","ing","mydb","zw","bmc","swiss","lettres","jsb","jane","kobe","society","mt2","img15","img14","mobileapp","marshall","extensions","immigration","proxy6","sud","bri","vermont","league","win20","w11","accreditation","portafolio","oklahoma","ldapadmin","emailadmin","kenya","i9","nirvana","anakin","mvc","ca2","yt","launchpad","parks","host25","contractor","87","btp","agile","mari","wsj","fax2","guard","preview1","plastic","bydgoszcz","vacances","ox-d","station","mag2","umail","lsc","bobo","vpproxy","zephir","ulysse","entrepreneurship","jijian","npc","zhidao","for","h7","carrier","icarus","szb","xc","scarab","mailserv","nostromo","parana","demo02","trd-gw","fsc","reverse","acacia","toad","essen","nas01","belgium","ftp11","lala","shenji","statistica","abi","arkansas","bugtrack","yoyaku","etest","errors","baze","mailboxes","hector","poze","papers","s207","s206","s202","s209","haber","isg","moodle-test","rail","dispatch","stealth","anthony","wizard","catalyst","s91","ciscoworks","elrond","area51","buildbot","bulkmail","choup","spartan","3ans","toulouse","cei","bergen-gw2","bond","consultas","billing2","eugene","mimosa","61","pagerank","lib1","pierre","planeacion","c11","pig","webclient","cincinnati","emailmarketing","alexandre","lounge","informatique","gene","datasync","l2tp-ca","ecdl","smtptest","adtest","porn","tcc","sml","appdev","uv","yxy","logistica","annunci","ghs","filemanager","tank","integracao","energia","edinburgh","molde-gsw","vu","net2","rsm","wii","pgp","plugin","elm","netstat","myo","plant","xxzx","ycbf3","hubble","api3","baseball","diane","sysaid","cead","tam","ip-ca","studentmail","irs","vpgk","jamaica","hovedbygget-gw4","s128","s127","vip3","teamwork","ns103","ppr","jasmin","solution","fortworth","asus","ek","rt2","per","saturne","saturno","frontier","en2","convention","inotes","pinky","licence","especiales","nautilus","norma","fotografia","roger","43","reno","novgorod","youtrack","universe","gls","observer","ressources","bibliotecadigital","ns120","gentoo","bingo","sfzx","ox-ui","mb2","mirror3","asso","arcturus","ishop","webpac","vesti","aragon","pci","guitar","srvc33","hostmaster","itest","battlestar-galactica","sgi","gastro","town","medya","signature","notas","ted","sws","sw3","autopromo","rapid","endpoint","ncs","informatika","snow","kredit","communities","cover","vhost1","nebraska","proxy02","c-00","pai","biyoloji","cf2","practice","bbm","airsoft","itwiki","oldblog","m01","smtp16","kurs","nomad","assets0","openhouse","springfield","chapters","xeon","czat","excalibur","dpm","smtpout2","cooper","mail18","stable","ltxc","mfs","94","fmf","aic","paygate","tf1","hydro","gds","virt2","ol","oe","garage","elara","glossary","leda","ebank","voodoo","hippo","jedi-en","crm3","adrian","inno","win17","topup","sdp","sda","longisland","sv01","sfs","sfc","pgsql2","version","delo","plesk1","h2o","oferta","ooo","defiant","msw","tutos","rf","r7","xgc","host17","s215","s217","myshop","mother","webapps2","lighthouse","stingray","lac","analyzer","oliver","dti","ecms","ap02","sds","lille","accommodation","content7","night","bash","blade3","vh2","cpanel3","fmail","coupang4","fisip","axa","aq","steel","filesender","druk","mci","opa","esn","spitfire","morton","xljk","content6","umfragen","gzw","mta01","devforum","dionysos","medios","nfs1","hp2","peixun","jimmy","socket","flame","plum","nl2","ns82","takvim","certificate","tex","relay03","lemur","landscape","sega","beagle","perth","ext2","forestry","realtor","igk","working","adidas","process","wes","citrix3","teknik","tsl","justin","e-commerce","gx1","gx2","websrv1","tristan","ecomm","box2","automation","verwaltung","suivi","w10","azure","sergio","brands","iks","etna","aladdin","p6","citi","ucs","jwjc","alesund-gw1","douglas","pwd","legion","vdc","shoptest","pila","nsd","nse","mio","sawmill","control1","cle","cl1","cyc","voucher","outside","pmail","211","tatooine","pls","ego","commons","csv","kite","host34","demo14","fr2","s81","s83","watcher","hyderabad","ezine","dogs","libcal","regi","mediasite","dennis","sng","ispconfig","ip-hk","vs01","scarlet","mg1","child","epost","ac2","atelier","img-m","zabbix2","blackbox","comunidades","tyxy","wls","cerbere","notification","icecast","millennium","ts01","oh","of","chemeng","maillog","yjsy","ndt","toolkit","regie","oita","canopus","solusvm","kalendar","obi","s218","emailer","ddn","liquid","cs01","goat","tara","traveller","jun","cpns","responsive","sl2","cnap","nevis","scorpio","wakayama","fai","srv21","boom","psm","fundacion","costarica","kmail","bogdan","mmp","communicator","xmlrpc","vital","gamezone","l2tp-hk","newman","fruit","cdn0","alpine","bmx","pigeon","name1","wombat","bluebird","rmc","primus","rpa","cmsdev","parus","netman","roadrunner","terry","mcfeely","loves","handy","sj1","tethys","serv-refi","gin","rubin","estonia","kdm","procyon","ns111","ido","ocsweb","mox","moj","webproxy","epos","silo","old3","memorial","leia","ponto","pfa","samurai","webeoc","roi","wha","whs","gizmo","arhiv","degreeworks","yoyo","vm11","nms2","sh1","folio","sandbox1","fogbugz","bmp","create","nextgen","census","kbox","silicon","cam4","dota","name2","kayit","euterpe","features","mam","cascade","ancien","microsites","deep","itadmin","listserv2","mpacc","blues","ns71","ns72","camera1","camera3","blitz","tyr","bau","comercio","gabriel","svn01","premiere","absolute","enlace","gloria","reprints","libtest","38","s71","s77","echanges","ysu1-catalyst4506e-0","elecciones","bass","compta","le","donkey","eventi","campus2","lucas","customerservice","contacto","fds","vs3","stamp","larry","barbados","dbase","admisiones","www-c","tde","training1","gender","163","narvik-gw3","sharing","appli","ibc","core3","imgf","carte","copenhagen","biochem","fanclub","accessories","joy","insomnia","robo","walker","valencia","mpr","server51","mechatronics","tile","ke","kd","kupon","head","heat","seshat","m16","104","gaz","b10","b11","ideal","www-org","seller","graham","ipod","vpn02","vacancy","slave1","nepal","mail22","host40","dhcp3","mgs","ns112","fms1","blacklist","alive","midas","quick","sequoia","driver","edukacja","elab","tomer","issuetracker","trustees","mr1","mrp","praxis","ns59","wwwftp","kansas","imap3","nicole","sven","myapps","kygl","tsgw","pronto","columbo","thc","spe","trailer","robert","nat3","nat4","blogi","j3","usb","uss","passwordreset","scratch","weblogs","epub","tales","fns","classics","h13","szukaj","adt","ad4","babylon","mssql01","windows1","remix","surat","piano","96","toro","pushmail","podarok","nt1","nt2","ntc","ccb","frost","parent","tumen","proxy7","sand","kdftp","dorado","brc","cns1","xkb","crew","crea","repro","geb","studentweb","selenium","hair","cobbler","ftpsearch","sniffer","yokohama","adm3","essai","credito","asb","iv","pabx","kor","unifi","island","national","support3","diplom","palladium","oidb","layout","login1","hex","3g66","webcal","yu","kepegawaian","host24","gerenciador","pon","rosa","88","89","84","trixbox","temp4","tlt","db03","linus","solid","gwia","tock","kvm4","york","crashplan","productos","indicadores","smtp-out-01","lst","cassini","vet","hcs","mta5","mailc","nero","h8","router-b","mississippi","ho","omail","writers","connection","zcs","pmt","vincent","gina","s222","politika","x4","videochat","secmail","x5","venice","demo03","fs4","fss","redbull","association","lds","activities","uslugi","saf","stone","infocentre","edu1","erato","suport","ftp14","nit","soma","fdc","mining","aba","opole","sitelife","pvc","pims","intrepid","mx22","paintball","cmi","clara","loisirs","aux","carnival","eroom","testwp","s205","s201","s208","katalogi","cp3","cph","tpm","cache01","reboot","transfers","hamar-gw2","scout","geplanes","eso","es1","lvs2","lvs1","red2","partnerzy","goliath","photoshop","gjc","chelsea","faust","redaccion","distributors","ssmtp","auriga","lara","66","ptm","pts","negocios","groupon","inews","explorer","github","cockpit","mlc","snail","nsrhost","ouvidoria","translation","c10","pif","pallas","perevod","pelican","csit","telephone","verdi","wwwstg","ping1","otter","arctic","cdrom","vcma","webster","staging40","regulus","sztz","brutus","strony","f6","fn","kgb","s142","s148","syndication","pri","techhelp","iklan","vcp","vc3","cio","thanhtra","webprod","bogota","rst","cmdb","public2","public1","zbx","archive1","vtc","www-uat","radios","websurvey","srvc78","azmoon","web101","zim","webdev2","webcall","gsl","dap","astronomy","zakon","bps","wallace","styles","taz","tan","fiona","timesheets","ira","olympus","studsovet","tolyatti","srv14","alma","wikidev","fukushima","ns105","haiti","ftpadmin","kraken","blog3","veterans","e5","asr","ru1","pes","pen","userweb","xchange","livecam","nfsen","patrimonio","u3","un","sanjose","keywords","persephone","crucible","inspire","megaplan","gesundheit","imgweb","sii","sin","ns70","edm2","cbi","desa","mailmems","presta","bobae","cims","media6","webhost1","fortress","spamwall","s66","customercare","libopac","administrator","emeeting","mbm","mbt","ama","lip","gest","amway","pca","pc3","gitweb","usability","img07","great","funny","animal","besyo","archer","cher","op2","dec","dakar","vserver","teo","ns2a","obits","gss","aday","host19","t8","lp3","static8","smsgw","kat","kaz","newftp","mydev","yukon","patches","uno","musique","36","vmware2","d10","d12","telefonia","mdc","droid","primo","mali","cust","nancy","ssm","olap","bars","pav","paf","handbook","motion","obit","server45","server46","server40","centre","ernie","petra","concorde","pooh","wmt","wm2","osm","cs16","politik","movie1","beeline","dimdim","cdp1","konto","finger","florence","smtp-relay","mamba","qms","optima","tableau","solarwinds","wwu","drupal7","dpt","dpa","up1","correos","windows2","rubicon","field","json","material","opus","mx-1","sodium","nfc","fld","beaver","stwww","roberto","bsmtp","banana","golestan","nightly","johnson","blogue","jszx","oid","oic","blackbird","fang","virt1","sems","fiesta","ngo","cdl","bdd","pics2","tims","flv2","ap01","wcg","ots","ott","yjszs","kemahasiswaan","ident","ssg","kilo","ichat","project1","statystyki","america","stark","apollo2","dlib","pace","mssql5","basis","utv","streaming1","sfl","s78","cloud4","skype","addon","sitetest","b9","bx","openmeetings","oob","msu","msb","bf2","bigsavings","r4","dsa","img08","godzilla","stream5","oakland","jesse","host16","eac","bsh","aplus","origin-live","save-big","cats","dmail","sergey","sd3","bulten","nba","fiber","fip","bigsave","pivot","nora","echo360","relay5","jxzy","belize","infosys","host50","080","adminmail","moodle-dev","wonder","vh1","kamery","mum","mun","apartment","travaux","wisdom","moviegalls2","moviegalls3","moviegalls1","moviegalls4","moviegalls5","archi","rfid","img22","aj","a8","documenti","apus","portuguese","host35","host37","vasco","bux","protect","rate","qw","zpush","betatest","xhtml","lgb","lab1","oskol","base2","echarge","securelab","uzem","sbl","inscripciones","module","redhat","neworleans","sirio","eyny","aton","aga","ags","studentaffairs","dnsmaster","noname","balance","hdd","chameleon","tennessee","omaha","fritz","inkubator","jas","wed","pnc","null","bangladesh","orbit","achieve","bookit","minisites","awc","hpc-oslo-gw","muzeum","gx4","jjxy","www99","apns","drmail","epm","gx3","rooms","mailgate3","providers","collector","amigos","monroe","bialystok","dop","fe1","andromede","square","raphael","aai","megatron","brahms","lookup","rejestracja","pantera","paraguay","vdr","hitech","mid","controle","ulan-ude","loadtest","shuzai","polling","ldaps","ldap4","atl","webplus","loan","ipkvm","matlab","pla","https","prospero","ebanking","sonoivu","webmail-old","hp1","srvc82","srvc87","storefront","csl","teleservices","85st","kodeks","demo17","loto","fr1","czech","s80","s82","s84","s85","s89","sql6","timer","rcc","elsa","olddev","serwer","programy","hermes2","ds01","nhs","arlington","fgc","mg2","april","lps","aspen","innovacion","acd","d11","pano","jxpt","nat-pool","gundam","edition","merkury","ftp13","ftp16","parker","obchod","verona","goofy","wahlen","oj","icdenetim","av1","md1","jee","ppp1","eic","cameron","fourier","diaspora","qa3","defender","fotki","wts","chelny","axel","asistencia","voices","kielce","textile","netherlands","exclusive","metropolis","fao","attendance","s157","s156","sip3","lyncwebconf","tuning","r1soft","ozzy","webedit","relief","apd","cms-test","grafik","flint","srvc42","srvc43","srvc48","ironmail","hannibal","shib","pti","recycling","ankara","n6","server39","publicitate","tci","amigo","minside","arquitectura","martinique","awverify","evm","dbm","cmail","iran","arsenal","ip6","jefferson","fisica","caronte","sonic2","web-dev","malta","accelerator","moses","angola","concord","centreon","ns110","ns113","ns114","extweb","tandem","modem","hls","sensor","vodka","server47","mol","talos","hobbes","ebony","appraisal","168","jin","off","eme","kursy","srvc68","srvc62","srvc63","srvc67","arhiva","abcd","pleiades","hilton","prospect","endeavor","ex1","exc","exo","patent","keeper","kunde","front3","endor","isi","stor","sp-test","ups2","god","mongoose","terminus","lobster","wtest","asterisk2","gabinetevirtual","isms","ultima","ma1","xmlfeed","brisbane","alc","scom","rtg","tarif","remax","viruswall","scribe","pdd","ctp","odn","greenfox","izmir","qk","owa1","pre-www","srvc02","srvc07","srvc08","kolkata","masters","globe","contactus","blago","dias","ogrencikonseyi","kabinet","rise","gogo","lineage2","intro","gdansk","dfs","xian","lana","hosting01","cvsweb","ipade","kdc1","sv8","sv7","svi","thebe","esupport","mobiel","2for1gift","s79","s73","s72","s75","luxembourg","ftpmini","ipsi","umc","umi","cybozu","netops","murray","test99","peanut","ipl-m","ipl-a","wish","test-admin","ani","mysql05","mobileiron","event2","perfil","fb-canvas","hentai","pbi","tomas","leasing","sharefile","guadeloupe","srvc27","srvc22","srvc23","srvc28","horoskop","bcn","bck","egloo","monica","suspended","help2","speedtest4","kantoor","greendog","panasonic","www-4","poste","ddm","comms","w3cache","tdb","certificates","official","covers","sniper","verizon","hi-tech","graal","ibk","bazaar","core4","wwwa","competitions","imgc","imgb","imga","imgt","mistral","mammoth","eniac","hardy","clustermail","vm6","rad2","employees","goose","redmine2","mp7","mp5","mpg","server52","server55","cgc","cgp","be2","kernel","alfred","venture","student1","k3","renshi","mars2","rei","m14","m19","smtp06","granite","srvc73","srvc77","elec","wbt","logan","k1","itsm","biurokarier","tree","stefan","pdu2","tjj","sotttt","sra","imperial","ent1","profi","wotan","svr1","dws","iceman","magnitogorsk","crime","viewer","renwen","video-m","lulu","mx21","hts","voltage-pp-0000","mgt","gerrit","aulas","lyj","studios","sftp2","planner","cont","sail","blink","mrs","heron","cef","cea","cer","crimson","westchester","lucifer","zombie","our","bulksms","st01","registrasi","spielwiese","buzon","chiba","bpc","bpi","spam02","120","129","zh-cn","jo","tromso-gw2","winupdate","aip","lb3","lmc","openemm","togo","sv10","sge","real1","only","aspera","vps15","z3","h10","h14","travail","adc","plataforma","miki","200","ola","ole","nieuw","ns06","nikita","nieruchomosci","ntt","ntv","mtu","mtn","mtm","mtb","cct","cco","asap","rencontres","mail250","duma","fond","ebe","ssl3","ssl4","dn2","smsgate","analog","astrahan","rews","contato","br2","br1","antalya","cns2","indy","void","win22","win24","ger","spica","dieta","apc4","homologa","hj","imaging","enlaces","webm","colombo","webdoc","allianz","deluxe","dwb","emo","gladiator","themis","garnet","jud","tede","srvc92","tenlcdn","telechargement","aloha","banco","mvs","ca1","cau","main2","yh","wwwalt","formularios","interscan","gonzo","webopac","edoas","wds","host26","host23","kariera","download4","abit","edp","81","86","85","project2","tuna","ctd","test23","wsn","version2","icms","cashier","prikol","sco","sc1","comcast","rogue","srvc97","outils","mag1","mage","printshop","senegal","fair","vps14","vps13","hcc","sovet","filip","esx5","claims","col","maild","hmp","bolivia","bugz","sfr","email3","mais","marconi","engelsiz","inicio","pmd","pmg","fanshop","s225","s227","s226","s220","bronx","dns14","dns13","srvc93","srvc98","res1","crt","dppd","tra","heimdall","xe","xq","dewey","smpt","fs5","fsp","origen","videos2","networks","localmail","73","78","bannerweb","itl","itd","edu3","static-m","fdm","mprod","nowe","gate3","atlant","routing","rogers","comments","host18","domen","smithers","cmr","imageserver","challenger","clark","northwest","aud","voip3","colossus","cp4","s06","sxy","gy","espresso","poetry","laposte","wws","wwa","alpha1","www40","www42","nono","nagasaki","pinnacle","emis","backlinks","sok","som","sou","mssql7","hukum","site4","site5","site3","iva","sprint","slim","ds10","digitalmedia","mach","studmail","kip","bgs","ura","cabal","pablo","vae","hod","butterfly","ckp","tele2","receiver","reality","panopto","awp","aikido","solomon","cmsadmin","olympics","222","boulder","stadtplan","subscription","c13","c12","sv02","niu","kansascity","record","srvc53","srvc52","srvc57","srvc58","arrow","outage","syktyvkar","proje","avis","dce","kraft","xxb","acad","firebird","vlab","sweet","arsip","ipn","ipt","ip5","uh","www-admin","fedex","srvc83","strong","fy","vertigo","hef-router","lug","points","hummer","s140","s141","s143","s144","zelda","prx","soluciones","hml","torun","ldapmaster","vf","net1","eblast","kzn","barbara","rse","domaincontrol","pgu","pgs","oa1","skidki","submitimages","testwiki","h24","srvc72","my3","enformatik","chat-service2","benz","resim","aaa2","weixin","gsc","gsb","gsd","gsk","drac","valhalla","ns202","anthropology","dal","day","lists2","traktor","harris","85cc","colaboracion","skt","ragnarok","l4d","corvus","findnsave","leela","nhce","iktisat","srv16","dchub","joshua","acta","dayton","ns104","ppl","newhampshire","nico","blog-dev","th-core","adnet","dangan","kairos","usosweb","91","carrefour","asf","linux11","bancuri","4x4","siap","serv2","srvc18","srvc17","srvc13","srvc12","srvc47","bluesky","bappeda","wuhan","uo","ue","race","holmes","metc","impulse","ngwnameserver2","warrior","nuxeo","hoth","srvc88","lama","carmen","six","temple","ydb","cbh","s69","s67","suse","ccnet","fbdev","aplicativos","s194","innov","lecture","stream02","screenshot","cumulus","bellatrix","uploader","optimum","v12","live3","clean","srvc03","rakuten","tvguide","pct","pcm","pc5","forschung","master2","matematik","pgsql1","cyan","mta6","srvc37","srvc32","srvc38","village","spor","zdrowie","aire","d9","gwmobile","opc","den","stiri","manage2","francais","unreal","bubbles","giveaway","swa","orion2","esmtp","220","testlab","t7","thot","wien","uat-online")
print(" ")

print("Listando SubDominios: ")
achar_domain = 0
for hani in domain :
    try:
    	url = requests.get(SSL+hani+"."+host)# 
    	url2 = SSL+hani+"."+host
    	if not url.status_code == 404:
    		print("[?] Domain finder: %s"%(url2))
    	else:
    		achar_domain = achar_domain + 1
    except:
       a = a

if achar_domain == 0:
	print("[x] Nenhum SubDominio encontrada.")
else: 
	print("[?] SubDominios encontrados: %s "%(achar_domain))


print(" ")
print("SubDomain detector:")
