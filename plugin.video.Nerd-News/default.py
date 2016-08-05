# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/MarcioCandido06 
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools

from addon.common.addon import Addon

addonID = 'plugin.video.Nerd-News'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'


def run():
    plugintools.log("Nerd-News.run")
    
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

def main_list(params):
		plugintools.log("kodicenter ===> " + repr(params))

                icon2 = "https://pbs.twimg.com/profile_images/648985217529724928/eloz4kiW_200x200.png"


                plugintools.add_item(title = "Nerd News"              , url = base + "channel/UCVTPXwVDI1Ab85guTAkE3Rw/", thumbnail = icon2, folder = True)
                
		

		
		
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		xbmc.executebuiltin('Container.SetViewMode(500)')
		
run()
