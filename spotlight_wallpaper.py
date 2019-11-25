#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# reference
# - https://github.com/ORelio/Spotlight-Downloader/blob/master/README.md
# - https://github.com/KoalaBR/spotlight/blob/3164a43684dcadb751ce9a38db59f29453acf2fe/spotlightprovider.cpp#L17

import os
import sys
import json
import re
import requests
import datetime
import time
import hashlib
import piexif

def main():
    
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
    
    sess = requests.session()
    for i in range(32):
        sys.stderr.write("[info] i=%s\n" % i)
        save_spotlight_image(sess, params, "images", "portrait")
        # time.sleep(10)


url_pat=re.compile("/([^/]*)$")
edge_pat=re.compile("^microsoft-edge:")
def save_spotlight_image(sess, params, outdir, mode="landscape"):
    spotlight_api = 'https://arc.msn.com/v3/Delivery/Cache'
    result = sess.get(spotlight_api, params = params)
    result.raise_for_status()

    js = json.loads(result.text)
    items = js.get('batchrsp').get('items')
    for item in items:
        item_js = json.loads(item.get('item'))
        ad = item_js.get('ad')

        title = ad.get('title_text').get('tx')

        for i in [1]: # do not change

            key = "image_fullscreen_%03d_%s" % (i, mode)
            image_info = ad.get(key)
            if not image_info:
                break

            url = image_info.get('u')
            sha256 = image_info.get('sha256')
            fileSize = image_info.get('fileSize')

            m = url_pat.search(url)
            fn = m.group(1)
            save_path_tentative = title + '_' + fn + '.jpg'
            save_path = os.path.join(outdir, save_path_tentative.replace('?', '_'))
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

    
if __name__ == '__main__':
    main()
    exit()
