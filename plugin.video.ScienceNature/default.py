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

addonID = 'plugin.video.ScienceNature'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UC2ojPtdle7fzjOdH8JkVPZQ"
YOUTUBE_CHANNEL_ID_2 = "animalnaturewildlife"
YOUTUBE_CHANNEL_ID_3 = "PlanetDocChannel"
YOUTUBE_CHANNEL_ID_4 = "oasishdchannel"
YOUTUBE_CHANNEL_ID_5 = "EducationDocumentary"
YOUTUBE_CHANNEL_ID_6 = "Myanimallifetv"
YOUTUBE_CHANNEL_ID_7 = "UCOdvwdx--5_tlNeBff8tAng"
YOUTUBE_CHANNEL_ID_8 = "NatureHates"
YOUTUBE_CHANNEL_ID_9 = "UC62NeTy6Ocd5Jmh_963mLFg"
YOUTUBE_CHANNEL_ID_10 = "UCl8PjjOKiniDKNHZ5rmYPuw"
YOUTUBE_CHANNEL_ID_11 = "documentariesTV2014"
YOUTUBE_CHANNEL_ID_12 = "UCWtYEiYkqI7RufMNlnF1P0A"
YOUTUBE_CHANNEL_ID_13 = "UCBGniJOGgLH0AlltfuJ29gg"
YOUTUBE_CHANNEL_ID_14 = "thesecretsofnature"
YOUTUBE_CHANNEL_ID_15 = "UCKnI6LeEjA38ruGPXeV4A4w"
YOUTUBE_CHANNEL_ID_16 = "AnimalinfoTV"
YOUTUBE_CHANNEL_ID_17 = "DocumentaryDesire"
YOUTUBE_CHANNEL_ID_18 = "UCt0y9LijjjiHrlIY6zAJ_Gg"
YOUTUBE_CHANNEL_ID_19 = "UCBkLCoMRcLPYdqMSQMvl5aQ"
YOUTUBE_CHANNEL_ID_20 = "NatureVideoChannel"
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
        title="Science & Nature Documentaries HD",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-TCFCYV-Hwy4/AAAAAAAAAAI/AAAAAAAAAAA/xhi7IyLy4tY/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Animal Nature Documentary",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-BbPatKuhwZ8/AAAAAAAAAAI/AAAAAAAAAAA/J3QK4Dpv2Vw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Planet Doc",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-jSIGfZAjyTk/AAAAAAAAAAI/AAAAAAAAAAA/dvaLu4krnwI/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Love Nature",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-zrB3s0bz4bI/AAAAAAAAAAI/AAAAAAAAAAA/bS23RTJa29E/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Educational Documentary",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-D9Nv31gRQFI/AAAAAAAAAAI/AAAAAAAAAAA/orU19BjSZhI/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Animal Life TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-9NP-WKgRVys/AAAAAAAAAAI/AAAAAAAAAAA/URNNx4FcziA/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ED Documentary TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-uWc5i9K7Fkg/AAAAAAAAAAI/AAAAAAAAAAA/2hStzC_B6hk/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nature Hates You",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-gm-WoU06l8s/AAAAAAAAAAI/AAAAAAAAAAA/qNzjbjLKhOg/s100-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="XiveTV Documentaries",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-3QSaQa74Ids/AAAAAAAAAAI/AAAAAAAAAAA/tb3yzKTWgGY/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Animal Documentaries",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-5_wyC-A1AUA/AAAAAAAAAAI/AAAAAAAAAAA/g-d8WEaucxk/s100-c-k-no/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="DOCUMENTARY TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-uJ_e4EY8xDo/AAAAAAAAAAI/AAAAAAAAAAA/v6Kv-xDGmmU/s100-c-k-no/photo.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="Wildlife Documentary HD",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-CVOPvBYjWF0/AAAAAAAAAAI/AAAAAAAAAAA/Dtn1b_1frnI/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Documentary TV (Official)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-gDpCcvcAUO4/AAAAAAAAAAI/AAAAAAAAAAA/lPNAnGw4SR4/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="The Secrets of Nature",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-iztw3n2qnJM/AAAAAAAAAAI/AAAAAAAAAAA/PCf32MQpPQw/s100-c-k-no/photo.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="Documentary Collection",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/-4Pstvt3ZAxo/AAAAAAAAAAI/AAAAAAAAAAA/V4K1uJnqR_g/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Animal Info TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-Sj-IyaC0R3g/AAAAAAAAAAI/AAAAAAAAAAA/mlvJtH4oUts/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DocumentaryDesire",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-c0MXz3GTTOE/AAAAAAAAAAI/AAAAAAAAAAA/BWdOC4ne_eE/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Science&Technology 4U",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/-e5HWr2czzec/AAAAAAAAAAI/AAAAAAAAAAA/QzTOnvbVn2Y/s100-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Nat Geo Wild Documentary & Discovery HD",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/-eio6D6VZIm4/AAAAAAAAAAI/AAAAAAAAAAA/pT0Y__fv5Xk/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nature Video",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/-ps2Sp3c8T5s/AAAAAAAAAAI/AAAAAAAAAAA/ik4Hai9IVdM/s100-c-k-no/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Other Perflix.TV Addons",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="http://perflix.tv/wizard/perflixlogo.png",
        folder=True )   		
run()
