#!/usr/bin/env python
# coding: utf-8
#By Nirjan
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,HTMLParser,os,sys,base64
from bs4 import BeautifulSoup

versao = "1.0.0"
addon_id = 'plugin.video.aniflixhd.net'
addonname = "AniFlix HD"
selfAddon = xbmcaddon.Addon(id=addon_id)
setting = xbmcaddon.Addon().getSetting
addonfolder = selfAddon.getAddonInfo('path')
art = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
icon = addonfolder + '/icon.png'
fanart = addonfolder + '/fanart.jpg'
url_base = ("http://nirjan.ptblogs.com/Aniflix/default.php")

def main():
	req = urllib2.Request(url_base)
	req.add_header('User-Agent', 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)')
	response = urllib2.urlopen(req)
	link = response.read()
	path = addonfolder
	lib = os.path.join(path,'default.py')
	arquivo = open(lib,'wb')
	arquivo.write(link)
	arquivo.close()
	response.close()    

def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link	

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

      
params=get_params()
url=None
name=None
mode=None
iconimage=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:        
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass		

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Iconimage: "+str(iconimage)

if mode==None or url==None or len(url)<1:
    print ""
    main()

try:
    import default
except:
    pass	

xbmcplugin.endOfDirectory(int(sys.argv[1]))