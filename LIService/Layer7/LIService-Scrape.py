import requests
import os
import subprocess
import random
import re
import threading
import urllib.request
import argparse
import sys
from colorama import Fore, Back, Style, init
from time import time

init(autoreset=True)

output_file = 'proxy.txt'
os.system('cls' if os.name == 'nt' else 'clear')

if os.path.isfile(output_file):
    os.remove(output_file)
    print(f"""
                    █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
                    █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
             ╚╦═════════════════════════════════════════════╦╝
           ╔══╩═════════════════════════════════════════════╩═══╗
            LIService Panel DDoS | Development By t.me/LIService 
           ╚══╦══════════════════════════════════════════════╦══╝
              ╚══════════════════════════════════════════════╝
              
""")


proxy_urls = [
'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all',
'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all',
'https://www.sslproxies.org',
'https://www.proxyscan.io',
'https://spys.one/en/https-ssl-proxy',
'https://spys.one/en/socks-proxy-list',
'https://www.proxy-list.download/HTTPS',
'https://www.proxy-list.download/SOCKS4',
'https://www.proxy-list.download/SOCKS5',
'https://premiumproxy.net/https-ssl-proxy-list',
'https://premiumproxy.net/http-proxy-list',
'https://premiumproxy.net/socks-proxy-list',
'https://premiumproxy.net/distorting-proxy-list',
'https://premiumproxy.net/web-proxy-list',
'http://free-proxy.cz/en/proxylist/country/all/socks5/ping/all',
'http://free-proxy.cz/en/proxylist/country/all/https/ping/all',
'http://free-proxy.cz/en/proxylist/country/all/socks4/ping/all',
'https://www.socks-proxy.net/',
'https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc',
'http://spys.one/en',
'https://openproxy.space/list/http',
'http://free-proxy.cz/en/',
'https://www.freeproxylists.net/',
'http://0dayproxies.blogspot.com/feeds/posts/default?alt=rss',
'http://1000freeanonymousproxy.blogspot.com/feeds/posts/default?alt=rss',
'http://100filmovru.blog.fc2.com/',
'http://100proxygratis.blogspot.com/feeds/posts/default?alt=rss',
'http://123proxies.blogspot.com/',
'http://139239123912391.my1.ru/',
'http://1viraldata.blogspot.com/feeds/posts/default?alt=rss',
'http://2013-proxy-list.blogspot.com/feeds/posts/default?alt=rss',
'http://24hourshacking.blogspot.com/feeds/posts/default?alt=rss',
'http://2freesocks5list.blogspot.com/feeds/posts/default?alt=rss',

'http://31f.cn/http-proxy/',
'http://31f.cn/https-proxy/',
'http://31f.cn/socks-proxy/',
'http://www.3464.com/data/Proxy/Http/',
'http://www.3464.com/data/Proxy/Socks5/',
'http://3doyunindir.blogspot.com/feeds/posts/default?alt=rss',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://www.proxyscan.io/download?type=socks4',
'https://www.proxyscan.io/download?type=http',
'https://www.proxyscan.io/download?type=https',
'https://www.proxyscan.io/download?type=socks5',
'https://www.sslproxies.org/',
'https://spys.one/en/https-ssl-proxy/',
'https://spys.one/en/socks-proxy-list/',
'https://www.proxy-list.download/HTTPS',
'https://www.proxy-list.download/SOCKS4',
'https://www.proxy-list.download/SOCKS5',
'https://premiumproxy.net/https-ssl-proxy-list',
'https://premiumproxy.net/http-proxy-list',
'https://premiumproxy.net/socks-proxy-list',
'https://premiumproxy.net/distorting-proxy-list',
'https://premiumproxy.net/web-proxy-list',
'http://free-proxy.cz/en/proxylist/country/all/socks5/ping/all',
'http://free-proxy.cz/en/proxylist/country/all/https/ping/all',
'http://free-proxy.cz/en/proxylist/country/all/socks4/ping/all',
'https://sockslist.net/',
'https://www.socks-proxy.net/',
'https://geonode.com/free-proxy-list',
'https://www.scraperapi.com',
'http://spys.one/en',
'https://openproxy.space/list',
'http://free-proxy.cz/en',
'https://proxyscrape.com/free-proxy-list',
'http://www.freeproxylists.net',
'https://www.sslproxies.org',
'http://gatherproxy.com',
'http://www.004388.com/ip/index_2.html',
'http://www.004388.com/ippt/index_2.html',
'http://www.004388.com/ipgw/index_2.html',
'http://www.004388.com/ipgwtm/index_2.html',
'http://www.004388.com/socks/index_2.html',
'http://www.004388.com/ip/',
'http://www.004388.com/ippt/',
'http://www.004388.com/ipgw/',
'http://www.004388.com/ipgwtm/',
'http://www.004388.com/socks/',
'http://01hitfaker.blogspot.com/feeds/posts/default?alt=rss',
'http://0dayproxies.blogspot.com/feeds/posts/default?alt=rss',
'http://1000freeanonymousproxy.blogspot.com/feeds/posts/default?alt=rss',
'http://100filmovru.blog.fc2.com/',
'http://100proxygratis.blogspot.com/feeds/posts/default?alt=rss',
'https://1110111.com/forumdisplay.php?fid=78',
'http://123proxies.blogspot.com/',
'http://1337spam.blogspot.com/feeds/posts/default?alt=rss',
'http://139239123912391.my1.ru/',
'http://13i13.blogspot.com/feeds/posts/default?alt=rss',
'http://174.139.241.42/1.txt',
'http://174.139.241.42/yahoo/lists/check_report.txt',
'http://185.81.158.218/http.txt',
'http://www.1887.sd.cn/xw/index.asp?id=1&page=1',
'http://1db2.in/?s=proxy',
'http://www.1tzc.com/shenbodaili/',
'http://1viraldata.blogspot.com/feeds/posts/default?alt=rss',
'http://2013-proxy-list.blogspot.com/feeds/posts/default?alt=rss',
'http://22xxbb.lofter.com/',
'http://24hourshacking.blogspot.com/feeds/posts/default?alt=rss',
'http://2freesocks5list.blogspot.com/feeds/posts/default?alt=rss',
'http://31f.cn/http-proxy/',
'http://31f.cn/https-proxy/',
'http://31f.cn/socks-proxy/',
'http://www.3464.com/data/Proxy/Http/',
'http://www.3464.com/data/Proxy/Socks5/',
'http://3doyunindir.blogspot.com/feeds/posts/default?alt=rss',
'https://www.3gmfw.cn/article/html2/list/467/1.html',
'http://www.3stuff.site/category/free-proxy/feed/',
'http://3xdr.blogspot.com/feeds/posts/default?alt=rss',
'http://3zun.com/',
'http://4r.ketnoitatca.net/showthread.php/170890-Share-Proxy-server-Proxies-list-update-daily/page9999999',
'http://4youngsterz.blogspot.com/feeds/posts/default?alt=rss',
'http://50kproxies.com/category/proxy-list/',
'http://www.51140.net/proxy/',
'http://55face.blogspot.com',
'http://64box.blogspot.com/feeds/posts/default?alt=rss',
'http://www.66ip.cn/mo.php?tqsl=1000',
'http://www.6brj.com/free',
'http://7519llsz.cn/llsz/av7xc7b7d9j7x3a2s6f54g.txt',
'http://7proxy.blogspot.com/feeds/posts/default?alt=rss',
'http://www.89ip.cn/tiqu.php?sxb=&tqsl=3000&ports=&ktip=&xl=on&submit=%CC%E1++%C8%A1',
'http://8proxy.blogspot.com/feeds/posts/default?alt=rss',
'http://98.126.108.155/1.txt',
'http://98.126.108.155/google/lists/check_report.txt',
'http://98.126.108.155/yahoo/lists/check_report.txt',
'http://98.126.108.155/yahoo/tmp/sortspeed.txt',
'http://98.126.61.179/yahoo/lists/check_report.txt',
'http://98.126.61.179/1.txt',
'http://aa8.narod.ru/index/0-11',
'http://aa8.narod.ru/index/0-10',
'http://aa8.narod.ru/index/0-9',
'http://aa8.narod.ru/index/0-8',
'http://ab57.ru/downloads/proxylist.txt',
'http://absentius.narod.ru/',
'http://accforfree.blogspot.com/feeds/posts/default?alt=rss',
'http://actualproxy.blogspot.com/feeds/posts/default?alt=rss',
'http://adan82222.blogspot.com/feeds/posts/default?alt=rss',
'http://adminsarhos.blogspot.com/feeds/posts/default?alt=rss',
'http://www.admintuan.com/',
'http://advanceauto-show.blogspot.com/feeds/posts/default?alt=rss',
'http://www.agarboter.ga/Proxy/',
'http://agarioproxys.blogspot.com/feeds/posts/default?alt=rss',
'http://agarproxy.tk/ip/1.php',
'http://agarproxy.tk/ip/2.php',
'http://agarproxy.tk/ip/3.php',
'http://agarproxy.tk/ip/4.php',
'http://ahmadas120873.blogspot.com/feeds/posts/default?alt=rss',
'http://ahmadqoisja09.blogspot.com/feeds/posts/default?alt=rss',
'http://aimeegracecatering.blogspot.com/feeds/posts/default?alt=rss',
'http://aircrack.kl.com.ua/all.txt',
'http://www.ajshw.net/news/?list_20.html',
'http://akatsukihackblog.blogspot.com/feeds/posts/default?alt=rss',
'http://alexa.lr2b.com/proxylist.txt',
'http://aliveproxies.com/ipproxy/page/1/',
'http://aliveproxies.com/ipproxy/transparent/page/1/',
'http://aliveproxies.com/pages/page-scrapebox-proxies/',
'http://aliveproxies.com/ipproxy/elite/page/1/',
'http://aliveproxies.com/ipproxy/anonymous/page%/page%/',
'http://alivevpn.blogspot.com/feeds/posts/default?alt=rss',
'http://alldayproxy.blogspot.com/feeds/posts/default?alt=rss',
'http://amega.blogfree.net/?f=1101173',
'http://amisauvveryspecial.blogspot.com/feeds/posts/default?alt=rss',
'http://www.amusetech.net/proxys.txt',
'http://android-amiral.blogspot.com/feeds/posts/default?alt=rss',
'http://android-ful.blogspot.com/feeds/posts/default?alt=rss',
'http://andrymc4.blogspot.com/feeds/posts/default?alt=rss',
'http://anondwahyu.blogspot.com/feeds/posts/default?alt=rss',
'https://anonfreeproxy.blogspot.com/feeds/posts/default?alt=rss',
'http://anon-hackers.forumfree.it/?f=11363412',
'http://anonimseti.blogspot.com/feeds/posts/default?alt=rss',
'http://anonproxylist.blogspot.com/feeds/posts/default?alt=rss',
'http://www.anonproxylist.com/feed/',
'http://anonymouscyberteamact.blogspot.com/feeds/posts/default?alt=rss',
'http://feeds.feedburner.com/AnonymousDailyProxyList',
'http://anonymousproxies007.blogspot.com/feeds/posts/default?alt=rss',
'http://anonymous-proxy.blogspot.com/feeds/posts/default?alt=rss',
'http://anonymousproxyblog.blogspot.com/feeds/posts/default?alt=rss',
'http://www.antynet.pl/index.php/feed/',
'http://anyelse.com/Index.aspx?p=1',
'http://apexgeeky.blogspot.com/feeds/posts/default?alt=rss',
'http://api.foxtools.ru/v2/Proxy.txt',
'http://api.good-proxies.ru/get.php?free=',
'http://applebaby2013.blogspot.com/feeds/posts/default?alt=rss',
'http://ar51.eu/forum/222-proxy/',
'http://arianatorleaks.com/list/proxy.txt',
'http://www.arpun.com/article/list_1_319.html',
'http://artgameshop.ru/proxy/api/proxylist.php',
'http://asdfg3ffasdasdasd.blogspot.com/feeds/posts/default?alt=rss',
'http://asifameerbakhsh.blogspot.com/feeds/posts/default?alt=rss',
'http://www.askimiz.net/kategori/genel',
'http://astra.bbbv.ru/index.php?showforum=4',
'http://asua.esy.es/ProxyServers/proxy.txt',
'http://www.atcpu.com/thread/123?type=179',
'http://www.atesclup.com/forum/guencel-proxy-listesi.285/',
'http://www.atnteam.com/forumdisplay.php?20-Discussions-about-anonymity',
'http://www.atnteam.com/forumdisplay.php?21-Socks-Proxy',
'http://www.atnteam.com/forumdisplay.php?22-HTTP-Proxy',
'http://atomintersoft.com/free_socks5_proxy_list',
'http://atomintersoft.com/free_proxy_list',
'http://atomintersoft.com/transparent_proxy_list',
'http://atomintersoft.com/anonymous_proxy_list',
'http://atomintersoft.com/high_anonymity_elite_proxy_list',
'https://autoproxyblog.wordpress.com/feed/',
'http://avto-alberto.avtostar.si/avtostar/proxy_list_1.txt',
'http://avto-alberto.avtostar.si/avtostar/proxy_list_2.txt',
'http://avto-alberto.avtostar.si/avtostar/proxy_list_3.txt',
'http://awmproxy.cn/freeproxy.php',
'http://awmproxy.com/freeproxy_XXXXXXXXX.txt',
'http://awmproxy.com.ua/',
'http://awmproxy.de/index.php',
'http://awmproxy.net/',
'http://www.aw-reliz.ru/index.php/board,7.0.html',
'https://bacasimpel.blogspot.com/feeds/posts/default?alt=rss',
'http://backtrack-gr0up.blogspot.com/feeds/posts/default?alt=rss',
'http://backtrack-group.blogspot.com/feeds/posts/default?alt=rss',
'http://baglanforum.10tr.net/syndication.php?type=atom1.0&fid=111',
'http://baglanforum.10tr.net/syndication.php?fid=112',
'http://baglanforum.10tr.net/syndication.php?fid=113',
'http://baglanforum.10tr.net/syndication.php?fid=118',
'http://www.bagnets.cn/bag/dailiIP/guonaIPdaili/',
'http://www.baizhongso.com/ipShow.aspx?id=7972',
'http://www.baizhongsou.com/default.aspx',
'http://www.bali-xp.com/feeds/posts/default?alt=rss',
'http://base.4rumer.com/f17-socks-proxy',
'http://base.4rumer.com/f18-http-proxy',
'http://bbhfdownloads.blogspot.com/feeds/posts/default?alt=rss',
'http://bbs.crsky.com/simple/index.php?f80.html',
'http://bdaccess24.blogspot.com/feeds/posts/default?alt=rss',
'https://beatemailmass9947.wordpress.com/feed/',
'http://beautydream.spb.ru/category/hvastiki/feed/',
'http://bestallproxy.blogspot.com/feeds/posts/default?alt=rss',
'http://bestblackhatforum.com/Forum-Proxies-and-VPN-Section',
'http://bestblackhattips.blogspot.com/feeds/posts/default?alt=rss',
'http://best-hacker.ru/proksi-svezhak/?s=%D0%BF%D1%80%D0%BE%D0%BA%D1%81%D0%B8',
'http://bestpollitra.com/lending/prxsRaw/all/',
'http://bestpremiumproxylist.blogspot.com/feeds/posts/default?alt=rss',
'http://bestproxiesandsocks.blogspot.com/feeds/posts/default?alt=rss',
'http://bestproxiesofworld.blogspot.com/feeds/posts/default?alt=rss',
'http://best-proxy.com/english/index.php?p=1',
'http://best-proxylist.blogspot.com/feeds/posts/default?alt=rss',
'http://bestproxylist4you.blogspot.com/feeds/posts/default?alt=rss',
'http://bhfreeproxies.blogspot.com/feeds/posts/default?alt=rss',
'http://www.bigdaili.com/dailiip/1/1.html',
'http://www.bigdaili.com/dailiip/2/1.html',
'http://www.bigdaili.com/dailiip/3/1.html',
'http://www.bigdaili.com/dailiip/4/1.html',
'http://biskutliat.blogspot.com/feeds/posts/default?alt=rss',
'https://bitorder.ru/forumdisplay.php?26-Socks5',
'http://blackhatforum.co/forumdisplay.php?17-Proxies',
'http://blackhatland.com/forumdisplay.php?fid=68',
'http://www.blackhatprivate.com/index.php?/forum/97-proxies-section/',
'http://www.blackhatprotools.org/forumdisplay.php?18-Proxies',
'http://www.blackhatseo.pl/forum/4-pozycjonowanie-w-google/',
'http://blackhatseocommunity.com/f20/',
'http://blackhatviet.com/forumdisplay.php/24-Hosting-VPS-Proxy-Socks',
'http://black-socks24.blogspot.com/feeds/posts/default?alt=rss',
'http://blackxpirate.blogspot.com/feeds/posts/default?alt=rss',
'http://blast.hk/forums/32/',
'http://www.blizzleaks.net/',
'http://blog.bafoed.ru/feed/',
'http://blog.baotuoitredoisong.com/search/label/Socks%20Proxy',
'http://blog.crackitindonesia.com/search?q=proxy',
'http://blog.donews.com/kemon/feed/',
'http://blog.fzcnjp.com/proxy',
'http://blog.i.ua/user/616175/',
'http://blog.kuaidaili.com/feed',
'http://blog.mobilsohbetodalari.org/feed',
'http://blog.sina.com.cn/rss/5075816935.xml',
'http://blogprojesitr.blogspot.com/feeds/posts/default?alt=rss',
'http://blogspotproxy.blogspot.com/feeds/posts/default?alt=rss',
'http://www.blue-hosting.biz/',
'http://boltonnewyork.blogspot.com/feeds/posts/default?alt=rss',
'https://www.boomplace.com/index.php/forum/mixed/282-proxy-liste-100-ips-taeglich-neu?start=99999999',
'http://boosterbotsforum.com/index.php?p=/categories/freebies-giveaways',
'http://botgario.ml/proxy/',
'http://brainviewhackers.blogspot.com/feeds/posts/default?alt=rss',
'http://brazilproxies.blogspot.com/feeds/posts/default?alt=rss',
'http://brothers-download.mihanblog.com/post/rss/',
'http://bsproxy.blogspot.com/feeds/posts/default?alt=rss',
'http://www.bulkmoneyforum.com/share-your-free-stuff-free-services-request-here-if-u-need-something/12768-good-working-checked-live-proxies-999999.html',
'http://buondon.info/forums/sock-live.143.html',
'http://www.buyproxy.ru/free-proxies/%D0%9D%D0%B5%D1%82_socks/',
'http://buytrafficus.blogspot.com/feeds/posts/default?alt=rss',
'http://bworm.vv.si/',
'http://www.cannabis-samen-hanfsamen.de/',
'http://www.captchapanel.blogspot.com/feeds/posts/default?alt=rss',
'http://caratrikblogger.blogspot.com/feeds/posts/default?alt=rss',
'http://carder.site/forumdisplay.php?f=58',
'http://carderparadise.com/forumdisplay.php?14-Security-Services',
'https://cardersforum.se/forum55/',
'https://cardersforum.ws/forum55/',
'http://www.caretofun.net/free-proxies-and-socks/',
'http://cc-ppfresh.blogspot.com/feeds/posts/default?alt=rss',
'http://cdn.vietso1.com/forums/proxy-socks.63/',
'https://cfud.biz/lending/prxsDownload/all/',
'http://www.changeips.com/',
'http://www.chaojirj.com/daili/',
'http://www.chatles.net/kategori/irc-proxy/feed',
'http://cheap-flights-to-dubai.blogspot.com/feeds/posts/default?alt=rss',
'http://cheap-offers-online.com/feed/',
'http://checkerproxy.net/',
'http://checkproxylist.blogspot.com/feeds/posts/default?alt=rss',
'http://check-proxylist.blogspot.com/feeds/posts/default?alt=rss',
'http://www.checkyounow.com/',
'http://www.chemip.net/proxyip.html',
'https://chenqu.wordpress.com/tag/proxy/',
'http://china-eliteproxy.blogspot.com/feeds/posts/default?alt=rss',
'http://chinaproxies.blogspot.com/feeds/posts/default?alt=rss',
'https://chinaproxylist.wordpress.com/feed/',
'http://chingachgook.net/my-servisy/proxy',
'http://chk.gblknjng.com/socks.txt',
'http://www.chupadrak.i8.com/',
'http://clientn.autohideip.com/update/',
'http://clientn.easy-hideip.com/update/',
'http://clientn.platinumhideip.com/update/?ACTION=Update',
'http://clientn.platinumhideip.com/update/?ACTION=Update&51823&PID=PHI&SN=&MCD=0000000000CD1A40&UNL=&LANG=English&DAY=0&RUNTIME=0&VER=03000406&SVER=0&WVER=5_1_Service',
'http://clientn.real-hide-ip.com/update/?ACTION=Update',
'http://clientn.superhideip.com/update/?ACTION=Update&14783&PID=SHI&SN=&MCD',
'http://clientn.surfanonymous-free.com/update/?ACTION=Update&27232&PID=SAF&SN=&MCD=000000001C35B5B7&UNL=&LANG=English&DAY=0&RUNTIME=0&VER=02010502&SVER=0&WVER=6_1_Service',
'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all',
'https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all',
'http://olaf4snow.com/public/proxy.txt',
'http://atomintersoft.com/products/alive-proxy/proxy-list/3128',
'http://atomintersoft.com/products/alive-proxy/proxy-list?ap=9',
'http://bestproxy.narod.ru/proxy1.html',
'http://bestproxy.narod.ru/proxy2.html',
'https://spys.one/',
'http://greenrain.bos.ru/R_Stuff/Proxy.htm',
'http://hack-hack.chat.ru/proxy/allproxy.txt',
'http://hack-hack.chat.ru/proxy/anon.txt',
'http://hack-hack.chat.ru/proxy/p1.txt',
'http://hack-hack.chat.ru/proxy/p2.txt',
'http://hack-hack.chat.ru/proxy/p3.txt',
'http://hack-hack.chat.ru/proxy/p4.txt',
'http://inav.chat.ru/ftp/proxy.txt',
'http://johnstudio0.tripod.com/index1.htm',
'http://rammstein.narod.ru/proxy.html',
'http://sergei-m.narod.ru/proxy.htm',
'http://tomoney.narod.ru/help/proxi.htm',
'http://westdollar.narod.ru/proxy.htm',
'http://atomintersoft.com/products/alive-proxy/proxy-list/high-anonymity/',
'http://atomintersoft.com/products/alive-proxy/socks5-list',
'http://proxy-ip-list.com/',
'http://proxy-ip-list.com',
'http://proxy-ip-list.com/download/free-usa-proxy-ip.txt',
'http://atomintersoft.com/products/alive-proxy/proxy-list',
'http://atomintersoft.com/products/alive-proxy/proxy-list/com',
'http://atomintersoft.com/proxy_list_domain_com',
'http://atomintersoft.com/proxy_list_domain_edu',
'http://atomintersoft.com/proxy_list_domain_net',
'http://atomintersoft.com/proxy_list_domain_org',
'http://atomintersoft.com/proxy_list_port_3128',
'http://atomintersoft.com/proxy_list_port_80',
'http://atomintersoft.com/proxy_list_port_8000',
'http://atomintersoft.com/proxy_list_port_81',
'http://best-proxy.com/english/search.php?search=anonymous-and-elite&country=any&type=anonymous-and-elite&port=any&ssl=any',
'http://best-proxy.com/english/search.php?search=anonymous-and-elite&country=any&type=anonymous-and-elite&port=any&ssl=any&p=2',
'http://best-proxy.com/english/search.php?search=anonymous-and-elite&country=any&type=anonymous-and-elite&port=any&ssl=any&p=3',
'http://nntime.com/proxy-list-01.htm',
'http://nntime.com/proxy-list-02.htm',
'http://nntime.com/proxy-list-03.htm',
'http://nntime.com/proxy-list-04.htm',
'http://nntime.com/proxy-list-05.htm',
'http://nntime.com/proxy-list-06.htm',
'http://nntime.com/proxy-list-07.htm',
'http://nntime.com/proxy-list-08.htm',
'http://nntime.com/proxy-list-09.htm',
'http://nntime.com/proxy-list-10.htm',
'http://nntime.com/proxy-list-11.htm',
'http://nntime.com/proxy-list-12.htm',
'http://nntime.com/proxy-list-13.htm',
'http://nntime.com/proxy-list-14.htm',
'http://nntime.com/proxy-list-15.htm',
'http://nntime.com/proxy-list-16.htm',
'http://nntime.com/proxy-list-17.htm',
'http://nntime.com/proxy-list-18.htm',
'http://nntime.com/proxy-list-19.htm',
'http://nntime.com/proxy-list-20.htm',
'http://nntime.com/proxy-list-21.htm',
'http://nntime.com/proxy-list-22.htm',
'http://nntime.com/proxy-list-23.htm',
'http://nntime.com/proxy-list-24.htm',
'http://nntime.com/proxy-list-25.htm',
'http://nntime.com/proxy-list-26.htm',
'http://nntime.com/proxy-list-27.htm',

    'https://advanced.name/freeproxy/6684a2dc45e52',
    'https://advanced.name/freeproxy',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
    'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
    'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
    'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
    'https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
    'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
    'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
    'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
    'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
    'https://api.openproxylist.xyz/http.txt',
    'https://api.proxyscrape.com/v2/?request=displayproxies',
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
    'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous',
    'http://worm.rip/http.txt',
    'https://proxyspace.pro/http.txt',
    'https://multiproxy.org/txt_all/proxy.txt',
    'https://proxy-spider.com/api/proxies.example.txt',
    'https://sunny9577.github.io/proxy-scraper/proxies.txt',
    'https://sunny9577.github.io/proxy-scraper/generated/http_proxies.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt',
    'https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt',
    'https://www.proxy-list.download/api/v1/get?type=http',
    'https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt',
    'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=5000&country=all&ssl=all&anonymity=all',
    'https://sunny9577.github.io/proxy-scraper/generated/socks4_proxies.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt',
    'https://www.proxy-list.download/api/v1/get?type=socks4',
    'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=5000&country=all&ssl=all&anonymity=all',
    'https://sunny9577.github.io/proxy-scraper/generated/socks5_proxies.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt',
    'https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt',
    'https://www.proxy-list.download/api/v1/get?type=socks',
    'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt',
    'https://raw.githubusercontent.com/mallisc5/master/proxy-list-raw.txt',
    'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
    'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt',
    'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt',
    'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt',
    'https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt',
    'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt',
    'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt',
    'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt',
    'https://raw.githubusercontent.com/tuanminpay/live-proxy/master/http.txt',
    'https://raw.githubusercontent.com/casals-ar/proxy-list/main/https',
    'https://raw.githubusercontent.com/casals-ar/proxy-list/main/http',
    'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
    'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt',
    'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
    'http://atomintersoft.com/proxy_list_port_80',
    'http://atomintersoft.com/proxy_list_domain_org',
    'http://atomintersoft.com/proxy_list_port_3128',
    'http://www.cybersyndrome.net/pla5.html',
    'http://alexa.lr2b.com/proxylist.txt',
    'http://browse.feedreader.com/c/Proxy_Server_List-1/449196258',
    'http://free-ssh.blogspot.com/feeds/posts/default',
    'http://browse.feedreader.com/c/Proxy_Server_List-1/449196259',
    'http://johnstudio0.tripod.com/index1.htm',
    'http://atomintersoft.com/transparent_proxy_list',
    'http://atomintersoft.com/anonymous_proxy_list',
    'http://atomintersoft.com/high_anonymity_elite_proxy_list',
    'http://worm.rip/https.txt',
    'http://rootjazz.com/proxies/proxies.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt',
    'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
    'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt'
];


def download_and_save_proxies(url, output_file):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_file, 'a') as file:
                file.write(response.text)
                print(f"Success Gets In {url}")
        else:
            print(f"Well Failed In {url}")
    except Exception as e:
        print(f"Something Broken in {url}")

open(output_file, 'w').close()

class Proxy:
    def __init__(self, method, proxy):
        if method.lower() not in ["http", "https"]:
            raise NotImplementedError("Only HTTP and HTTPS are supported")
        self.method = method.lower()
        self.proxy = proxy

    def is_valid(self):
        return re.match(r"\d{1,3}(?:\.\d{1,3}){3}(?::\d{1,5})?$", self.proxy)

    def check(self, site, timeout, user_agent):
        url = self.method + "://" + self.proxy
        proxy_support = urllib.request.ProxyHandler({self.method: url})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
        req = urllib.request.Request(self.method + "://" + site)
        req.add_header("User-Agent", user_agent)
        try:
            start_time = time()
            urllib.request.urlopen(req, timeout=timeout)
            end_time = time()
            time_taken = end_time - start_time
            return True, time_taken, None
        except Exception as e:
            return False, 0, e

    def __str__(self):
        return self.proxy

def verbose_print(verbose, message):
    if verbose:
        print(message)

def check(file, timeout, method, site, verbose, random_user_agent):
    proxies = []
    with open(file, "r") as f:
        for line in f:
            proxies.append(Proxy(method, line.replace("\n", "")))

    print(f"Checking {len(proxies)} Proxy")
    proxies = filter(lambda x: x.is_valid(), proxies)
    valid_proxies = []
    user_agent = random.choice(user_agents)

    def check_proxy(proxy, user_agent):
        new_user_agent = user_agent
        if random_user_agent:
            new_user_agent = random.choice(user_agents)
        valid, time_taken, error = proxy.check(site, timeout, new_user_agent)
        message = {
            True: f"{proxy} is valid, took {time_taken} seconds",
            False: f"{proxy} is invalid: {repr(error)}",
        }[valid]
        verbose_print(verbose, message)
        valid_proxies.extend([proxy] if valid else [])

    threads = []
    for proxy in proxies:
        t = threading.Thread(target=check_proxy, args=(proxy, user_agent))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    with open(file, "w") as f:
        for proxy in valid_proxies:
            f.write(str(proxy) + "\n")

    print(f"Finding {len(valid_proxies)} Valid Proxy")


def verbose_print(verbose, message):
    if verbose:
        print(message)

for url in proxy_urls:
    download_and_save_proxies(url, output_file)
    
with open('proxy.txt', 'r') as ceki:
    jumlh = sum(1 for line in ceki)
    
print(f"Get: {jumlh} Proxy. Do you want to check it out? [Y/N]: ", end="")
choice = input().strip().lower()

if choice == 'y' or choice == 'Y':
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10157) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.48",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.277",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
    ]
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--timeout", type=int, default=20, help="Dismiss the proxy after -t seconds")
    parser.add_argument("-p", "--proxy", default="http", help="Check HTTPS or HTTP proxies")
    parser.add_argument("-s", "--site", default="https://google.com/", help="Check with specific website like google.com")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
    parser.add_argument("-r", "--random_agent", action="store_true", help="Use a random user agent per proxy")
    
    args = parser.parse_args()
    check(file=output_file, timeout=args.timeout, method=args.proxy, site=args.site, verbose=args.verbose, random_user_agent=args.random_agent)
    sys.exit(0)
else:
    print(f"Thank you for using my script ~Lintar")
