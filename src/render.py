import os, json, re
from playwright.sync_api import sync_playwright
titles=json.load(open('titles.json',encoding='utf-8'))
p='file://'+os.path.abspath('deck.html')+'#raw'
names=['개요','서비스유형1_경매방식','서비스유형2_부가서비스','채널','변경요약1_2020-2023','변경요약2_2024-2026','정책1_요금규약','정책2_입찰프로그램','서비스유형상세_지정시간','정책3_개인정보','정책4_점검클레임','회원등급쿠폰','센터레인변천','체크리스트1','체크리스트2','한계와출처']
with sync_playwright() as pw:
    b=pw.chromium.launch(channel='chrome'); pg=b.new_page(viewport={'width':1920,'height':1080})
    pg.goto(p); pg.wait_for_timeout(1000)
    for i,n in enumerate(names):
        el=pg.query_selector('#s%d'%(i+1))
        el.screenshot(path='png/%02d_%s.png'%(i+1,n))
    b.close()
print(sorted(os.listdir('png')))
