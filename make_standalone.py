# Embeds everything in assets/ into each page -> standalone/ (single-file versions)
import re,base64,os
os.makedirs('standalone',exist_ok=True)
for f in ['mira-birthday-navy.html','mira-birthday-pink.html']:
    s=open(f).read()
    def r(m):
        p=m.group(1); t='jpeg' if p.endswith('.jpg') else 'png'
        return f'data:image/{t};base64,'+base64.b64encode(open(p,'rb').read()).decode()
    open('standalone/'+f,'w').write(re.sub(r'(assets/[a-z_0-9]+\.(?:png|jpg))',r,s))
