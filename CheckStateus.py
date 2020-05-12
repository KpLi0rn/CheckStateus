# !/usr/bin/env python
# coding: utf-8

import urllib3
import threading
import time
from concurrent.futures import ThreadPoolExecutor
# 第三方库
import pyperclip
import requests
from fake_useragent import UserAgent

# 自定义模块


def banner():
    print("""\033[36m
      ____ _               _     ____  _        _             
     / ___| |__   ___  ___| | __/ ___|| |_ __ _| |_ _   _ ___ 
    | |   | '_ \ / _ \/ __| |/ /\___ \| __/ _` | __| | | / __|
    | |___| | | |  __/ (__|   <  ___) | || (_| | |_| |_| \__ \\
     \____|_| |_|\___|\___|_|\_\|____/ \__\__,_|\__|\__,_|___/ \033[0m

        # Coded By KpLi0rn Website: https://www.wjlshare.xyz
        """)

class Checkstatus(object):
    def __init__(self):
        self.data = set()

    # fofa 语句搜索模块
    # 缺少一个检测 fofa页面回显的功能


    def Paste_Res(self):
        for value in pyperclip.paste().split('\n'):
            if len(value) == 0:
                continue
            else:
                value = value.strip('\r').strip('\n')
                value = value.replace(' ', '')
                if value not in self.data:
                    if not value.startswith("http"):
                        value = "http://" + value
                    self.data.add(value)
                else:
                    continue


    def check(self, url):
        ua = UserAgent(verify_ssl=False)
        urllib3.disable_warnings()  # 禁止跳出来对warning
        headers = {
            'User-Agent': ua.random,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
        s = requests.Session()
        s.keep_alive = False
        try:
            code = str(s.get(url, headers=headers, timeout=6, verify=False).status_code)  # 正常的返回code是int类型
            if code.startswith("2"):
                print("\033[1;0m%s\033[0m  --->>  \033[1;32m%s\033[0m" % (url, code))
            if code.startswith("3"):
                print("\033[1;0m%s\033[0m  --->>  \033[1;33m%s\033[0m" % (url, code))
            if code.startswith("4"):
                print("\033[1;0m%s\033[0m  --->>  \033[1;34m%s\033[0m" % (url, code))
            if code.startswith("5"):
                print("\033[1;0m%s\033[0m  --->>  \033[1;0m%s\033[0m" % (url, code))
        except:
            # print(str(e))
            print("\033[1;31m%s\033[0m  --->>  \033[1;31mtimeout\033[0m" % (str(url)))

    def Run(self):
        self.Paste_Res()
        target = (url for url in self.data)
        pool = ThreadPoolExecutor(10)
        [pool.submit(self.check,domain) for domain in target]


if __name__ == '__main__':
    try:
        banner()
        start = time.time()
        che = Checkstatus()
        che.Run()
        end = time.time()
        print("\n消耗{:.2f}s".format(end - start))
    except KeyboardInterrupt:
        print("停止中...")
