# -*- coding: utf-8 -*-
# @Time  : 2025/01/23 10:33
# @Author: masonsxu
# @File  : GetRedMansionData.py
# @Desc  : Get the data of the Red Mansion from the website

import time

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_html(url):
    # 调用 UserAgent 随机生成用户代理头
    ua = UserAgent()
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "User-Agent": ua.random,
    }
    try:
        page_text = requests.get(url, timeout=3000, headers=header)
        page_text.raise_for_status()
        # 制定编码
        page_text.encoding = page_text.apparent_encoding
        return page_text.text
    except ValueError:
        return "please inspect your url or setup"


bookFile = open("./data/RedMansion_origin.txt", "a+", encoding="utf-8")


def get_chapter_data(url):
    try:
        html = get_html(url)
        soup = BeautifulSoup(html, "lxml")
        header = (
            soup.find("b")
            .get_text()
            .replace(" 第", "第")
            .replace("\u3000", " ")
            .strip()
        )
        if header.find("《红楼梦》第一回") != -1:
            bookFile.write(header)
        else:
            bookFile.write(header.replace("《红楼梦》第", "\n《红楼梦》第").rstrip(" "))
        content = (
            soup.find("pre")
            .get_text()
            .replace("\n", "")
            .replace("\u3000\u3000", "\n\u3000\u3000")
        )
        bookFile.write(content)
    except IndexError or UnicodeEncodeError:
        print("稍等~~~，出现错误！！！")
        get_chapter_data(url)


if __name__ == "__main__":
    start = time.perf_counter()
    for index in range(1, 121):
        get_chapter_data("http://www.purepen.com/hlm/" + str(index).zfill(3) + ".htm")
        a = "*" * index
        b = "." * (120 - index)
        c = (index / 120) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
    bookFile.close()
    print("\n下载完成！！！")
    # get_chapter_data('http://www.purepen.com/hlm/001.htm')
