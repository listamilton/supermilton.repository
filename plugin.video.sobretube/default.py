# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/OMundo2osBrasileiros
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools

from addon.common.addon import Addon

addonID = 'plugin.video.sobretube'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

icon1 = 'https://yt3.ggpht.com/-e3wkxRAmx0I/AAAAAAAAAAI/AAAAAAAAAAA/hQyndGxIf5M/s100-c-k-no/photo.jpg'
icon2 = 'https://yt3.ggpht.com/-drk7bDd2Tz0/AAAAAAAAAAI/AAAAAAAAAAA/r7Pyv_DJTno/s100-c-k-no/photo.jpg'
icon3 = 'https://yt3.ggpht.com/-O6MDheQdsHY/AAAAAAAAAAI/AAAAAAAAAAA/qGeOTGHfaWQ/s176-c-k-no/photo.jpg'
icon4 = 'https://yt3.ggpht.com/-kqPpOpdrdc0/AAAAAAAAAAI/AAAAAAAAAAA/UlVQegnnZ8g/s176-c-k-no/photo.jpg'
icon5 = 'https://yt3.ggpht.com/-Zx0F3gfaHzc/AAAAAAAAAAI/AAAAAAAAAAA/RNlEX4U4TCE/s100-c-k-no/photo.jpg'
icon6 = 'https://yt3.ggpht.com/-fGQ-EGV6Stc/AAAAAAAAAAI/AAAAAAAAAAA/5YD5fcLhK_g/s100-c-k-no/photo.jpg'
icon7 = 'https://yt3.ggpht.com/-BzZFa6i7zyI/AAAAAAAAAAI/AAAAAAAAAAA/N3A36PLu3CA/s88-c-k-no/photo.jpg'

def run():
    plugintools.log("DocBrasil.run")
    
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

def main_list(params):
		plugintools.log("DocBrasil ===> " + repr(params))

		plugintools.add_item(title = "Canal AssombradO.com.br"       , url = base + "user/AssombradoBlog/"            , thumbnail = icon1, folder = True)
		plugintools.add_item(title = "Encarando o Sobrenatural"     , url = base + "channel/UCxR9jCW0ZFSWL9_BQJwlaaQ/", thumbnail = icon2, folder = True)
		plugintools.add_item(title = "Ambu Play"                    , url = base + "user/AmbuPlay/"                , thumbnail = icon3, folder = True)	

		plugintools.add_item(title = "Tio Lu"                       , url = base + "channel/UCUA-pQmmsor1nWCqFRr-zSw/", thumbnail = icon4, folder = True)	

                plugintools.add_item(title = "David Herick"                    , url = base + "user/davi170994/"               , thumbnail = icon5, folder = True)	
              
		plugintools.add_item(title = "DR MISTERIO #DRM"                , url = base + "user/DRMisterioladoB/"           , thumbnail = icon6, folder = True)	

		plugintools.add_item(title = "Canal Oculto #legiaooculta"     , url = base + "channel/UC2bspMS-MyGe6SfHXGUKLIA/", thumbnail = icon7, folder = True)
		
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		xbmc.executebuiltin('Container.SetViewMode(500)')
		
run()
