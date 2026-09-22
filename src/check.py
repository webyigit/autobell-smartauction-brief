import os, json
from playwright.sync_api import sync_playwright
p='file://'+os.path.abspath('deck.html')+'#raw'
with sync_playwright() as pw:
    b=pw.chromium.launch(channel='chrome'); pg=b.new_page(viewport={'width':1920,'height':1080})
    pg.goto(p); pg.wait_for_timeout(800)
    res=pg.evaluate("""()=>[...document.querySelectorAll('.slide')].map((s,i)=>{const m=s.querySelector('.main');return {i:i+1,over:m.scrollHeight-m.clientHeight,mainH:m.clientHeight,foot:s.querySelector('.foot').getBoundingClientRect().height}})""")
    for r in res: print(r)
    b.close()
