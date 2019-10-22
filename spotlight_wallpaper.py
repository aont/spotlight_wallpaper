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
import hashlib
import piexif

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
        'pl' : 'ja-JP', \
        'lc' : 'us', \
        'ctry' : 'jp' \
    }
    # date_i = datetime.datetime.now()
    # params['time'] = '2017-12-31T23:59:59Z'
    
    sess = requests.session()
    for i in range(32):
        # date_i -= datetime.timedelta(hours=i)
        # params['time'] = date_i.strftime("%Y-%m-%dT%H:%M:%SZ")
        sys.stderr.write("[info] i=%s\n" % i)
        show_spotlight_url(sess, params)
        #time.sleep(120)


url_pat=re.compile("/([^/]*)$")
edge_pat=re.compile("^microsoft-edge:")
def show_spotlight_url(sess, params):
    spotlight_api = 'https://arc.msn.com/v3/Delivery/Cache'
    result = sess.get(spotlight_api, params = params)
    # sys.stdout.write(result.content)
    if requests.codes.get("ok") != result.status_code:
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
        # for k, v in ad.items():
        #     print("ad:%s: %s"%(k,v))


        # print(ad.get('title_text').get('tx'))
        title = ad.get('title_text').get('tx')

        # print(ad.get("hs1_title_text").get('tx'))
        # print(ad.get("hs1_cta_text").get('tx'))
        # print(ad.get("hs2_title_text").get('tx'))
        # print(ad.get("hs2_cta_text").get('tx'))

        for i in [1]: # do not change

            landscape_key = "image_fullscreen_%03d_landscape" % i
            # landscape_key = "image_fullscreen_%03d_portrait" % i
            landscape = ad.get(landscape_key)
            if not landscape:
                break

            # print(ad.get('image_fullscreen_001_portrait').get('u'))
            # url = ad.get('image_fullscreen_001_portrait').get('u')
            # print(ad.get('image_fullscreen_001_landscape').get('u'))
            url = landscape.get('u')
            sha256 = landscape.get('sha256')
            fileSize = landscape.get('fileSize')

            # json.dump(item_js.get('ad'), fp=sys.stdout, ensure_ascii=False, indent=2)
            # for k, v in item_js.get('ad').items():
            #     print("%s: %s"%(k,v))
            
            # print repr(item.get('item'))

            m = url_pat.search(url)
            fn = m.group(1)
            save_path_tentative = title + '_' + fn + '.jpg'
            save_path = save_path_tentative.replace('?', '_')
            sys.stderr.write('[Info] downloading %s\n' % save_path)
            img_result = sess.get(url)
            jpeg_data = img_result.content
            sys.stderr.write('[Info] sanity check\n')
            if len(jpeg_data) != fileSize:
                Exception("fileSize is not consistent!")
            if hashlib.sha256(jpeg_data).hexdigest() != sha256:
                Exception("sha256 is not consistent!")

            # 0x010e: b'title'
            # 0x013b: b'creator'
            # 0x8298: b'copyright'
            # 0x9c9b: kenmei
            # 0x9c9c: comment
            # 0x9c9d: author
            # 0x9c9f: subject

            
            exif_0th = {}
            exif_0th[0x010e] = title.encode('utf-8')
            # exif_0th[0x013b] = "creator"
            exif_0th[0x8298] = ad.get('copyright_text').get('tx').encode('utf-8')
            # exif_0th[str(0x9c9b)] = title
            # exif_0th[str(0x9c9f)] = title
            exif_0th[0x9c9c] = "\n\n".join([
                ad.get('title_text').get('tx'),
                edge_pat.sub("", ad.get('title_destination_url').get('u')),
                ad.get('hs1_title_text').get('tx'),
                ad.get('hs1_cta_text').get('tx'),
                edge_pat.sub("", ad.get('hs1_destination_url').get('u')),
                ad.get('hs2_title_text').get('tx'),
                ad.get('hs2_cta_text').get('tx'),
                edge_pat.sub("", ad.get('hs2_destination_url').get('u'))
            ]).encode('utf-16')

            exif = {'0th': exif_0th }
            exif_bytes = piexif.dump(exif)
            piexif.insert(exif_bytes, jpeg_data, save_path)

            # with open(save_path, 'wb') as save_file:
            #     save_file.write(img_result.content)
            
            # break
            i+=1

    # print js
    
if __name__ == '__main__':
    main()
    exit()
