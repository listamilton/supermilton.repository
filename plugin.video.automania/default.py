# -*- coding: utf-8 -*-
#------------------------------------------------------------
# The Prem Addon by udan
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: udan
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.automania'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "TopGear"
YOUTUBE_CHANNEL_ID_2 = "UC87jvYlwLcKqxYmhIlP0bgA"
YOUTUBE_CHANNEL_ID_3 = "Formula1"
YOUTUBE_CHANNEL_ID_4 = "indycars"
YOUTUBE_CHANNEL_ID_5 = "motousa"
YOUTUBE_CHANNEL_ID_6 = "TheOfficialNASCAR"
YOUTUBE_CHANNEL_ID_7 = "UnitedSportsCar"
YOUTUBE_CHANNEL_ID_8 = "AMAProVids"
YOUTUBE_CHANNEL_ID_9 = "KMan2100"
YOUTUBE_CHANNEL_ID_10 = "MotorTrend"
YOUTUBE_CHANNEL_ID_11 = "GoodwoodTV"
YOUTUBE_CHANNEL_ID_12 = "UC9NM8DvGJvJ08OWMHgxcsbQ"
YOUTUBE_CHANNEL_ID_13 = "RaceWorldTVChannel"
YOUTUBE_CHANNEL_ID_14 = "FIAF3EUROPE"
YOUTUBE_CHANNEL_ID_15 = "EVOTV"
YOUTUBE_CHANNEL_ID_16 = "mightycarmods"
YOUTUBE_CHANNEL_ID_17 = "StockCarMagazine"
YOUTUBE_CHANNEL_ID_18 = "StadiumSUPERTrucks"
YOUTUBE_CHANNEL_ID_19 = "PsychosisPC05"
YOUTUBE_CHANNEL_ID_20 = "speedwaytv1"
YOUTUBE_CHANNEL_ID_21 = "UCO-tVbRdSCmsowpz7CfzTbw"

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Top Gear (890+ Video Clips)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-3778qljvKEQ/AAAAAAAAAAI/AAAAAAAAAAA/g-bHapsDzwQ/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Le Mans Story (100+ Video Clips)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-lNmKlQRrhvc/AAAAAAAAAAI/AAAAAAAAAAA/e4tawmN6dmw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FORMULA 1 (200+ Video Clips)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-p4tzDhRHziM/AAAAAAAAAAI/AAAAAAAAAAA/BgBf89zrN30/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Indycar (2700+ Video Clips)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-CWXwc53cELY/AAAAAAAAAAI/AAAAAAAAAAA/k_mm6XIanrM/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Motorcycle USA (1000+ Video Clips)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-OJljRcGamX0/AAAAAAAAAAI/AAAAAAAAAAA/u7bc-SbU1eI/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="NASCAR (3300+ Video Clips)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-mNHVvNGrAws/AAAAAAAAAAI/AAAAAAAAAAA/AMZcgnuhJBg/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="IMSA Official (300+ Video Clips) (Full Race)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-V19gAJIR_6A/AAAAAAAAAAI/AAAAAAAAAAA/WMo462KBLuE/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AMA Pro Racing (800+ Video Clips)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-Q7ehV_Fbu4Q/AAAAAAAAAAI/AAAAAAAAAAA/ckzw1ZJ_Dww/s100-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="KMan's Ultimate Drag Racing Channel (1600+ Video Clips)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-CyOECWxWkvY/AAAAAAAAAAI/AAAAAAAAAAA/-gUlhaK83iU/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Motor Trend Channel (1400+ Video Clips) Builds N Stuff",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-K-cVNW0boRs/AAAAAAAAAAI/AAAAAAAAAAA/Jg9oUhvZgjM/s100-c-k-no/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Goodwood Road & Racing (700+ Video Clips)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-zMHS-SqcCLY/AAAAAAAAAAI/AAAAAAAAAAA/_8Vbx9I-v20/s100-c-k-no/photo.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="Pimp My Ride  (USA TV Show Episodes)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-rvR25m6Sj4U/AAAAAAAAAAI/AAAAAAAAAAA/4f7UUGH-__0/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="RaceWorld TV (News & Interesting Information)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-cuTa57cgKtU/AAAAAAAAAAI/AAAAAAAAAAA/i5qnD4TSgy0/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="FIA Formula 3 European Championship (Full Races)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-g7AbmNrpI34/AAAAAAAAAAI/AAAAAAAAAAA/62KDdkQlpoQ/s100-c-k-no/photo.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="EVO (Geneva Motor Show 2016) N Stuff",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/-KAgWM3MEykA/AAAAAAAAAAI/AAAAAAAAAAA/jQCzeZC2tcw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mighty Car Mods (Aussie Mod Guys)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-b8-0ku2pp-U/AAAAAAAAAAI/AAAAAAAAAAA/2QftimURo_A/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Stock Car  Magazine (British Stock car Racing)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-8sktAHw5DmU/AAAAAAAAAAI/AAAAAAAAAAA/f2YRAwgdkp0/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="StadiumSUPERTrucks (Pickup Truck Racing Full Races)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://i.ytimg.com/i/2LnjzvWORxZ1b8im7ZwzCw/mq1.jpg?v=509724a5",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Racing Psychosis (Go-Cart Racing & Tips)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/-npaMiV5mhZU/AAAAAAAAAAI/AAAAAAAAAAA/ZNlXWwWF4_c/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SPEEDWAY TV (Bike Speedway)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://i.ytimg.com/i/k1GnM8RjkY8a2dkcgjPrmg/mq1.jpg?v=514efd04",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Other Perflix.TV Addons",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="http://perflix.tv/wizard/perflixlogo.png",
        folder=True )   		
run()
