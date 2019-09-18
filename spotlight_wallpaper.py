#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# reference
# - https://github.com/ORelio/Spotlight-Downloader/blob/master/README.md
# - https://github.com/KoalaBR/spotlight/blob/3164a43684dcadb751ce9a38db59f29453acf2fe/spotlightprovider.cpp#L17

import sys
import json
import re
import requests
# import requests_cache
import datetime
import time

def main():
    # requests_cache.install_cache('spotlight')
    
    params = { \
               'pid' : 209567, \
               'fmt' : 'json', \
               'rafb' : 0, \
               'ua' : 'WindowsShellClient\\0', # %2F? \
               'disphorzres' : 9999, \
               'dispvertres' : 9999, \
               'lo' : 80217, \
               'pl' : 'en-US', \
               'lc' : 'us', \
               'ctry' : 'jp' \
    }
    # date_i = datetime.datetime.now()
    # params['time'] = '2017-12-31T23:59:59Z'
    
    sess = requests.session()
    for i in range(1):
        # date_i -= datetime.timedelta(hours=i)
        # params['time'] = date_i.strftime("%Y-%m-%dT%H:%M:%SZ")
        show_spotlight_url(sess, params)
        # time.sleep(120)


url_pat=re.compile("/([^/]*)$")
def show_spotlight_url(sess, params):
    spotlight_api = 'https://arc.msn.com/v3/Delivery/Cache'
    result = sess.get(spotlight_api, params = params)
    # sys.stdout.write(result.content)
    if requests.codes.ok != result.status_code:
        sys.stderr.write("[info] status_code = %s\n" % result.status_code)
        exit()

    
    js = json.loads(result.text)
    items = js.get('batchrsp').get('items')
    # print "len:%s" % len(items)
    for item in items:
        # print item

        # print type(item.get('item'))
        item_js = json.loads(item.get('item'))
        # print item_js
        ad = item_js.get('ad')
        # print ad
        # for k, v in ad.items():
        #     print k

        # print(ad.get('title_text').get('tx'))
        title = ad.get('title_text').get('tx')

        # print(ad.get("hs1_title_text").get('tx'))
        # print(ad.get("hs1_cta_text").get('tx'))
        # print(ad.get("hs2_title_text").get('tx'))
        # print(ad.get("hs2_cta_text").get('tx'))

        # print(ad.get('image_fullscreen_001_portrait').get('u'))
        # print(ad.get('image_fullscreen_001_landscape').get('u'))
        url = ad.get('image_fullscreen_001_landscape').get('u')

        # for k, v in item_js.get('ad').items():
        #     print k
        #     print v
        
        # print repr(item.get('item'))

        m = url_pat.search(url)
        fn = m.group(1)
        save_path_tentative = title + '_' + fn + '.jpg'
        save_path = save_path_tentative.replace('?', '_')
        sys.stderr.write('[Info] downloading %s\n' % save_path)

        img_result = sess.get(url)
        with open(save_path, 'wb') as save_file:
            save_file.write(img_result.content)
        # break


    # print js
    
if __name__ == '__main__':
    main()
    exit()
