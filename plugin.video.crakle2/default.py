import urllib, urllib2, re, sys, cookielib, os
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
try:
    import simplejson as json
except:
    import json
try:
   import StorageServer
except:
   import storageserverdummy as StorageServer


__settings__ = xbmcaddon.Addon()
rootDir = __settings__.getAddonInfo('path')

programs_thumb = os.path.join(rootDir, 'resources', 'media', 'programs.png')
topics_thumb = os.path.join(rootDir, 'resources', 'media', 'topics.png')
search_thumb = os.path.join(rootDir, 'resources', 'media', 'search.png')
next_thumb = os.path.join(rootDir, 'resources', 'media', 'next.png')

# initialise cache object to speed up plugin operation
cache = StorageServer.StorageServer(__settings__.getAddonInfo('id'))

pluginhandle = int(sys.argv[1])

########################################################
## URLs
########################################################
API_URL = 'http://%s.crackle.com/Service.svc/'
MOVIES = '/movies/all/%s/50?format=json'
SHOWS = '/shows/all/%s/50?format=json'
FEATURED = 'featured'
POPULAR = 'popular'
RECENT = 'recent'
BROWSE = 'browse/%s/full/all/alpha/%s?format=json'
BROWSE2 = 'browse/%s/all/all/alpha/%s?format=json'
SEARCHURL = 'search/all/%s/%s?format=json'
HOMESLIDE = 'slideShow/home/%s?format=json'
ORIGINALS = 'originals'
COLLECTIONS = 'collections'
CHURL = 'channel/%s/folders/%s?format=json'
BASE_MEDIA_URL = 'http://media-%s-am.crackle.com/%s_'
DETAILS_URL = 'http://%s.crackle.com/Service.svc/details/media/%s/%s?format=json'

########################################################
## Modes
########################################################
M_DO_NOTHING = 0
M_MOVIES = 10   # FEATURED
M_MOVIES_POPULAR = 11
M_MOVIES_RECENT = 12
M_SHOWS = 20    # FEATURED
M_SHOWS_POPULAR = 21
M_SHOWS_RECENT = 22
M_BROWSE = 30    # MOVIES
M_BROWSE_SHOWS = 31
M_BROWSE_ORIGINALS = 32
M_BROWSE_COLLECTIONS = 33
M_Search = 4
M_GET_VIDEO_LINKS = 5
M_PLAY = 6
M_SINGLE_VIDEO = 50

##################
## Class for items
##################
class MediaItem:
    def __init__(self):
        self.ListItem = xbmcgui.ListItem()
        self.Url = ''
        self.Mode = ''

## Get URL
def getURL(url):
    print 'CRACKLE getURL :: url = ' + url
    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;)')]
    response = opener.open(url)
    html = response.read()
    ret = {}
    ret['html'] = html
    return ret

def TestURL(url):
    print 'TestURL :: url = ' + url
    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;)')]
    try:
        usock = opener.open(url)
        usock.close()
        return True
    except:
        return False

def CountryCode():
    url = 'http://api.crackle.com/Service.svc/geo/country?format=json'
    data = cache.cacheFunction(getURL, url)
    ret = {}
    CCode = ''
    if data:
        djson = json.loads(data['html'])
        CCode = djson['CountryCode']

    ret['CCode'] = CCode

    if CCode.lower() in ['us','uk','au','ca']:
        ret['api'] = 'api'
        ret['lang'] = 'us'
    elif CCode.lower() == 'br': # brazil
        ret['api'] = 'api-br'
        ret['lang'] = 'br'
    elif CCode.lower() in ['cr','ar','uy','cl','py','pa','pe','ve','ec','co','bo','mx']: # spanish latin america
        ret['api'] = 'api-es'
        ret['lang'] = 'es'
    else:
        print "CRACKLE country code not expected: "+CCode
        ret['api'] = 'api'
        ret['lang'] = 'us'
        ret['CCode'] = 'US'

    return ret

# Remove HTML codes
def cleanHtml(dirty):
    clean = re.sub('&quot;', '\"', dirty)
    clean = re.sub('&#039;', '\'', clean)
    clean = re.sub('&#215;', 'x', clean)
    clean = re.sub('&#038;', '&', clean)
    clean = re.sub('&#8216;', '\'', clean)
    clean = re.sub('&#8217;', '\'', clean)
    clean = re.sub('&#8211;', '-', clean)
    clean = re.sub('&#8220;', '\"', clean)
    clean = re.sub('&#8221;', '\"', clean)
    clean = re.sub('&#8212;', '-', clean)
    clean = re.sub('&amp;', '&', clean)
    clean = re.sub("`", '', clean)
    clean = re.sub('<em>', '[I]', clean)
    clean = re.sub('</em>', '[/I]', clean)
    return clean

def createMediaItem(Mode,Title,Image='',Url=''):
    Title = Title.encode('utf8')
    item = MediaItem()
    item.Url = sys.argv[0] + "?url=" + urllib.quote_plus(Url) + "&mode=" + str(Mode) + "&name=" + urllib.quote_plus(Title)
    item.ListItem.setThumbnailImage(Image)
    item.ListItem.setIconImage(Image)
    item.ListItem.setLabel(Title)
    return item


########################################################
## Mode = None
## Build the main directory
########################################################
def BuildMainDirectory():
    MediaItems = []
    countryInfo = CountryCode()

    # Top Title
    MediaItems.append(createMediaItem(M_DO_NOTHING,__settings__.getLocalizedString(30011)))

    # Get featured homepage contents
    URL = (API_URL + HOMESLIDE) % (countryInfo['api'],countryInfo['CCode'])
    data = cache.cacheFunction(getURL, URL)
    #data = load_local_json('featured.json')
    items = json.loads(data['html'])
    #print items
    slideList = items['slideList']
    slideList = [slide for slide in slideList]
    #print ('slidelist length ') + str(len(slideList))
    for slide in slideList:
        #print 'Debug Msg 1'
        Url = str(slide['appDataID'])
        if Url == '0': continue
        Title = '* ' + slide['title']+ '  -  ' + slide['additionalInfo']
        Image = slide['OneSheetImage_400_600']
        if Image is None:
            Image = slide['MobileImage']
        Genre = slide['ParentChannelName']
        if not Genre:
            Genre = ''
        Plot = slide['slideDescription'].encode('utf-8')
        Mpaa = slide['Rating']
        if not Mpaa:
            Mpaa = 'None'
        NextScreen = slide['appNextScreenType']
        if NextScreen == 'VideoDetail':
            #Mediaitem.Mode = M_SINGLE_VIDEO
            #Url = DETAILS_URL % (countryInfo['api'], Url, countryInfo['CCode'])
            Url =  slide['DeepLinkingInfo']['ChannelID']
        #else:
        Url = (API_URL + CHURL) % (countryInfo['api'], Url, countryInfo['CCode'])

        Mediaitem = createMediaItem(M_GET_VIDEO_LINKS,Title,Image,Url)
        Mediaitem.ListItem.setInfo('video', { 'Title': Title, 'Plot': Plot, 'Mpaa': Mpaa, 'Genre': Genre})
        Mediaitem.ListItem.setProperty('fanart_image', slide['SlideImage_421x316'])
        MediaItems.append(Mediaitem)
        #print repr(Title) +" *** \n\n"+Url
        #print repr(slide)

    # Static Links for Browsing and Search
    main = [
        (__settings__.getLocalizedString(30012), topics_thumb, str(M_MOVIES)),
        (__settings__.getLocalizedString(30013), topics_thumb, str(M_SHOWS)),
        (__settings__.getLocalizedString(30010), programs_thumb, str(M_BROWSE)),
        (__settings__.getLocalizedString(30015), search_thumb, str(M_Search))
        ]
    for name, thumbnailImage, mode in main:
        MediaItems.append(createMediaItem(mode,name,thumbnailImage))

    addDir(MediaItems)

###########################################################
## Mode == M_Movies
## Movies Directory
###########################################################
def MoviesDirectory(mode):
    MediaItems = []
    countryInfo = CountryCode()

    if mode == M_MOVIES:
        menuTitle = __settings__.getLocalizedString(30011)
        #fname = 'moviesf.json'
        btm = [
        (__settings__.getLocalizedString(30014), topics_thumb, str(M_MOVIES_POPULAR)),
        (__settings__.getLocalizedString(30016), topics_thumb, str(M_MOVIES_RECENT))
        ]
        URL = (API_URL + FEATURED + MOVIES) % (countryInfo['api'],countryInfo['CCode'])
    elif mode == M_MOVIES_POPULAR:
        menuTitle = __settings__.getLocalizedString(30014)
        #fname = 'moviesp.json'
        btm = [
        (__settings__.getLocalizedString(30011), topics_thumb, str(M_MOVIES)),
        (__settings__.getLocalizedString(30016), topics_thumb, str(M_MOVIES_RECENT))
        ]
        URL = (API_URL + POPULAR + MOVIES) % (countryInfo['api'],countryInfo['CCode'])
    elif mode == M_MOVIES_RECENT:
        menuTitle = __settings__.getLocalizedString(30016)
        #fname = 'moviesr.json'
        btm = [
        (__settings__.getLocalizedString(30011), topics_thumb, str(M_MOVIES)),
        (__settings__.getLocalizedString(30014), topics_thumb, str(M_MOVIES_POPULAR))
        ]
        URL = (API_URL + RECENT + MOVIES) % (countryInfo['api'],countryInfo['CCode'])
    menuMode = M_DO_NOTHING
    # Top Title
    MediaItems.append(createMediaItem(menuMode,menuTitle))

    # Get featured movies contents
    data = cache.cacheFunction(getURL, URL)
    #data = load_local_json(fname)
    mjson = json.loads(data['html'])
    items = mjson['Items']
    items = [item for item in items]
    #print items
    for item in items:
        Title = '* ' + item['Title']
        Url = str(item['ID'])
        Url = (API_URL + CHURL) % (countryInfo['api'],Url,countryInfo['CCode'])
        Image = item['ImageUrl2']
        Genre = item['Genre']
        Plot = item['Description']
        Mpaa = item['Rating']
        Mediaitem = createMediaItem(M_GET_VIDEO_LINKS,Title,Image,Url)
        Mediaitem.ListItem.setInfo('video', { 'Title': Title, 'Plot': Plot, 'Mpaa': Mpaa, 'Genre': Genre})
        Mediaitem.ListItem.setProperty('fanart_image', (item['ImageUrl9'] if 'ImageUrl9' in item else ''))
        MediaItems.append(Mediaitem)

    for name, thumbnailImage, mode in btm:
        MediaItems.append(createMediaItem(mode,name,thumbnailImage))

    # Static Links for Browsing and Search
    main = [
        (__settings__.getLocalizedString(30013), topics_thumb, str(M_SHOWS)),
        (__settings__.getLocalizedString(30010), programs_thumb, str(M_BROWSE)),
        (__settings__.getLocalizedString(30015), search_thumb, str(M_Search))
        ]
    for name, thumbnailImage, mode in main:
        MediaItems.append(createMediaItem(mode,name,thumbnailImage))

    addDir(MediaItems)

###########################################################
## Mode == M_SHOWS
## SHOWS DIRECTORY
###########################################################
def ShowsDirectory(mode):
    MediaItems = []
    countryInfo = CountryCode()

    if mode == M_SHOWS:
        menuTitle = __settings__.getLocalizedString(30011)
        #fname = 'showsf.json'
        btm = [
        (__settings__.getLocalizedString(30014), topics_thumb, str(M_SHOWS_POPULAR)),
        (__settings__.getLocalizedString(30016), topics_thumb, str(M_SHOWS_RECENT))
        ]
        URL = (API_URL + FEATURED + SHOWS) % (countryInfo['api'],countryInfo['CCode'])
    elif mode == M_SHOWS_POPULAR:
        menuTitle = __settings__.getLocalizedString(30014)
        #fname = 'showsp.json'
        btm = [
        (__settings__.getLocalizedString(30011), topics_thumb, str(M_SHOWS)),
        (__settings__.getLocalizedString(30016), topics_thumb, str(M_SHOWS_RECENT))
        ]
        URL = (API_URL + POPULAR + SHOWS) % (countryInfo['api'],countryInfo['CCode'])
    elif mode == M_SHOWS_RECENT:
        menuTitle = __settings__.getLocalizedString(30016)
        #fname = 'showsr.json'
        btm = [
        (__settings__.getLocalizedString(30011), topics_thumb, str(M_SHOWS)),
        (__settings__.getLocalizedString(30014), topics_thumb, str(M_SHOWS_POPULAR))
        ]
        URL = (API_URL + RECENT + SHOWS) % (countryInfo['api'],countryInfo['CCode'])
    menuMode = M_DO_NOTHING
    # Top Title
    MediaItems.append(createMediaItem(menuMode,menuTitle))

    # Get featured movies contents
    data = cache.cacheFunction(getURL, URL)
    #data = load_local_json(fname)
    mjson = json.loads(data['html'])
    items = mjson['Items']
    items = [item for item in items]
    for item in items:
        Title = '* ' + item['Title']
        Url = str(item['ID'])
        Url = (API_URL + CHURL) % (countryInfo['api'],Url,countryInfo['CCode'])
        Image = item['ImageUrl10']
        Genre = item['Genre']
        Plot = item['Description']
        Mpaa = item['Rating']
        Mediaitem = createMediaItem(M_GET_VIDEO_LINKS,Title,Image,Url)
        Mediaitem.ListItem.setInfo('video', { 'Title': Title, 'Plot': Plot, 'Mpaa': Mpaa, 'Genre': Genre})
        Mediaitem.ListItem.setProperty('fanart_image',(item['ImageUrl9'] if 'ImageUrl9' in item else ''))
        MediaItems.append(Mediaitem)

    for name, thumbnailImage, mode in btm:
        MediaItems.append(createMediaItem(mode,name,thumbnailImage))

    # Static Links for Browsing and Search
    main = [
        (__settings__.getLocalizedString(30012), topics_thumb, str(M_MOVIES)),
        (__settings__.getLocalizedString(30010), programs_thumb, str(M_BROWSE)),
        (__settings__.getLocalizedString(30015), search_thumb, str(M_Search))
        ]
    for name, thumbnailImage, mode in main:
        MediaItems.append(createMediaItem(mode,name,thumbnailImage))

    addDir(MediaItems)


###########################################################
## Mode == M_BROWSE
## BROWSE DIRECTORY
###########################################################
def BrowseDirectory(mode):
    MediaItems = []
    countryInfo = CountryCode()

    if mode == M_BROWSE:
        menuTitle = __settings__.getLocalizedString(30012)
        #fname = 'browsem.json'
        btm = [
        (__settings__.getLocalizedString(30017), topics_thumb, str(M_BROWSE_SHOWS)),
        (__settings__.getLocalizedString(30018), topics_thumb, str(M_BROWSE_ORIGINALS)),
        (__settings__.getLocalizedString(30019), topics_thumb, str(M_BROWSE_COLLECTIONS))
        ]
        URL = (API_URL + BROWSE) % (countryInfo['api'] ,'movies', countryInfo['CCode'])
    elif mode == M_BROWSE_SHOWS:
        menuTitle = __settings__.getLocalizedString(30017)
        #fname = 'browset.json'
        btm = [
        (__settings__.getLocalizedString(30012), topics_thumb, str(M_BROWSE)),
        (__settings__.getLocalizedString(30018), topics_thumb, str(M_BROWSE_ORIGINALS)),
        (__settings__.getLocalizedString(30019), topics_thumb, str(M_BROWSE_COLLECTIONS))
        ]
        URL = (API_URL + BROWSE) % (countryInfo['api'] ,'television', countryInfo['CCode'])
    elif mode == M_BROWSE_ORIGINALS:
        menuTitle = __settings__.getLocalizedString(30018)
        #fname = 'browseo.json'
        btm = [
        (__settings__.getLocalizedString(30012), topics_thumb, str(M_BROWSE)),
        (__settings__.getLocalizedString(30017), topics_thumb, str(M_BROWSE_SHOWS)),
        (__settings__.getLocalizedString(30019), topics_thumb, str(M_BROWSE_COLLECTIONS))
        ]
        URL = (API_URL + BROWSE2) % (countryInfo['api'] ,'originals', countryInfo['CCode'])
    elif mode == M_BROWSE_COLLECTIONS:
        menuTitle = __settings__.getLocalizedString(30019)
        #fname = 'browsec.json'
        btm = [
        (__settings__.getLocalizedString(30012), topics_thumb, str(M_BROWSE)),
        (__settings__.getLocalizedString(30017), topics_thumb, str(M_BROWSE_SHOWS)),
        (__settings__.getLocalizedString(30018), topics_thumb, str(M_BROWSE_ORIGINALS))
        ]
        URL = (API_URL + BROWSE2) % (countryInfo['api'] ,'collections', countryInfo['CCode'])
    menuMode = M_DO_NOTHING
    # Top Title
    MediaItems.append(createMediaItem(menuMode,menuTitle))

    # Get featured movies contents
    data = cache.cacheFunction(getURL, URL)
    #print data
    #data = load_local_json(fname)
    mjson = json.loads(data['html'])
    items = mjson['Entries']
    items = [item for item in items]
    for item in items:
        #print item
        Title = '* ' + item['Name']
        #print Title
        Url = str(item['ID'])
        Url = (API_URL + CHURL) % (countryInfo['api'] ,Url, countryInfo['CCode'])
        #print Url
        Image = item['ChannelArtTileLarge']
        Genre = item['Genre']
        Plot = item['Description']
        Year = item['ReleaseYear']
        Mpaa = item['Rating']
        Mediaitem = createMediaItem(M_GET_VIDEO_LINKS,Title,Image,Url)
        Mediaitem.ListItem.setInfo('video', { 'Title': Title, 'Plot': Plot, 'Mpaa': Mpaa,  'Genre': Genre, 'Year': Year})
        Mediaitem.ListItem.setProperty('fanart_image', (item['ChannelImage_432x243'] if item['ChannelImage_432x243'] != '' else item['ChannelArtLandscape'] ))
        MediaItems.append(Mediaitem)

    for name, thumbnailImage, mode in btm:
        MediaItems.append(createMediaItem(mode,name,thumbnailImage))

    # Static Links for Browsing and Search
    main = [
        (__settings__.getLocalizedString(30012), topics_thumb, str(M_MOVIES)),
        (__settings__.getLocalizedString(30013), topics_thumb, str(M_SHOWS)),
        (__settings__.getLocalizedString(30015), search_thumb, str(M_Search))
        ]
    for name, thumbnailImage, mode in main:
        MediaItems.append(createMediaItem(mode,name,thumbnailImage))

    addDir(MediaItems)


###########################################################
## Mode == M_GET_VIDEO_LINKS
## Try to get a list of playable items and play it.
###########################################################
def Playlist(URL):
    print "CRACKLE Playlist "+URL

    path_pattern = re.compile('http:\\/\\/.+?\/(.+?)_[a-zA-Z0-9]+')

    MediaItems = []
    countryInfo = CountryCode()
    sub_url = ''
    #URL = API_URL + CHURL % url
    data = cache.cacheFunction(getURL, URL)
    #data = load_local_json('chdet3.json')
    mjson = json.loads(data['html'])

    Count = mjson['Count']
    if Count < 1:
        dialog = xbmcgui.Dialog()
        dialog.ok('No Item', 'The selected item does not exist any more.')
        return

    FolderList = mjson['FolderList']
    FolderList = [folder for folder in FolderList]
    for folder in FolderList:
    #folder = FolderList[0]:
      PlaylistList = folder['PlaylistList']
      PlaylistList = [playlist for playlist in PlaylistList]
    #playlist = PlaylistList[0]
      for playlist in PlaylistList:
         print playlist['Name']+" #### "+repr(playlist['LockedToChannel'])
         if not playlist['LockedToChannel']: continue
         MediaList = playlist['MediaList']
         MediaList = [media for media in MediaList]
         count = 0
         #print MediaList
         for item in MediaList:
            Title = item['Title']
            HackUrl = item['Thumbnail_Wide']
            print HackUrl
            print item['ClosedCaptionFiles']
            #Path = re.compile('http://.+?\/(.+?)_.+?').findall(HackUrl)[0]
            Path = path_pattern.findall(HackUrl)
            if not Path and item['ClosedCaptionFiles']:
               Path = path_pattern.findall(item['ClosedCaptionFiles'][0]['Path'])
            if not Path:
               print "CRACLE no url details found"
               continue
            Url = BASE_MEDIA_URL % (countryInfo['lang'],Path[0])
            Image = item['Thumbnail_Large208x156']
            Genre = item['Genre']
            Plot = item['Description']
            Mpaa = item['Rating']
            Duration = int(item['DurationInSeconds'])/60
            Subtitle = item['ClosedCaptionFiles']

            Mediaitem = createMediaItem(M_PLAY,Title,Image,Url)

            if Subtitle:
                #print "\n############### FOUND SUBTITLES \n############## "+Subtitle[0]['Path']
                sub_url = Subtitle[0]['Path']
                Mediaitem.Url = Mediaitem.Url + "&sub="+urllib.quote_plus(sub_url)

            Mediaitem.ListItem.setInfo('video', { 'Title': Title, 'Plot': Plot, 'Mpaa': Mpaa,'Genre': Genre, 'Duration': Duration})
            Mediaitem.ListItem.setProperty('fanart_image',(item['ChannelImage_432x243'] if item['ChannelImage_432x243'] != '' else item['ThumbnailExternal'] ))
            #Mediaitem.ListItem.setProperty('IsPlayable', 'true')
            MediaItems.append(Mediaitem)
            count += 1

    if count < 1:
        return

    if count == 1:
        Play(Url, Mediaitem.ListItem, sub_url)
    else:
        addDir(MediaItems)


def VideoDetails(URL):
    print "CRACKLE VideoDetails "+URL
    ###########################################################
    ## Mode == M_SINGLE_VIDEO
    ## Try to get a playable item and play it.
    ###########################################################

    path_pattern = re.compile('http:\\/\\/.+?\/(.+?)_[a-zA-Z0-9]+')

    MediaItems = []
    countryInfo = CountryCode()
    sub_url = ''

    data = cache.cacheFunction(getURL, URL)
    #data = load_local_json('chdet3.json')
    mjson = json.loads(data['html'])
    Title = mjson['Title']
    HackUrl = mjson['Thumbnail_Wide']
    #print HackUrl
    #Path = re.compile('http://.+?\/(.+?)_.+?').findall(HackUrl)[0]
    Path = path_pattern.findall(HackUrl)[0]
    Url = BASE_MEDIA_URL % (countryInfo['lang'], Path)
    #print mjson
    Image = mjson['Thumbnail_Large208x156']
    Genre = mjson['Genre']
    Plot = mjson['Description']
    Mpaa = mjson['Rating']
    Duration = int(mjson['DurationInSeconds'])/60
    Subtitle = mjson['ClosedCaptionFiles']

    Mediaitem = createMediaItem(M_PLAY,Title,Image,Url)
    Mediaitem.ListItem.setInfo('video', { 'Title': Title, 'Plot': Plot, 'Mpaa': Mpaa, 'Genre': Genre, 'Duration': Duration})
    #Mediaitem.ListItem.setProperty('fanart_image', mjson['SlideImage_421x316'])
    #Mediaitem.ListItem.setProperty('IsPlayable', 'true')

    if Subtitle:
         sub_url = Subtitle[0]['Path']
         Mediaitem.Url = Mediaitem.Url + "&sub="+urllib.quote_plus(sub_url)

    MediaItems.append(Mediaitem)
    addDir(MediaItems)
    Play(Url, Mediaitem.ListItem, sub_url)


def Play(url, litem=False, subtitles_url='', name=''):
    if url is not None and url != '':
        #try:
            Url = url + '480p_1mbps.mp4'
            if not TestURL(Url):
                Url = url + '480p.mp4'
                if not TestURL(Url):
                    Url = url + '360p.mp4'
            playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            playList.clear()
            if not litem:
                litem=xbmcgui.ListItem(name)
                litem.setInfo( type="video",  infoLabels = {'title' : name })
            litem.setProperty('mimetype','video/mp4') # improve loading time
            playList.add(Url,litem)
            xbmcPlayer = xbmc.Player()
            xbmcPlayer.play(playList)

            if subtitles_url:
                while not xbmcPlayer.isPlaying():
                    xbmc.sleep(100) #wait until video is being played
                try:
                    xbmc.sleep(1000)
                    import SubtitleControl
                    SC = SubtitleControl.SubtitleControl(xbmc.translatePath("special://userdata"))
                    subtitleFile = SC.saveSubtitle(getURL(subtitles_url)['html'])
                    xbmc.sleep(1000)
                    xbmcPlayer.setSubtitles(subtitleFile) #set subtitle
                except Exception as inst:
                    print "ERROR loading subtitles "+str(subtitles_url), inst

            playList.clear()
            #vid = xbmcgui.ListItem(path=url)
            #xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(url, vid)
            #xbmc.executebuiltin("xbmc.PlayMedia("+url+")")
        #except:
        #    print 'Exception while trying to play'

# Set View Mode selected in the setting
def SetViewMode():
    try:
        # if (xbmc.getSkinDir() == "skin.confluence"):
        if __settings__.getSetting('view_mode') == "1": # List
            xbmc.executebuiltin('Container.SetViewMode(502)')
        if __settings__.getSetting('view_mode') == "2": # Big List
            xbmc.executebuiltin('Container.SetViewMode(51)')
        if __settings__.getSetting('view_mode') == "3": # Thumbnails
            xbmc.executebuiltin('Container.SetViewMode(500)')
        if __settings__.getSetting('view_mode') == "4": # Poster Wrap
            xbmc.executebuiltin('Container.SetViewMode(501)')
        if __settings__.getSetting('view_mode') == "5": # Fanart
            xbmc.executebuiltin('Container.SetViewMode(508)')
        if __settings__.getSetting('view_mode') == "6":  # Media info
            xbmc.executebuiltin('Container.SetViewMode(504)')
        if __settings__.getSetting('view_mode') == "7": # Media info 2
            xbmc.executebuiltin('Container.SetViewMode(503)')
        if __settings__.getSetting('view_mode') == "0": # Media info for Quartz?
            xbmc.executebuiltin('Container.SetViewMode(52)')
    except:
        print "SetViewMode Failed: " + __settings__.getSetting('view_mode')
        print "Skin: " + xbmc.getSkinDir()

# Search documentaries
def SEARCH(url):
    MediaItems = []
    countryInfo = CountryCode()

    if url is None or url == '':
        keyb = xbmc.Keyboard('', 'Search Crackle')
        keyb.doModal()
        if (keyb.isConfirmed() == False):
            return
        search = keyb.getText()
        if search is None or search == '':
            return
        #search = search.replace(" ", "+")
        encSrc = urllib.quote(search)
        url = (API_URL + SEARCHURL) % (countryInfo['api'], encSrc, countryInfo['CCode'])

    data = cache.cacheFunction(getURL, url)
    mjson = json.loads(data['html'])
    count = mjson['Count']
    if count < 1:
        return
    items = mjson['Items']
    items = [item for item in items]
    #print repr(items)
    for item in items:
        Title = item['Title']
        Url = str(item['ID'])
        Url = (API_URL + CHURL) % (countryInfo['api'],Url,countryInfo['CCode'])
        Image = item['ImageUrl2']
        Genre = item['Genre']
        Plot = item['Description']#+"\nWhy It Clrackles: "+cleanHtml(item['WhyItCrackles'])
        Mpaa = item['Rating']
        Mediaitem = createMediaItem(M_GET_VIDEO_LINKS,Title,Image,Url)
        Mediaitem.ListItem.setInfo('video', { 'Title': Title, 'Plot': Plot, 'Mpaa': Mpaa, 'Genre': Genre})
        Mediaitem.ListItem.setProperty('fanart_image',(item['ChannelImage_432x243'] if item['ChannelImage_432x243'] != '' else item['ImageUrl9'] ))
        MediaItems.append(Mediaitem)

    addDir(MediaItems)


## Get Parameters
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

def addDir(Listitems):
    if Listitems is None:
        return
    Items = []
    for Listitem in Listitems:
        #print repr(Listitem.Url)
        Item = Listitem.Url, Listitem.ListItem, True
        Items.append(Item)
    xbmcplugin.addDirectoryItems(pluginhandle, Items)
    xbmcplugin.endOfDirectory(pluginhandle)
    ## Set Default View Mode. This might break with different skins. But who cares?
    SetViewMode()

params = get_params()
url = None
name = None
mode = None
titles = None
subtitles = None

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
        titles = urllib.unquote_plus(params["titles"])
except:
        pass
try:
        sub = urllib.unquote_plus(params["sub"])
except:
        sub = ''

xbmc.log("CRACKLE Mode: " + str(mode))
#print "URL: " + str(url)
#print "Name: " + str(name)
#print "Title: " + str(titles)

# set content type so library shows more views and info
xbmcplugin.setContent(pluginhandle, 'movies')

if mode == None: #or url == None or len(url) < 1:
    #print "Top Directory"
    BuildMainDirectory()
elif mode == M_DO_NOTHING:
    print 'CRACKLE Doing Nothing'
elif mode == M_Search:
    #print "SEARCH  :" + url
    SEARCH(url)
elif mode == M_MOVIES or mode == M_MOVIES_POPULAR or mode == M_MOVIES_RECENT:
    MoviesDirectory(mode)
elif mode == M_SHOWS or mode == M_SHOWS_POPULAR or mode == M_SHOWS_RECENT:
    ShowsDirectory(mode)
elif mode == M_BROWSE or mode == M_BROWSE_SHOWS or mode == M_BROWSE_ORIGINALS or mode == M_BROWSE_COLLECTIONS:
    BrowseDirectory(mode)
elif mode == M_GET_VIDEO_LINKS:
    Playlist(url)
elif mode == M_SINGLE_VIDEO:
    VideoDetails(url)
elif mode == M_PLAY:
    #print "CRACKLE play "+url
    Play(url,subtitles_url=sub,name=name)
