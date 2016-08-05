# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/MarcioCandido06 
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools

from addon.common.addon import Addon

addonID = 'plugin.video.ComedyTube'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

icon1 = 'https://yt3.ggpht.com/-8OYVz3F5lxU/AAAAAAAAAAI/AAAAAAAAAAA/2dOIPiZaWsM/s100-c-k-no-rj-c0xffffff/photo.jpg'
icon2 = 'https://yt3.ggpht.com/-ooVRMJ1N_QQ/AAAAAAAAAAI/AAAAAAAAAAA/IT6uGMwLxYg/s100-c-k-no-rj-c0xffffff/photo.jpg'
icon3 = 'https://yt3.ggpht.com/-xle954Zxs4E/AAAAAAAAAAI/AAAAAAAAAAA/geYaRfTQ0FY/s100-c-k-no-rj-c0xffffff/photo.jpg'
icon4 = 'https://yt3.ggpht.com/-oV5jRl-r4GA/AAAAAAAAAAI/AAAAAAAAAAA/MW_e0iGl0wc/s100-c-k-no-rj-c0xffffff/photo.jpg'
icon5 = 'https://lh4.googleusercontent.com/-KJF_SE5_Jhg/AAAAAAAAAAI/AAAAAAAAAAA/DlHsh2-ODsk/photo.jpg'
icon6 = 'https://yt3.ggpht.com/-qUvv9tgD_fc/AAAAAAAAAAI/AAAAAAAAAAA/TSsEvJb2j8A/s100-c-k-no-rj-c0xffffff/photo.jpg'
icon7 = 'https://yt3.ggpht.com/-QzJ6DOWkp2U/AAAAAAAAAAI/AAAAAAAAAAA/xqhtFQ7FE58/s100-c-k-no-rj-c0xffffff/photo.jpg'
icon8 = 'https://yt3.ggpht.com/-Z-6UaIamaRQ/AAAAAAAAAAI/AAAAAAAAAAA/Pg9QS86ipFY/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon9 = 'https://yt3.ggpht.com/-pLosxp8Dv2s/AAAAAAAAAAI/AAAAAAAAAAA/sZOF__uxZQc/s100-c-k-no-rj-c0xffffff/photo.jpg'
icon0 = 'https://yt3.ggpht.com/-UEjE1FhEQ2w/AAAAAAAAAAI/AAAAAAAAAAA/mUmazwENu48/s100-c-k-no-rj-c0xffffff/photo.jpg'
icon  = 'https://yt3.ggpht.com/-R_Gxs55BRXw/AAAAAAAAAAI/AAAAAAAAAAA/_dUTbV1Vrgw/s100-c-k-no-rj-c0xffffff/photo.jpg'

def run():
    plugintools.log("ComedyTube.run")
    
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

def main_list(params):
		plugintools.log("ComedyTube===> " + repr(params))

		plugintools.add_item(title = "Whindersson Nunes"             , url = base + "channel/UC3KQ5GWANYF8lChqjZpXsQw/"          , thumbnail = icon1, folder = True)
		plugintools.add_item(title = "É tipo isso"                   , url = base + "channel/UCrpkeAWEbFXYoIWEgNx7yzw/", thumbnail = icon2, folder = True)
		plugintools.add_item(title = "Porta dos Fundos"              , url = base + "user/portadosfundos/", thumbnail = icon3, folder = True)
		plugintools.add_item(title = "Canal BOOM"                    , url = base + "user/Boomoficial/", thumbnail = icon4, folder = True)
		plugintools.add_item(title = "Batalha de Youtubers"          , url = base + "playlist/PLj_r6fchQfwYRhfFSpRJ6MlvateXHksQ2/"     , thumbnail = icon5, folder = True)
		plugintools.add_item(title = "Parafernalha"                  , url = base + "user/canalparafernalha/", thumbnail = icon6, folder = True)
		plugintools.add_item(title = "Canal Canalha"                 , url = base + "channel/UCPHXtOVmjvbP9OJihsd7gCg/", thumbnail = icon7, folder = True)
		plugintools.add_item(title = "Galo Frito"                    , url = base + "channel/UCyb0T6J6nL5ibo0HLRMINKw/", thumbnail = icon8, folder = True)
		plugintools.add_item(title = "Barbixas"                      , url = base + "channel/UCZbgt7KIEF_755Xm14JpkCQ/", thumbnail = icon9, folder = True)
		plugintools.add_item(title = "AnimaTunes "                   , url = base + "channel/UCWAbMASyyaNzpe3zkIg2syQ/", thumbnail = icon0, folder = True)
		plugintools.add_item(title = "Encrenca Zap Zap"              , url = base + "channel/UCSL-WeSc8Pje5c7Ay7uJglw/"          , thumbnail = icon, folder = True)

		
		
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		xbmc.executebuiltin('Container.SetViewMode(500)')

		
		
		
run()