# -*- coding: utf-8 -*-
"""Generate /cn/index.html (Simplified Chinese, Mainland terminology) from index.html."""
import os
from opencc import OpenCC

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'portfolio')
SRC = os.path.join(BASE, 'index.html')
DST = os.path.join(BASE, 'cn', 'index.html')

with open(SRC, 'r', encoding='utf-8') as f:
    html = f.read()

# 1) Mainland terminology mapping applied on the Traditional text FIRST
#    (terms OpenCC tw2sp misses or renders differently from the spec).
#    Longer phrases before shorter ones.
TERM_MAP = [
    ('馬韡寧', '马韡宁'),
    ('記帳', '记账'),
    ('指標', '指标'),
    ('截圖', '截图'),
    ('身分', '身份'),
    ('想像', '想象'),
    ('回饋', '反馈'),
    ('物件導向', '面向对象'),
    ('資料庫', '数据库'),
    ('資料夾', '文件夹'),
    ('短視頻', '短视频'),
    ('視頻', '视频'),
    ('軟體', '软件'),
    ('網路', '网络'),
    ('使用者', '用户'),
    ('介面', '界面'),
    ('資訊', '信息'),
    ('資料', '数据'),
    ('記憶體', '内存'),
    ('預設', '默认'),
    ('串接', '接入'),
    ('透過', '通过'),
    ('程式', '程序'),
    ('品質', '质量'),
    ('螢幕', '屏幕'),
    ('線上', '在线'),
    ('下載', '下载'),
    ('日誌', '日志'),
    ('範例', '示例'),
    ('陣列', '数组'),
    ('變數', '变量'),
    ('回圈', '循环'),
    ('模組', '模块'),
    ('外掛', '插件'),
    ('帳號', '账号'),
    ('註冊', '注册'),
    ('登入', '登录'),
    ('隱私', '隐私'),
    ('設定', '设置'),
    ('檔案', '文件'),
    ('列印', '打印'),
    ('匯出', '导出'),
    ('匯入', '导入'),
    ('連結', '链接'),
    ('搜尋', '搜索'),
    ('簡訊', '短信'),
]
for tw, cn in TERM_MAP:
    html = html.replace(tw, cn)

# 2) Character-level Traditional -> Simplified (Taiwan standard) for the rest.
#    English text and already-simplified terms are untouched.
cc = OpenCC('tw2sp')
html = cc.convert(html)

# 3) Remove the History Bridge project card (cn version only).
# Locate the card by its icon, then drop the whole <div class="project-card">
# block by counting div nesting depth.
import re
_marker = 'icons/history-bridge.svg'
_pos = html.find(_marker)
if _pos != -1:
    _start = html.rfind('<div class="project-card">', 0, _pos)
    _depth = 0
    _end = None
    for _m in re.finditer(r'<div\b[^>]*>|</div>', html[_start:]):
        if _m.group(0).startswith('</'):
            _depth -= 1
            if _depth == 0:
                _end = _start + _m.end()
                break
        else:
            _depth += 1
    if _end is not None:
        html = html[:_start] + html[_end:]

# 4) Structural adjustments for the /cn page
# Default lang="zh-CN": only Simplified Chinese is shown by default
# (html[lang="zh-CN"] hides .en-only). EN/中 toggle buttons still work.
html = html.replace('<html lang="en">', '<html lang="zh-CN">')
html = html.replace('html[lang="zh-TW"]', 'html[lang="zh-CN"]')
html = html.replace("'zh-TW'", '"zh-CN"')
html = html.replace('Noto+Sans+TC', 'Noto+Sans+SC')
html = html.replace("'Noto Sans TC'", "'Noto Sans SC'")

# Chinese shown by default: 中 button starts active, EN does not
html = html.replace(
    '<button id="lang-en" class="active">EN</button>',
    '<button id="lang-en">EN</button>')
html = html.replace(
    '<button id="lang-zh">中</button>',
    '<button id="lang-zh" class="active">中</button>')

# Chinese-first title; canonical/og:url point at the /cn deployment
html = html.replace(
    '<title>Wei-Ning (Vernessa) Ma | AI Product &amp; Growth</title>',
    '<title>马韡宁 Vernessa Ma｜AI 产品与海外增长</title>')
html = html.replace(
    '<meta property="og:url" content="https://weining-ma.vercel.app/">',
    '<meta property="og:url" content="https://weining-ma.vercel.app/cn">')
html = html.replace(
    '<link rel="canonical" href="https://weining-ma.vercel.app/">',
    '<link rel="canonical" href="https://weining-ma.vercel.app/cn">')

# 简体页的增长案例按钮指向简体版增长页（绝对路径，/cn 和 /cn/ 都不会断）
html = html.replace('<a href="/growth/" class="btn btn-secondary">', '<a href="/growth/cn/" class="btn btn-secondary">')

os.makedirs(os.path.dirname(DST), exist_ok=True)
with open(DST, 'w', encoding='utf-8') as f:
    f.write(html)
print('written:', DST)
