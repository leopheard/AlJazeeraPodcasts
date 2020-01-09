from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL1 = "http://aljazeera-eng-apple-live.adaptive.level3.net/apple/aljazeera/english/160audio.m3u8" #LIVE-AUDIO-ENGLISH
#URL2 = "https://english.streaming.aljazeera.net/aljazeera/english2/index576_07370.ts" #LIVE-VIDEO-ENGLISH
URL2 = "http://aljazeera-eng-apple-live.adaptive.level3.net/apple/aljazeera/english/160audio/160_040219_020939_1599111.aac" #ALT-VIDEO
URL3 = "http://feeds.soundcloud.com/users/soundcloud:users:338760306/sounds.rss" #ALL-JETTY-NETWORK
URL4 = "http://feeds.aljazeera.net/podcasts/101eastHD" #101-EAST
URL5 = "http://feeds.aljazeera.net/podcasts/aljazeeracorrespondentHD" #AJ-CORRESPONDENT
URL6 = "http://feeds.aljazeera.net/podcasts/featureddocumentariesHD" #AJ-DOC
URL22 = "https://rss.art19.com/al-jazeera-investigates" #AJ-INVESTIGATES
URL7 = "http://feeds.aljazeera.net/podcasts/aljazeeraworldHD" #AJ-WORLD
URL8 = "https://rss.art19.com/al-jazeera-your-world" #AJ-YOURWORLD
URL9 = "http://feeds.aljazeera.net/podcasts/countingthecostAU" #COUNTING-THE-COST
URL10 = "https://audioboom.com/channels/4922429.rss" #THE-DEBRIEF
URL11 = "https://rss.art19.com/game-of-our-lives" #GAME-OF-OUR-LIVES
URL12 = "http://feeds.aljazeera.net/podcasts/headtoheadAU" #HEAD-TO-HEAD
URL13 = "http://feeds.aljazeera.net/podcasts/insidestoryAU" #INSIDE-STORY
URL14 = "http://feeds.aljazeera.net/podcasts/peopleandpowerHD" #PEOPLE-POWER
URL15 = "http://feeds.aljazeera.net/podcasts/talktoaljazeeraHD" #TALKTOAJ
URL16 = "http://feeds.aljazeera.net/podcasts/techknowHD" #TECH-KNOW
URL17 = "http://feeds.aljazeera.net/podcasts/listeningpostAU" #THE-LISTENING-POST
URL18 = "http://feeds.aljazeera.net/podcasts/thestreamaudio" #THE-STREAM
URL19 = "https://rss.art19.com/the-take" #THE-TAKE
URL20 = "http://feeds.aljazeera.net/podcasts/upfrontAU" #UPFRONT
URL21 = "http://feeds.aljazeera.net/podcasts/witnessHD" #WITNESS

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': "http://aljazeera-eng-apple-live.adaptive.level3.net/apple/aljazeera/english/160audio.m3u8",
            'thumbnail': "https://duckduckgo.com/i/7a6abcc2.png",
            'is_playable': True},
   {
            'label': plugin.get_string(30002), 
            'path': "https://english.streaming.aljazeera.net/aljazeera/english2/index576_07370.ts",
            'thumbnail': "https://www.aljazeera.com/assets/images/aj-logo-lg-124.png",
            'is_playable': True},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://i1.sndcdn.com/avatars-000365237387-f0k2ci-original.jpg"},
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2014/10/26/8e067a0f8b304217b468cbef6d3b28b3_18.jpg"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2014/10/26/e0c2ca23a1a54c07b827104aa57ada83_18.jpg"},
        {
            'label': plugin.get_string(30006),
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2011/11/2/20111121156257797_20.jpg"},
        {
            'label': plugin.get_string(30022),
            'path': plugin.url_for('episodes22'),
            'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Podcasts123/v4/3d/f4/23/3df42350-844e-8e08-264e-b26c2dc97d3d/mza_17312054508823443213.jpeg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30007),
            'path': plugin.url_for('episodes7'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2014/10/26/beefc69a4b0d4b6aac13938ee98f0103_18.jpg"},
        {
            'label': plugin.get_string(30008),
            'path': plugin.url_for('episodes8'),
            'thumbnail': "https://content.production.cdn.art19.com/images/fe/0f/7b/ab/fe0f7bab-cb97-48aa-bd74-40b01672b318/1dacf16442ed4c4784afb1c456855f18ba15dadfc5e4da9e46df8c9075a9bbeae716b7f2cfcb7c3cc3ce53d8c906f24279a8f8a738f554c3263ecc00ee275d36.jpeg"},
        {
            'label': plugin.get_string(30009),
            'path': plugin.url_for('episodes9'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2014/10/26/306b83e403044e08a885ed6de19499e3_18.jpg"},
        {
            'label': plugin.get_string(30010),
            'path': plugin.url_for('episodes10'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2017/8/27/35c83b0e839047f7901d5d939450d199_18.jpg"},
        {
            'label': plugin.get_string(30011),
            'path': plugin.url_for('episodes11'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2018/3/15/3ce79cc3f72d47c399210733a7f64a67_18.jpg"},
        {
            'label': plugin.get_string(30012),
            'path': plugin.url_for('episodes12'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2014/10/26/3bb4d9be598a4521a13575ac20a49a59_18.jpg"},
        {
            'label': plugin.get_string(30013),
            'path': plugin.url_for('episodes13'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2014/10/26/71fd4736163a411a88d01bfb9b65c601_18.jpg"},
        {
            'label': plugin.get_string(30014),
            'path': plugin.url_for('episodes14'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2014/10/26/53be074342184ff989d7de2b1e784941_18.jpg"},
        {
            'label': plugin.get_string(30015),
            'path': plugin.url_for('episodes15'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2014/10/26/ef823a58504c4e87aea5d433502fa5b5_18.jpg"},
        {
            'label': plugin.get_string(30016),
            'path': plugin.url_for('episodes16'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2014/11/11/8a0e1868d6774cc0ae67a260a852f498_18.jpg"},
        {
            'label': plugin.get_string(30017),
            'path': plugin.url_for('episodes17'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2014/10/26/3234a2b34a644e11ad4a06b7c9ef98f6_18.jpg"},
        {
            'label': plugin.get_string(30018),
            'path': plugin.url_for('episodes18'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2011/5/31/2011531843277371_20.jpg"},
        {
            'label': plugin.get_string(30019),
            'path': plugin.url_for('episodes19'),
            'thumbnail': "https://www.aljazeera.com/mritems/Images/2018/11/18/dca00d429cf44dce88f92dbb3cdbf077_6.jpg"},
        {
            'label': plugin.get_string(30020),
            'path': plugin.url_for('episodes20'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2015/8/17/1f735ca175bd440d9f36e154be17633d_18.jpg"},
        {
            'label': plugin.get_string(30021),
            'path': plugin.url_for('episodes21'),
            'thumbnail': "https://www.aljazeera.com/mritems/imagecache/mbdresplarge/mritems/Images/2014/10/26/04cca55fea2247b2a15d32ca7227291c_18.jpg"},
   ]
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(URL3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(URL4)
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items

@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(URL5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items

@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(URL6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items

@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(URL7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7)
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items

@plugin.route('/episodes8/')
def episodes8():
    soup8 = mainaddon.get_soup8(URL8)
    playable_podcast8 = mainaddon.get_playable_podcast8(soup8)
    items = mainaddon.compile_playable_podcast8(playable_podcast8)
    return items

@plugin.route('/episodes9/')
def episodes9():
    soup9 = mainaddon.get_soup9(URL9)
    playable_podcast9 = mainaddon.get_playable_podcast9(soup9)
    items = mainaddon.compile_playable_podcast9(playable_podcast9)
    return items

@plugin.route('/episodes10/')
def episodes10():
    soup10 = mainaddon.get_soup10(URL10)
    playable_podcast10 = mainaddon.get_playable_podcast10(soup10)
    items = mainaddon.compile_playable_podcast10(playable_podcast10)
    return items

@plugin.route('/episodes11/')
def episodes11():
    soup11 = mainaddon.get_soup11(URL11)
    playable_podcast11 = mainaddon.get_playable_podcast11(soup11)
    items = mainaddon.compile_playable_podcast11(playable_podcast11)
    return items

@plugin.route('/episodes12/')
def episodes12():
    soup12 = mainaddon.get_soup12(URL12)
    playable_podcast12 = mainaddon.get_playable_podcast12(soup12)
    items = mainaddon.compile_playable_podcast12(playable_podcast12)
    return items

@plugin.route('/episodes13/')
def episodes13():
    soup13 = mainaddon.get_soup13(URL13)
    playable_podcast13 = mainaddon.get_playable_podcast13(soup13)
    items = mainaddon.compile_playable_podcast13(playable_podcast13)
    return items

@plugin.route('/episodes14/')
def episodes14():
    soup14 = mainaddon.get_soup14(URL14)
    playable_podcast14 = mainaddon.get_playable_podcast14(soup14)
    items = mainaddon.compile_playable_podcast14(playable_podcast14)
    return items

@plugin.route('/episodes15/')
def episodes15():
    soup15 = mainaddon.get_soup15(URL15)
    playable_podcast15 = mainaddon.get_playable_podcast15(soup15)
    items = mainaddon.compile_playable_podcast15(playable_podcast15)
    return items

@plugin.route('/episodes16/')
def episodes16():
    soup16 = mainaddon.get_soup16(URL16)
    playable_podcast16 = mainaddon.get_playable_podcast16(soup16)
    items = mainaddon.compile_playable_podcast16(playable_podcast16)
    return items

@plugin.route('/episodes17/')
def episodes17():
    soup17 = mainaddon.get_soup17(URL17)
    playable_podcast17 = mainaddon.get_playable_podcast17(soup17)
    items = mainaddon.compile_playable_podcast17(playable_podcast17)
    return items

@plugin.route('/episodes18/')
def episodes18():
    soup18 = mainaddon.get_soup18(URL18)
    playable_podcast18 = mainaddon.get_playable_podcast18(soup18)
    items = mainaddon.compile_playable_podcast18(playable_podcast18)
    return items

@plugin.route('/episodes19/')
def episodes19():
    soup19 = mainaddon.get_soup19(URL19)
    playable_podcast19 = mainaddon.get_playable_podcast19(soup19)
    items = mainaddon.compile_playable_podcast19(playable_podcast19)
    return items

@plugin.route('/episodes20/')
def episodes20():
    soup20 = mainaddon.get_soup20(URL20)
    playable_podcast20 = mainaddon.get_playable_podcast20(soup20)
    items = mainaddon.compile_playable_podcast20(playable_podcast20)
    return items

@plugin.route('/episodes21/')
def episodes21():
    soup21 = mainaddon.get_soup21(URL21)
    playable_podcast21 = mainaddon.get_playable_podcast21(soup21)
    items = mainaddon.compile_playable_podcast21(playable_podcast21)
    return items

@plugin.route('/episodes22/')
def episodes22():
    soup22 = mainaddon.get_soup22(URL22)
    playable_podcast22 = mainaddon.get_playable_podcast22(soup22)
    items = mainaddon.compile_playable_podcast22(playable_podcast22)
    return items

if __name__ == '__main__':
    plugin.run()
