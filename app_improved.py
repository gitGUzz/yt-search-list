#RAM INTENSIVE                                          RAM INTENSIVE#
#RAM INTENSIVE                                          RAM INTENSIVE#
#RAM INTENSIVE                                          RAM INTENSIVE#
#RAM INTENSIVE      DO NOT INCLUDE A LOT OF SONGS       RAM INTENSIVE#
#RAM INTENSIVE      DO NOT INCLUDE A LOT OF SONGS       RAM INTENSIVE#
#RAM INTENSIVE      DO NOT INCLUDE A LOT OF SONGS       RAM INTENSIVE#
#RAM INTENSIVE                                          RAM INTENSIVE#
#RAM INTENSIVE                                          RAM INTENSIVE#
#RAM INTENSIVE                                          RAM INTENSIVE#



import re
import sys
import webbrowser
import time

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
sys.stdin = open('primerno.txt', 'r', encoding='utf-8')
count = 0
for line in sys.stdin:
        count += 1
        mod_string = re.sub('^\d*. ', '', line)
        mod_string_nospace = re.sub('\s', '+', mod_string)
        url = "https://www.youtube.com/results?search_query=" + mod_string_nospace

        if url == "https://www.youtube.com/results?search_query=+":
            print("empty line\n")
            url = "https://www.youtube.com/results?search_query=" #reset
        else:
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open_new_tab(url)
            time.sleep(2.5) #cpu intens buffer
            print(mod_string + " ---> " + url + "\n")
    