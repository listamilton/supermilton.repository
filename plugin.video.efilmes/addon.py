#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright 2015 acamposxp
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


##############BIBLIOTECAS A IMPORTAR E DEFINICOES####################

import urllib, urllib2, re, xbmcplugin, xbmcgui, xbmc, xbmcaddon, HTMLParser, urlresolver
import xml.etree.ElementTree as ET
import jsunpack
from bs4 import BeautifulSoup

h = HTMLParser.HTMLParser()

addon_id = 'plugin.video.efilmes'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = '/resources/img/'


################################################## 

# MENUS############################################
def CATEGORIES():
    dialog = xbmcgui.Dialog()
    addDir('[B]ANIMAÇÃO[/B]', 'http://efilmesnarede.com/category/animacao/', 1, 'http://i.imgur.com/W2okuob.jpg')
    addDir('[B]AVENTURA[/B]', 'http://efilmesnarede.com/category/aventura/', 1, 'http://i.imgur.com/WeLHJy9.jpg')
    addDir('[B]COMÉDIA[/B]', 'http://efilmesnarede.com/category/comedia/', 1, 'http://i.imgur.com/PomZHty.jpg')
    addDir('[B]COMÉDIA ROMÂNTICA[/B]', 'http://efilmesnarede.com/category/comedia-romantica/', 1,
           'http://i.imgur.com/4Agolcp.jpg')
    addDir('[B]DOCUMENTÁRIO[/B]', 'http://efilmesnarede.com/category/documentario/', 1,
           'http://i.imgur.com/VjHRh57.jpg')
    addDir('[B]DRAMA[/B]', 'http://efilmesnarede.com/category/drama/', 1, 'http://i.imgur.com/WpW1gqD.jpg')
    addDir('[B]FANTASIA[/B]', 'http://efilmesnarede.com/category/fantasia/', 1, 'http://i.imgur.com/DGpMnRL.jpg')
    addDir('[B]FAROESTE[/B]', 'http://efilmesnarede.com/category/faroeste/', 1, 'http://i.imgur.com/KazScUI.jpg')
    addDir('[B]FICÇÃO CIENTÍFICA[/B]', 'http://efilmesnarede.com/category/ficcao/', 1,
           'http://i.imgur.com/i7hCgvV.jpg')
    addDir('[B]GUERRA[/B]', 'http://efilmesnarede.com/category/guerra/', 1, 'http://i.imgur.com/eOK658J.jpg')
    addDir('[B]MUSICAL[/B]', 'http://efilmesnarede.com/category/musical/', 1, 'http://i.imgur.com/sIpnMfJ.jpg')
    addDir('[B]NACIONAL[/B]', 'http://efilmesnarede.com/category/nacional/', 1, 'http://i.imgur.com/3TTKH4e.jpg')
    addDir('[B]POLICIAL[/B]', 'http://efilmesnarede.com/category/policial/', 1, 'http://i.imgur.com/VgG7V15.jpg')
    addDir('[B]ROMANCE[/B]', 'http://efilmesnarede.com/category/romance/', 1, 'http://i.imgur.com/Gz341un.jpg')
    addDir('[B]SUSPENSE[/B]', 'http://efilmesnarede.com/category/suspense/', 1, 'http://i.imgur.com/bhVu5fU.jpg')
    addDir('[B]TERROR[/B]', 'http://efilmesnarede.com/category/terror/', 1, 'http://i.imgur.com/uBYk5rh.jpg')
    addDir('[B]THRILLER[/B]', 'http://efilmesnarede.com/category/thriller/', 1, 'http://i.imgur.com/bhVu5fU.jpg')
    addDir('[B]PESQUISAR[/B]', '-', 3, 'http://www.shoppingportaldaserra.com.br/2013/img/lupa.png')	
    xbmc.executebuiltin('Container.SetViewMode(500)')


###################################################################################
# FUNCOES

def listar_videos(url):
    codigo_fonte = abrir_url(url)
    grupo = re.findall(
        '<div class="titulo"><a href="(.+?)" title="(.+?)">.+?<img src="(.+?)" width="135" height="169"/>',
        abrir_url(url), re.DOTALL)
    for link, nomefilme, imgfilme in grupo:
        nomefilme = nomefilme.replace('Assistir', "").replace('Filme',"").replace('&#8211;',"")
        addDirPlayer(nomefilme, link, 4, imgfilme, False)
    # Parte do codigo para o "link" da pagina seguinte
    # <a class='blog-pager-older-link' href='http://www.cinemaemcasa.pt/search/label/Anima%C3%A7%C3%A3o?updated-max=2015-03-21T13:00:00Z&amp;max-results=20&amp;start=15&amp;by-date=false' id='Blog1_blog-pager-older-link' title='Next Post'>Mais Filmes &#187;</a>
    page = re.compile('<a class="nextpostslink" rel="next" href="(.+?)">»</a>').findall(abrir_url(url))
    for prox_pagina in page:
        addDir('Página Seguinte >>', prox_pagina, 1, "http://i.imgur.com/63Qyw7k.png")
        break

    xbmc.executebuiltin("Container.SetViewMode(500)")
	

def pesquisa():
    keyb = xbmc.Keyboard('', 'Escreva o parâmetro de pesquisa')  # Chama o keyboard do XBMC com a frase indicada
    keyb.doModal()  # Espera ate que seja confirmada uma determinada string
    if (keyb.isConfirmed()):  # Se a entrada estiver confirmada (isto e, se carregar no OK)
        search = keyb.getText()  # Variavel search fica definida com o conteudo do formulario
        parametro_pesquisa = urllib.quote(
            search)  # parametro_pesquisa faz o quote da expressao search, isto Ã©, escapa os parametros necessarios para ser incorporado num endereÃ§o url
        url = 'http://efilmesnarede.com/?s=' + str(
            parametro_pesquisa)  # nova definicao de url. str forÃ§a o parametro de pesquisa a ser uma string
        listar_videos(url)  # chama a funÃ§Ã£o listar_videos com o url definido em cima


# Resolvers
def obtem_neodrive(url):
	codigo_fonte = abrir_url(url)
	
	try:
		url_video = re.findall(r'vurl.=."(.*?)";',codigo_fonte)[0]
		return [url_video,"-"]
	except:
		return ["-","-"]
		
		
def obtem_neodrive2(url):
	codigo_fonte = abrir_url(url)
	
	try:
		url_video = re.findall(r'vurl.=."(.*?)";',codigo_fonte)[0]
		return [url_video,"-"]
	except:
		return ["-","-"]		
		

def obtem_videopw(url):
	codigo_fonte = abrir_url(url)
	
	try:
		url_video = re.findall(r'var vurl2 = "(.*?)";',codigo_fonte)[0]
		return [url_video,"-"]
	except:
		return ["-","-"]


def obtem_videopw2(url):
	codigo_fonte = abrir_url(url)
	
	try:
		url_video = re.findall(r'var vurl2 = "(.*?)";',codigo_fonte)[0]
		return [url_video,"-"]
	except:
		return ["-","-"]		


def obtem_videomega(url):
    codigo_fonte = abrir_url(url)
    code = re.compile('document.write\(unescape\("(.+?)"\)\)\;').findall(codigo_fonte)
    texto = urllib.unquote(code[0])
    try:
        url_video = re.compile('file: "(.+?)"').findall(texto)[0]
    except:
        url_video = '-'
    try:
        url_legendas = re.compile('http://videomega.tv/servesrt.php\?s=(.+?).srt').findall(texto)[0] + '.srt'
    except:
        url_legendas = '-'
    return [url_video, url_legendas]


def videomega_resolver(referer):
    html = abrir_url(referer)

    ref_data = {'Host': 'videomega.tv',
                'Connection': 'Keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                'Referer': referer}

    if re.search('http://videomega.tv/iframe.js', html):
        lines = html.splitlines()
        aux = ''
        for line in lines:
            if re.search('http://videomega.tv/iframe.js', line):
                aux = line
                break;
        ref = re.compile('ref="(.+?)"').findall(line)[0]
    else:
        try:
            hash = re.compile('"http://videomega.tv/validatehash.php\?hashkey\=(.+?)"').findall(html)[0]
            ref = re.compile('ref="(.+?)"').findall(
                abrir_url_tommy("http://videomega.tv/validatehash.php?hashkey=" + hash, ref_data))[0]
        except:
            try:
                hash = re.compile("'http://videomega.tv/validatehash.php\?hashkey\=(.+?)'").findall(html)[0]
                ref = re.compile('ref="(.+?)"').findall(
                    abrir_url_tommy("http://videomega.tv/validatehash.php?hashkey=" + hash, ref_data))[0]
            except:
                iframe = re.compile('"http://videomega.tv/iframe.php\?(.+?)"').findall(html)[0] + '&'
                ref = re.compile('ref=(.+?)&').findall(iframe)[0]

    url = 'http://videomega.tv/cdn.php?ref=' + ref + '&width=638&height=431&val=1'
    iframe_html = abrir_url_tommy(url, ref_data)
    code = re.compile('document.write\(unescape\("(.+?)"\)\)\;').findall(iframe_html)
    id = re.compile('<div id="(.+?)" name="adblock"').findall(iframe_html)[0]
    texto = ''
    for c in code:
        aux = urllib.unquote(c)
        if re.search(id, aux):
            texto = aux
            break
    if texto == '': return ['-', '-']
    try:
        url_video = re.compile('file:"(.+?)"').findall(texto)[0]
    except:
        try:
            url_video = re.compile('file: "(.+?)"').findall(texto)[0]
        except:
            url_video = '-'
    if not 'mp4' in url_video: return ['-', '-']
    try:
        url_legendas = re.compile('http://videomega.tv/servesrt.php\?s=(.+?).srt').findall(texto)[0] + '.srt'
    except:
        url_legendas = '-'
    ref_data = {'Host': url_video.split('/')[2],
                'Connection': 'Keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                'Referer': 'http://videomega.tv/player/jwplayer.flash.swf'}
    return [url_video + headers_str(ref_data), url_legendas]


def obtem_url_dropvideo(url):
	codigo_fonte = abrir_url(url)
	try:
		soup = BeautifulSoup(codigo_fonte)
		lista = soup.findAll('script')
		js = str(lista[9]).replace('<script>',"").replace('</script>',"")
		sUnpacked = jsunpack.unpack(js)
		print sUnpacked
		url_video = re.findall(r'var vurl2="(.*?)";', sUnpacked)
		url_video = str(url_video).replace("['","").replace("']","")
		return [url_video,"-"]
	except:
		pass
		
		
def obtem_url_dropvideo2(url):
	codigo_fonte = abrir_url(url)
	try:
		soup = BeautifulSoup(codigo_fonte)
		lista = soup.findAll('script')
		js = str(lista[9]).replace('<script>',"").replace('</script>',"")
		sUnpacked = jsunpack.unpack(js)
		print sUnpacked
		url_video = re.findall(r'var vurl2="(.*?)";', sUnpacked)
		url_video = str(url_video).replace("['","").replace("']","")
		return [url_video,"-"]
	except:
		pass		

###################################################################################
# FUNCOES JÁ FEITAS
def abrir_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link = response.read()
    response.close()
    return link


#
def addLink(name, url, iconimage):
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setProperty('fanart_image', addonfolder + artfolder + 'fanart.png')
    liz.setInfo(type="Video", infoLabels={"Title": name})
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=liz)
    return ok


#

def addDir(name, url, mode, iconimage, pasta=True):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=pasta)
    return ok
	
def addDirPlayer(name, url, mode, iconimage, pasta=False):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=pasta)
    return ok	
	

#
def player(name, url, iconimage):
    dropmega = r'src=".*?drop.*?id=(.*?)"'
    dropmega2 = r'src=".*?drop.*?/embed/(.*?)"'	
    videopw = r'src=".*?videopw.*?/e/(.*?)"'
    videopw2 = r'src=".*?videopw.*?id=(.*?)"'	
    neomega = r'src=".*?neodrive.*?id=(.*?)"'
    neomega2 = r'src=".*?neodrive.*?id=(.*?)"'	
    flashx = r'src=".*?flashx.*?id=(.*?)"'
    videomega = r'src=".*?videomega.*?ref=(.*?)"'
    nowvideo = r'src=".*?nowvideo.*?id=(.*?)"'
    okru = r'src=".*?okru.*?id=(.*?)"'
    mensagemprogresso = xbmcgui.DialogProgress()
    mensagemprogresso.create('eFilmesnaRede', 'A resolver link', 'Por favor aguarde...')
    mensagemprogresso.update(33)
    links = []
    hosts = []
    matriz = []
    codigo_fonte = abrir_url(url)
    # try: url_video = re.findall(r'<iframe src="(.*?)" width="738" height="400" frameborder="0"></iframe></li>',codigo_fonte)[0]
    # <iframe src="(.*?)" width="738" height="400" frameborder="0"></iframe></li>
    # except: return
    try:
        links.append(re.findall(cloudzilla_e, codigo_fonte)[0])  # http://www.cloudzilla.to/embed/%s
        hosts.append('CloudZilla')
    except:
        pass
    try:
        links.append('http://www.cloudzilla.to/embed/%s' % re.findall(cludzilla_s, codigo_fonte)[0])  # http://www.cloudzilla.to/embed/%s
        hosts.append('CloudZilla')
    except:
        pass
    try:
        links.append('http://vidigvideo.com/embed-%s-885x660.html' % re.findall(vidig_s, codigo_fonte)[0])
        hosts.append('Vidig')
    except:
        pass
    try:
        links.append(re.findall(vidig, codigo_fonte)[0])
        hosts.append('Vidig')
    except:
        pass
    try:
        links.append(re.findall(okru, codigo_fonte)[0])
        hosts.append('Odnoklassniki')
    except:
        pass
    try:
        links.append(re.findall(videomail, codigo_fonte)[0])
        hosts.append('Videomail')
    except:
        pass
    try:
        links.append('http://neodrive.co/embed/'+re.findall(neomega, codigo_fonte)[0])
        hosts.append('Neodrive')
    except:
        pass
    try:
        links.append('http://neodrive.co/embed/'+re.findall(neomega2, codigo_fonte)[0])
        hosts.append('Neodrive2')
    except:
        pass		
    try:
        links.append(re.findall(videomega, codigo_fonte)[0])
        hosts.append('Videomega')
    except:
        pass
    try:
        links.append(re.findall(flashx, codigo_fonte)[0])
        hosts.append('Flashx')
    except:
        pass
    try:
        links.append('http://videopw.com/e/'+re.findall(videopw, codigo_fonte)[0])
        hosts.append('Videopw')
    except:
        pass
    try:
        links.append('http://videopw.com'+re.findall(videopw2, codigo_fonte)[0])
        hosts.append('Videopw2')
    except:
        pass		
    try:
        links.append(re.findall(vidzi, codigo_fonte)[0])
        hosts.append('Vidzi')
    except:
        pass
    try:
        links.append(re.findall(videobis, codigo_fonte)[0])
        hosts.append('VideoBis')
    except:
        pass
    try:
        links.append(re.findall(videott, codigo_fonte)[0])
        hosts.append('Video.TT')
    except:
        pass
    try:
        links.append(re.findall(picasa, codigo_fonte)[0])
        hosts.append('Picasa')
    except:
        pass
    try:
        links.append(re.findall(google, codigo_fonte)[0])
        hosts.append('Gdrive')
    except:
        pass
    try:
        links.append(re.findall(vk, codigo_fonte)[0])
        hosts.append('Vk')
    except:
        pass
    try:
        links.append(re.findall(nvideo, codigo_fonte)[0])
        hosts.append('Nowvideo - Sem suporte')
    except:
        pass
    try:
        links.append(re.findall(dropvideo, codigo_fonte)[0])
        hosts.append('Dropvideo')
    except:
        pass
    try:
        links.append('http://www.dropvideo.com/embed/'+re.findall(dropmega, codigo_fonte)[0])
        hosts.append('Dropvideo')
    except:
        pass
    try:
        links.append('http://www.dropvideo.com/embed/'+re.findall(dropmega2, codigo_fonte)[0])
        hosts.append('Dropvideo2')
    except:
        pass		
    try:
        links.append('http://www.cloudzilla.to/embed/' + re.findall(cloudzilla, codigo_fonte)[0])
        hosts.append('CloudZilla')
    except:
        pass
    try:
        links.append('http://www.cloudzilla.to/embed/' + re.findall(cloudzilla_t, codigo_fonte)[0])
        hosts.append('CloudZilla(Legendado)')
    except:
        pass
    try:
        links.append(re.findall(vodlocker, codigo_fonte)[0])
        hosts.append('Vodlocker')
    except:
        pass
    try:
        links.append('http://www.firedrive.com/embed/' + re.findall(firedrive2, codigo_fonte)[0])
        hosts.append('Firedrive')
    except:
        pass
    if not hosts:
        mensagemprogresso.update(100)
        mensagemprogresso.close()
        return

    index = xbmcgui.Dialog().select('Selecione um dos hosts suportados :', hosts)

    if index == -1:
        return

    url_video = links[index]
    mensagemprogresso.update(66)

    if 'google' in url_video:
        matriz = obtem_url_google(url_video)
    elif 'dropvideo.com/embed' in url_video:
        matriz = obtem_url_dropvideo(url_video)   # esta linha está a mais
    elif 'dropvideo.com/embed' in url_video:
        matriz = obtem_url_dropvideo2(url_video)   # esta linha está a mais		
    elif 'filmesonlinebr.info/player' in url_video:
        matriz = obtem_url_picasa(url_video)
    elif 'vk.com/video_ext' in url_video:
        matriz = obtem_url_vk(url_video)
    elif 'neodrive' in url_video:
        matriz = obtem_neodrive(url_video)
    elif 'neodrive' in url_video:
        matriz = obtem_neodrive2(url_video)		
    elif 'http://ok.ru' in url_video:
        matriz = obtem_okru(url_video)
    elif 'vodlocker.com' in url_video:
        matriz = obtem_url_vodlocker(url_video)
    elif 'firedrive.com/embed' in url_video:
        matriz = obtem_url_firedrive(url_video)
    elif 'cloudzilla' in url_video:
        matriz = obtem_cloudzilla(url_video)
    elif 'http://video.tt' in url_video:
        matriz = obtem_videott(url_video)
    elif 'videobis.net' in url_video:
        matriz = obtem_videobis(url_video)  # video.pw
    elif 'videopw' in url_video:
        matriz = obtem_videopw(url_video)  # video.pw
    elif 'videopw2' in url_video:
        matriz = obtem_videopw2(url_video)  # video.pw		
    elif 'vidzi.tv' in url_video:
        matriz = obtem_vidig(url_video)
    elif 'mail.ru' in url_video:
        matriz = obtem_videomail(url_video)
    elif 'videomega.tv' in url_video:
        matriz = videomega_resolver(url_video)
    else:
        print "Falha: " + str(url_video)

    url = matriz[0]

    if url == '-':
        mensagemprogresso.update(100)
        mensagemprogresso.close()
        return

    mensagemprogresso.update(100)
    mensagemprogresso.close()

    listitem = xbmcgui.ListItem()  # name, iconImage="DefaultVideo.png", thumbnailImage="DefaultVideo.png"
    listitem.setPath(url)
    listitem.setProperty('mimetype', 'video/mp4')
    listitem.setProperty('IsPlayable', 'true')
    # try:
    xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
    xbmcPlayer.play(url)
    return
        
############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################

def get_params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?', '')
        if (params[len(params) - 1] == '/'):
            params = params[0:len(params) - 2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]

    return param


params = get_params()
url = None
name = None
mode = None
iconimage = None

try:
    url = urllib.unquote_plus(params["url"])
except:
    pass
try:
    name = urllib.unquote_plus(params["name"])
except:
    pass
try:
    mode = int(params["mode"])
except:
    pass

try:
    iconimage = urllib.unquote_plus(params["iconimage"])
except:
    pass

print "Mode: " + str(mode)
print "URL: " + str(url)
print "Name: " + str(name)
print "Iconimage: " + str(iconimage)


###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################


if mode == None or url == None or len(url) < 1:
    print ""
    CATEGORIES()

elif mode == 1:
    print ""
    listar_videos(url)

elif mode == 3:
    print ""
    pesquisa()

elif mode == 4:
    print ""
    player(name, url, iconimage)
	

xbmcplugin.endOfDirectory(int(sys.argv[1]))