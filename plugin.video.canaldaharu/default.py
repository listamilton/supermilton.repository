# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/canaldaharu
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import os
import sys
import time
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.canaldaharu'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
#icon = local.getAddonInfo('icon')
icon = "https://66.media.tumblr.com/d41783d240df469602fc33b0b6bbb53d/tumblr_o72ld4rPgr1tjlg3so1_500.jpg"
addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"

YOUTUBE_CHANNEL_ID = "HaruJiggly"

# Ponto de Entrada
def run():
	# Pega Parâmetros
	params = plugintools.get_params()
	
	if params.get("action") is None:
		xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(entryurl)
		
		while xbmc.Player().isPlaying():
			time.sleep(1)

		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"

	plugintools.close_item_list()

# Menu Principal
def main_list(params):
	plugintools.log("canaldaharu.main_list "+repr(params))
	
	plugintools.log("canaldaharu.run")
	
	#plugintools.direct_play(str(entryurl))

	plugintools.add_item(
		title = "Canal da Haru",
		url = "plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID+"/",
		thumbnail = icon,
		folder = True )
		

run()