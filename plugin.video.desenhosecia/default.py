#!/usr/bin/env python
# -*- coding: UTF-8 -*-
##############BIBLIOTECAS A IMPORTAR####################
import xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,sys,urllib,urllib2,re
from bs4 import BeautifulSoup
import urlresolver

#######################SETTINGS#########################
addon_id = 'plugin.video.desenhosecia'
addon_name = 'Desenhos e Cia'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
art = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
icon = addonfolder + '/icon.png'
fanart = addonfolder + '/fanart.jpg'
baseurl = 'http://www.feiraogoiano.com/'

##################################################MENUS############################################

def MENU():
		addDir('[COLOR green]Ver Filmes[/COLOR]',baseurl,3,art+'icon_base.png',art+'f5.jpg','','')


def CATEGORIES():
	itens = []
	link = abrir_url(baseurl)
	match=re.compile('<a href="(.*?)">(.*?)/</a></li>').findall(link)
	for url,name in match:
		url=baseurl+url
		if 'Parent Directory' not in name and 'cgi' not in name and 'artefalada' not in name and 'audio' not in name and 'Chips Oficial' not in name:
			name=name.replace('audio','Audio').replace('perdidos no espaco terceira temporada','Perdidos no Espaço - Terceira Temporada').replace('besouro verde','Besouro Verde').replace('Osfli','Os Fli').replace('osaa','ossa')
			itens.append(name+','+url)
	for item in sorted (itens):
		params = item.split(',')
		name = params[0]
		url = params[1]
		addDir(name,url,4,'','','')
		xbmc.executebuiltin('Container.SetViewMode(502)')
#	addDir('*Coelho Ricochete','http://www.feiraogoiano.com/Chips%20Oficial/Coelho%20ricochete/',4,'','','')
#	addDir('*Johnny Quest','http://www.feiraogoiano.com/Chips%20Oficial/Johnny%20Quest/',4,'','','')
	listar_esp2()
def listar_filmes(url):
	itens = []
	link = abrir_url(url)
	match1=re.compile(' <title>Index of /(.*?)</title>').findall(link)
	for diretorio in match1:
		dir=diretorio
	match=re.compile('<li><a href="(.*?)"> (.*?)</a></li>').findall(link)
	for url,name in match:
		url=baseurl+dir+'/'+url
		url=url.replace('amp;','').replace(' ','%20')
		name=name.replace('&amp;','&').replace('(1)','(01)').replace('(2)','(02)').replace('(3)','(03)').replace('(4)','(04)').replace('(5)','(05)').replace('(6)','(06)').replace('(7)','(07)').replace('(8)','(08)').replace('(9)','(09)')
		if 'MM' in name:
			listar_esp(url)
		if 'Parent Directory' not in name  and 'MM' not in name:
			itens.append(name+','+url)
	for item in sorted (itens):
		params = item.split(',')
		name = params[0]
		url = params[1]
		addDir(name,url,1,'','','')
		xbmc.executebuiltin('Container.SetViewMode(502)')
		
def listar_esp(url):
	itens = []
	link = abrir_url(url)
	match1=re.compile(' <title>Index of /(.*?)</title>').findall(link)
	for diretorio in match1:
		dir=diretorio
	match=re.compile('<li><a href="(.*?)"> (.*?)</a></li>').findall(link)
	for url,name in match:
		url=baseurl+dir+'/'+url
		url=url.replace('amp;','').replace(' ','%20')
		name=name.replace('&amp;','&').replace('(1)','(01)').replace('(2)','(02)').replace('(3)','(03)').replace('(4)','(04)').replace('(5)','(05)').replace('(6)','(06)').replace('(7)','(07)').replace('(8)','(08)').replace('(9)','(09)')
#		if 'Chips Oficial' in name:
#			listar_esp(url)
		if 'Parent Directory' not in name:
			itens.append(name+','+url)
	for item in sorted (itens):
		params = item.split(',')
		name = params[0]
		url = params[1]
		addDir(name,url,1,'','','')
		xbmc.executebuiltin('Container.SetViewMode(502)')
#############################
def listar_esp2():
	link = abrir_url('http://www.feiraogoiano.com/Chips%20Oficial/')
	itens = []
	match1=re.compile(' <title>Index of /(.*?)</title>').findall(link)
	for diretorio in match1:
		dir=diretorio
	match=re.compile('<li><a href="(.*?)"> (.*?)</a></li>').findall(link)
	for url,name in match:
		url=baseurl+dir+'/'+url
		url=url.replace('amp;','').replace(' ','%20')
		name=name.replace('&amp;','&').replace('(1)','(01)').replace('(2)','(02)').replace('(3)','(03)').replace('(4)','(04)').replace('(5)','(05)').replace('(6)','(06)').replace('(7)','(07)').replace('(8)','(08)').replace('(9)','(09)').replace('/','')
#		if 'Chips Oficial' in name:
#			listar_esp(url)
		if 'Parent Directory' not in name:
			itens.append(name+','+url)
	for item in sorted (itens):
		params = item.split(',')
		name = params[0]
		url = params[1]
		addDir(' '+name,url,4,'','','')
		xbmc.executebuiltin('Container.SetViewMode(502)')



##############################################################################################################
def RESOLVE(url):
	print url
	arquivo = url
	url1 = urlresolver.resolve(url)
	if url1:
		try:
			liz = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
			liz.setInfo(type="Video", infoLabels={ "Title": name })
			liz.setProperty("IsPlayable","true")
			liz.setPath(url1)
			xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
		except: pass
	else:
		liz = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
		liz.setInfo(type="Video", infoLabels={ "Title": name })
		liz.setProperty("IsPlayable","true")
		liz.setPath(url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

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


def addDir(name,url,mode,iconimage,fanart,description):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name,"Plot":description} )
		liz.setProperty('fanart_image', fanart)
		if mode==1 or mode==8:
			liz.setProperty("IsPlayable","true")
			ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		else:
			ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		return ok

def gethtml(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link = response.read()
	soup = BeautifulSoup(link)
	return soup

def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link

params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None
site=None

try:
		url=urllib.unquote_plus(params["url"])
except:
		pass
try:
		name=urllib.unquote_plus(params["name"])
except:
		pass
try:
		iconimage=urllib.unquote_plus(params["iconimage"])
except:
		pass
try:		
		mode=int(params["mode"])
except:
		pass
try:
		description=urllib.unquote_plus(params["description"])
except:
		pass


if mode==None or url==None or len(url)<1:
		print ""
		CATEGORIES()

elif mode==1:
		RESOLVE(url)

elif mode==2:
		categorias()

elif mode==3:
		todas_categorias(url)

elif mode==4:
		listar_filmes(url)

elif mode==5:
		listar_links(url)

elif mode==6:
		listar_series(url)

elif mode==7:
		listar_categorias(url)

elif mode==8:
		Player(name,url,iconimage)

elif mode==9:
		listar_esp2()

xbmcplugin.endOfDirectory(int(sys.argv[1]))