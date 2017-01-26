#!/usr/bin/python
# -*- coding:utf-8 -*-
from sys import argv
import re
import requests
from flask import Flask

app = Flask(__name__)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 Chrome/55.0.2883.87 Safari/537.36',
    'Referer': 'http://kinopoisk.ru'
}
regexp = re.compile(r"document\.getElementById\('code_textarea'\)\.innerHTML='(.*)'")
HTML = '''
<html>
<head>
    <meta charset="utf-8">
    <title>MoonVideo</title>
</head>
<body>
    <h1>{kid}</h1>
    <div>{data}</div>
</body>
</html>
'''

@app.route('/<kinopoisk_id>')
def main(kinopoisk_id):
    url = "http://moonwalk.co/moonwalk/search_as?kinopoisk_id=" + kinopoisk_id
    r = requests.get(url, headers=HEADERS)
    iframe = regexp.search(r.text).groups()[0]
    iframe = iframe.replace("\\'", "'").replace('\\"', '"')
    if not iframe:
        return HTML.format(kid=kinopoisk_id, data="<p>Видео не найдено</p>")
    else:
        return HTML.format(kid=kinopoisk_id, data=iframe)

if len(argv) >= 2:
    print('DEBUG MODE')
    app.run(host='0.0.0.0', port=80, debug=True)
else:
    app.run(host='0.0.0.0', port=80)
