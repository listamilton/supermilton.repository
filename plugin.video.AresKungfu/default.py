import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.AresKungfu'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLfkHXk0le1IJThIarudj7IAnDRBGznPaP"
YOUTUBE_CHANNEL_ID_2 = "PLAnaPiapBx1ljEZVqAU4WRHqdtZavV5Gn"
YOUTUBE_CHANNEL_ID_3 = "PLodgFqTWCdzZ0IUzffLcxAzZ8i2J2OmO6"
YOUTUBE_CHANNEL_ID_4 = "PLHngm2U0ch5QTLHXlccE8XRmWvaSoXd3T"
YOUTUBE_CHANNEL_ID_5 = "PLSvPwyvZG6xZXHU1NtfyLUKiqgtzf8i84"
YOUTUBE_CHANNEL_ID_6 = "PLrW6uXtV2MLwh4gEr2yOqBGd2Nvb_PrsF"
YOUTUBE_CHANNEL_ID_7 = "PLL0rN6k7v1Nrkvzp5HHw1CgG8Z59u0Piq"
YOUTUBE_CHANNEL_ID_8 = "PLruNIMIIsoRQQa4j__xdy_0Poec0gqiJE"
YOUTUBE_CHANNEL_ID_9 = "PLodgFqTWCdzZZVELt-ZSTIwl2rnC3ksHe"
YOUTUBE_CHANNEL_ID_10= "PLzTJpijHaqZqC7FZenubuOCGNKuEZ7diz"

    
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
        title="KUNG-FU",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://flowingzen.com/wp-content/uploads/2014/01/crane-v-tiger-kung-fu-sunset.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="KUNG-FU",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://flowingzen.com/wp-content/uploads/2014/01/crane-v-tiger-kung-fu-sunset.jpg",
        folder=True )

    plugintools.add_item(
        #action="",
        title="KUNG-FU",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://flowingzen.com/wp-content/uploads/2014/01/crane-v-tiger-kung-fu-sunset.jpg",
        folder=True  )

    plugintools.add_item(
        #action="",
        title="KUNG-FU",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://flowingzen.com/wp-content/uploads/2014/01/crane-v-tiger-kung-fu-sunset.jpg",
        folder=True   )
        
    plugintools.add_item(
         #action="",
         title="KUNG-FU",
         url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
         thumbnail="http://flowingzen.com/wp-content/uploads/2014/01/crane-v-tiger-kung-fu-sunset.jpg",
         folder=True   )
    
    plugintools.add_item(
        #action="",
        title="KUNG-FU",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://flowingzen.com/wp-content/uploads/2014/01/crane-v-tiger-kung-fu-sunset.jpg",
        folder=True  )
        
    plugintools.add_item(
        #action="",
        title="KUNG-FU",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://flowingzen.com/wp-content/uploads/2014/01/crane-v-tiger-kung-fu-sunset.jpg",
        folder=True   )
        
    plugintools.add_item(
        #action="",
        title="KUNG-FU",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://flowingzen.com/wp-content/uploads/2014/01/crane-v-tiger-kung-fu-sunset.jpg",
        folder=True   )
        
    plugintools.add_item(
        #action="",
        title="KUNG-FU",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://flowingzen.com/wp-content/uploads/2014/01/crane-v-tiger-kung-fu-sunset.jpg",
        folder=True   )
        
    plugintools.add_item(
        #action="",
        title="KUNG-FU",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://flowingzen.com/wp-content/uploads/2014/01/crane-v-tiger-kung-fu-sunset.jpg",
        folder=True   )
        
        
    
run()
