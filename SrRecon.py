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
   ██████  ██▀███        ██▀███  ▓█████ ▄████▄  ▒█████   ███▄    █ 
 ▒██    ▒ ▓██ ▒ ██▒     ▓██ ▒ ██▒▓█   ▀▒██▀ ▀█ ▒██▒  ██▒ ██ ▀█   █ 
 ░ ▓██▄   ▓██ ░▄█ ▒     ▓██ ░▄█ ▒▒███  ▒▓█    ▄▒██░  ██▒▓██  ▀█ ██▒ 1.2 BETA
   ▒   ██▒▒██▀▀█▄       ▒██▀▀█▄  ▒▓█  ▄▒▓▓▄ ▄██▒██   ██░▓██▒  ▐▌██▒
 ▒██████▒▒░██▓ ▒██▒     ░██▓ ▒██▒░▒████▒ ▓███▀ ░ ████▓▒░▒██░   ▓██░
 ▒ ▒▓▒ ▒ ░░ ▒▓ ░▒▓░     ░ ▒▓ ░▒▓░░░ ▒░ ░ ░▒ ▒  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
 ░ ░▒  ░ ░  ░▒ ░ ▒░       ░▒ ░ ▒░ ░ ░  ░ ░  ▒    ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░  ░  ░    ░░   ░        ░░   ░    ░  ░       ░ ░ ░ ▒     ░   ░ ░ 
       ░     ░             ░        ░  ░ ░         ░ ░           ░ 
                                      ░                                                          
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
        print(" [?] Use: ipRecon.py [IP/URL]")
        sys.exit()

host = sys.argv[1]
try:
        ip = socket.gethostbyname(host)
except:
        print(" [x] FALHA AO PEGAR HOST")
        print(" [x] TENTE TIRAR O HTTPS/HTTP")
        sys.exit()


print(" ")

try:
        print(" [?] HOST: %s"%host)
except:
        print(" [x] HOST: ERRO")

try:
        servidor = socket.gethostbyaddr(ip)
        print(" [?] SERVIDOR-DNS: %s"%(servidor[0]))
except:
        print(" [x] SERVIDOR-DNS: ERRO ")

try:
        public = IpPublico(ip)
        print(" [?] TIPO DE SERVIDOR: PUBLICO")
except:
        print(" [x] TIPO DE SERVIDOR: PRIVADO")
       

try:
        print(" [?] IP: %s"%(ip))
except:        
        print(" [x] IP: ERRO ")

try:
	url = requests.get("https://" + host)
	SSL = "https://"
	print(" [?] HTTPS: SIM") 
except:
	print(" [?] HTTPS: NAO")
	SSL = "http://"


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	sock.connect((host,443))
	sock.settimeout(2)
	sslsock = ssl.wrap_socket(sock)
	cert_der = sslsock.getpeercert(True)
	cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, cert_der)
	print (" [?] SSL CRIPTROGRAFIA: %s"%(cert.get_signature_algorithm()))

except socket.error:
	print(" [x] SSL CERTIFICADO: ERROR")



try:
	context = ssl.create_default_context()
	with socket.create_connection((host, 443)) as sock:
		with context.wrap_socket(sock, server_hostname=host) as sock:
			print(" [?] SSL VERSÃO: %s"%(sock.version()))
except:
	print(" [x] SSL VERSAO: ERROR")

headers = requests.get(SSL+host).headers

print(" [?] Linguagem: %s "%(headers["content-type"]))
try:
	print(" [?] Servidor: %s "%(headers["server"]))
except:
	print(" [x] Servidor: ERROR")

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

# url = requests.get(SSL+host+"/diretorio/") #/diretorio/ é pra botar o diretorio que o arquivo do CMS esta. 
# if url.status_code == 200 or not url.status_code >= 305: # Se esta com pagina nao esta erro
#       CmsDetectar[1] = 1                   # CmsDetectar[CMS] = Sim ou Nao ( 1 = sim | 2 = nao)

try: #tentando a conexao com o servidor.
        url = requests.get(SSL+host+"/wp-content/") #Cms WordPress .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[1] = 1
                

        url = requests.get(SSL+host+"/wp-admin/") #Cms WordPress .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[1] = 1
                

        url = requests.get(SSL+host+"/wp-login.php") #Cms WordPress .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[1] = 1
                

        url = requests.get(SSL+host+"/wp-includes") #Cms WordPress .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[1] = 1
                

        url = requests.get(SSL+host+"/wp-config.php") #Cms WordPress .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[1] = 1
                print("ALERT: WP-CONFIG.PHP DETECTADO!!!")
                

        ############

        url = requests.get(SSL+host+"/joomla/") #Cms Joomla .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[2] = 1
                
                                
        url = requests.get(SSL+host+"/language/") #Cms Joomla .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[2] = 1
                
                                
        url = requests.get(SSL+host+"/Template_preview.png/") #Cms Joomla .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[2] = 1
                
                
        url = requests.get(SSL+host+"/template_thumbnail.png/") #Cms Joomla .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[2] = 1
                
                        
        url = requests.get(SSL+host+"/error.php/") #Cms Joomla .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[2] = 1
                
        ############
        ############
        url = requests.get(SSL+host+"/administrator/backups/") #Cms Mambo .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[3] = 1
                
                
        url = requests.get(SSL+host+"/administrator/") #Cms Mambo .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[3] = 1
                
                
                                
        url = requests.get(SSL+host+"/mambots/") #Cms Mambo .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[3] = 1
                
        ############
        ############
                                        
        url = requests.get(SSL+host+"/sites/all/") #Cms Drupal .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[4] = 1
                
                                                
        url = requests.get(SSL+host+"/sites/all/libraries/") #Cms Drupal .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[4] = 1
                
                                                        
        url = requests.get(SSL+host+"/sites/all/themes/") #Cms Drupal .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[4] = 1
                
                                                        
        url = requests.get(SSL+host+"/sites/all/modules/custom/") #Cms Drupal .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[4] = 1
                
                                                        
        url = requests.get(SSL+host+"/site/all/modules/contrib") #Cms Drupal .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[4] = 1
                
        ############
        ############
        url = requests.get(SSL+host+"/app/code/") #Cms Magento .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[5] = 1
                

        url = requests.get(SSL+host+"/app/design/") #Cms Magento .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[5] = 1
                

        url = requests.get(SSL+host+"/app/etc/") #Cms Magento .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[5] = 1
                

        url = requests.get(SSL+host+"/downloader/") #Cms Magento .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[5] = 1
                

        url = requests.get(SSL+host+"/app/") #Cms Magento .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[5] = 1
                
        ############
        ############
        ############

        url = requests.get(SSL+host+"/jekyll/") #Cms Jekyll .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[6] = 1
                

        url = requests.get(SSL+host+"/_config.yml") #Cms Jekyll .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[6] = 1

        url = requests.get(SSL+host+"/.jekyll-metadata") #Cms Jekyll .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[6] = 1

        url = requests.get(SSL+host+"/_layouts") #Cms Jekyll .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[6] = 1

        url = requests.get(SSL+host+"/404.md") #Cms Jekyll .
        if url.status_code == 200 or not url.status_code >= 305:
                CmsDetectar[6] = 1

        url = requests.get(SSL+host+"/about.md") #Cms Jekyll .
        if url.status_code == 200 or not url.status_code >= 305: 
                CmsDetectar[6] = 1
                
                
                
except: #Se falhar a conexao com o servidor.
        print(" [x] FALHA AO CONECTAR A SERVIDOR HTTP/HTPPS")
        
        

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
        
        
print(" [?] CMS: %s "%(CMS))


# 1 = Wordpress
# 2 = Joomla
# 3 = Mambo
# 4 = Drupal
# 5 = Magento
# 6 = Jekyll

print(" ")
print("	Listando as Portas: ")



portas = [21,22,23,25,80,81,110,113,143,443,587,2525,3306,8080]
portasdebug = 1
portas_abertas=0
for i in portas:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1.5)
    try:
        response = client.connect_ex((ip, i))
        if response == 0:
                print(" [?] PORTA: %s ABERTA"%(str(i)))
                portas_abertas = portas_abertas + 1
    except:
        portasdebug = 0
print(" [?] Portas abertas: %s"%(portas_abertas))
print(" ")

print(" Localização da HOST: ")
url = "https://api.hackertarget.com/geoip/?q=" + host 
request = requests.get(url)
localizar = request.text
print(" %s"%(localizar))


print(" ")
print(" Listando paginas admins:")

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
b = 1
for hani in passe :
    try :
    	a = SSL+host+"/"+hani
    	url = requests.get(SSL+host+"/"+hani) 
    	if url.status_code == 200 or not url.status_code >= 305:
        	print(" [?] Finder Admin: %s"%(a))
        	b = b + 1
    except:
       a = a
if b == 1:
	print(" Nenhuma pagina encontrada.")
else: 
	print(" [?] Paginas encontradas: %s "%(b - 1))




# try: tentar
# url = requests.get(SSL+"domain"+host) #"domain" é pra botar o diretorio que o subdominio esta 
# if not url.status_code == 404:       # Se apagina nao esta com erro
#       print("Subdominio detectado: ssl+dominio+host") # printa o subdominio
# except: se der errado a tentativa.

print(" ")
print(" Listando SubDominios:")
host = host.replace("www.","") # formata a palavra sem www
debug = 1

try:
        url = requests.get(SSL+"ftp."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: ftp.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"mail."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: mail.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"nasa."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: nasa.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"whm."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: whm.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www2."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www2.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"new."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: new.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"webdisk."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: webdisk.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"localhost."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: localhost.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"email."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: email.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"email2."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: email2.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"ns1."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: ns1.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"ns2."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: ns2.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"portal."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: portal.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"blog."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: blog.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"dns."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: dns.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"dns2."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: dns2.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"dns3."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: dns3.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"dns4."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: dns4.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"dns5."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: dns5.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"dns6."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: dns6.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"dns7."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: dns7.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"dns8."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: dns8."%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"dns9."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: dns9.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"dns10."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: dns10.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"dns11."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: dns11.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www3."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www3.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"host."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: host.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"host2."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: host2.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"stats."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: stats.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"host3."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: host3.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"video."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: video.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"wiki."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: wiki.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"mail1."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: mail1.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"mx1."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: mx1.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"forum."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: forum.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"start."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: start.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"media."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: media.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"sql."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: sql.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"api."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: api.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"list."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: list.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"backup."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: backup.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"images."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: images.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"img."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: img.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"staging."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: staging.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"sip."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: sip.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"search."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: search.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"ads."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: ads.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"remote."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: remote.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"ipv4."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: ipv4.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"store."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: store.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"wap."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: wap.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"if."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: if.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"svn."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: svn.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"my."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: my.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"mx2."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: mx2.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"chat."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: chat.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"forums."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: forums.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"exchange."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: exchange.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"mail123."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: mail123.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"dev."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: dev.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"apps."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: apps.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"mysql."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: mysql.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"proxy."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: proxy.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"contents."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: contents.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"visa."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: visa.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cc."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cc.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"pagar."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: pagar.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"user."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: user.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"usuario."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: usuario.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"client."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: client.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"painel."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: painel.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"panel."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: panel.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"shell."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: shell.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"date."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: date.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"workspace."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: workspace.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"space."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: space.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"work."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: work.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"tools."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: tools.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"intern."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: intern.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"default."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: default.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"bot."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: bot.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"crew."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: crew.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"css."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: css.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"admin."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: admin.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"wlan."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: wlan.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"dev."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: dev.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"fuck."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: fuck.%s"%(host))
                

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"teste."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: teste.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"test."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: test.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"txt."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: txt.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"eua."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: eua.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"br."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: br.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"demo."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: demo.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"moodle."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: moodle.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"games."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: games.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"gateway."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: gateway.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"view."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: view.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"bost2."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: host2.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"config."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: config.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"server1."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: server1.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"jobs."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: jobs.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"kill."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: kill.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"buy."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: buy.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"suport."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: suport.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0


try:
        url = requests.get(SSL+"help."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: help.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"preview."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: preview.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"123ftp."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: 123ftp.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0
try:
        url = requests.get(SSL+"service."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: service.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"vga."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: vga.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"buy."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: buy.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"fodation."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: fodation.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"hack."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: hack.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"me."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: me.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel1."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel1.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel2."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel2.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0


try:
        url = requests.get(SSL+"cpanel3."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel3.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel4."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel4.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel5."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel5.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel6."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel6.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel7."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel7.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel8."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel8.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel9."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel9.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel10."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel10.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel11."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel11.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel12."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel12.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel13."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel13.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel14."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel14.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel16."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel16.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel17."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel17.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel18."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel18.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel19."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel19.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"cpanel20."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: cpanel20.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"new2."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: new2.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"master."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: master.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"sub."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: sub.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"contruct."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: contruct.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"git."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: git.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"bug."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: bug.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www3."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www3.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www4."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www4.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www5."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www5.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www6."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www6.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www7."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www7.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www8."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www8.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www9."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www9.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www10."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www10.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www11."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www11.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www12."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www12.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www13."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www13.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www14."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www14.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"www15."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: www15.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"dowloand."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: dowloand.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"down."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: down.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"baixar."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: baixar.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"genero."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: genero.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"direct."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: direct.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"marker."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: marker.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"maker."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: maker.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"name."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: name.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"loja."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: loja.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"public."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: public.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0

try:
        url = requests.get(SSL+"correio."+host) # www.
        if not url.status_code == 404:
                print(" [?] SUB-DOMINIO DETECTADO: correio.%s"%(host))

except requests.exceptions.ConnectionError:
        debug = 0
