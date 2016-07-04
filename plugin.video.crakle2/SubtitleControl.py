
import sys
import os.path
import CommonFunctions as common


class SubtitleControl():


    def __init__(self, path):
        self.subtitle_file = os.path.join(path,'subtitles.ssa')


    def saveSubtitle(self, result):
        result = self.transformSubtitleXMLtoSRT(result)

        w = open(self.subtitle_file, 'w')
        try:
            w.write(result.encode("utf-8")) # WTF, didn't have to do this before, did i?
        except:
            w.write(result)
            print "NOT utf-8 WRITE!!!: " + filename + " - " + repr(result)
            time.sleep(20)
        w.flush()
        w.close()
        return self.subtitle_file


    def simpleReplaceHTMLCodes(self, str):
        str = str.strip()
        str = str.replace("&amp;", "&")
        str = str.replace("&quot;", '"')
        str = str.replace("&hellip;", "...")
        str = str.replace("&gt;", ">")
        str = str.replace("&lt;", "<")
        str = str.replace("&#39;", "'")
        str = str.replace("<br/>", "\\N")
        str = str.replace("<br />", "\\N")
        str = str.replace('<span tts:fontStyle="italic">', '{\\i1}')
        str = str.replace('</span>', '')
        return str


    def transformSubtitleXMLtoSRT(self, xml):

        result = u""
        dialogues = common.parseDOM(xml, "p")
        starts = common.parseDOM(xml, "p", ret = "begin")
        ends = common.parseDOM(xml, "p", ret = "end")
        count = 0
        for node in dialogues:
            text = self.simpleReplaceHTMLCodes(node)

            result += "Dialogue: Marked=%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\r\n" % ("0", starts[count][1:8]+".00", ends[count][1:8]+".00", "Default", "Name", "0000", "0000", "0000", "", text)

            count = count+1

        result = "[Script Info]\r\n; This is a Sub Station Alpha v4 script.\r\n; For Sub Station Alpha info and downloads,\r\n; go to http://www.eswat.demon.co.uk/\r\n; or email kotus@eswat.demon.co.uk\r\nTitle: Auto Generated\r\nScriptType: v4.00\r\nCollisions: Normal\r\nPlayResY: 1280\r\nPlayResX: 800\r\n\r\n[V4 Styles]\r\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, TertiaryColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, AlphaLevel, Encoding\r\nStyle: Default,Arial,80,&H00FFFFFF&,65535,65535,&00000000&,-1,0,1,3,2,2,0,0,0,0,0\r\nStyle: speech,Arial,60,0,65535,65535,&H4BFFFFFF&,0,0,3,1,0,1,0,0,0,0,0\r\nStyle: popup,Arial,60,0,65535,65535,&H4BFFFFFF&,0,0,3,3,0,1,0,0,0,0,0\r\nStyle: highlightText,Wolf_Rain,60,15724527,15724527,15724527,&H4BFFFFFF&,0,0,1,1,2,2,5,5,0,0,0\r\n[Events]\r\nFormat: Marked, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\r\n" + result
        result += "Dialogue: Marked=0,0:00:0.00,0:00:0.00,Default,Name,0000,0000,0000,,\r\n"

        return result
