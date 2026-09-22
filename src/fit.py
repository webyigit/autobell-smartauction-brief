import os, json
from playwright.sync_api import sync_playwright
p='file://'+os.path.abspath('deck.html')+'#raw'
fs={}
with sync_playwright() as pw:
    b=pw.chromium.launch(channel='chrome'); pg=b.new_page(viewport={'width':1920,'height':1080})
    pg.goto(p); pg.wait_for_timeout(800)
    n=pg.evaluate("document.querySelectorAll('.slide').length")
    for i in range(1,n+1):
        if i in (1,16): continue
        best=None
        for f in range(30,19,-1):
            ok=pg.evaluate("""([i,f])=>{const m=document.querySelector('#s'+i+' .main'); m.style.setProperty('--fs',f+'px'); const top=m.getBoundingClientRect().top; const bot=Math.max(...[...m.children].map(c=>c.getBoundingClientRect().bottom)); return (bot-top)<=m.clientHeight-30}""",[i,f])
            if ok: best=f;break
        fs[str(i)]=best or 20
    b.close()
json.dump(fs,open('fs.json','w'))
print(fs)
