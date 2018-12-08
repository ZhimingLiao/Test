# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 茅岗新村  志明  2018-12-08 10:36
# 当前计算机登录名称 :志明
# 项目名称  :
# 编译器   :PyCharm
__author____ = '志明'
__time__ = '2018-12-08 '

import time
import random
import libtorrent_test as lt


if __name__ == '__main__':

    print(time.time())

    try:
        session = lt.session()
        r = random.randrange(10000, 50000)
        session.listen_on(r, r + 10)
        session.add_dht_router('router.bittorrent.com', 6881)
        session.add_dht_router('router.utorrent.com', 6881)
        session.add_dht_router('dht.transmission.com', 6881)
        session.add_dht_router('127.0.0.1', 6881)
        session.start_dht()
        # metadata = fetch_torrent(session, binhash.encode('hex'), timeout)
        session = None
    except:
        # traceback.print_exc()
        print('报错')
        pass
    finally:

        # metadata_queue.put((binhash, address, metadata, 'lt', start_time))
        print(metadata)
