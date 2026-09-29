from PIL import Image
import numpy as np
from scipy import ndimage as ndi
U='/mnt/user-data/uploads/'
def cut(src,box,name,bg,tol,maxw=420):
    im=Image.open(U+src).convert('RGBA')
    if box: im=im.crop(box)
    a=np.array(im).astype(int)
    d=np.abs(a[:,:,:3]-np.array(bg)).max(axis=2)
    cand=d<=tol
    lab,_=ndi.label(cand)
    edge=set(lab[0,:])|set(lab[-1,:])|set(lab[:,0])|set(lab[:,-1]); edge.discard(0)
    m=np.isin(lab,list(edge))
    m=ndi.binary_dilation(m,iterations=1)&cand|m
    fg=~m
    if name not in('kitty_cake','plush','happy_birthday'):
        l2,n=ndi.label(ndi.binary_dilation(fg,iterations=3))
        sizes=ndi.sum(fg,l2,range(1,n+1)); keep=l2==(1+int(np.argmax(sizes)))
        fg=fg&keep
    h,w=fg.shape
    if name=='tag':
        fg[80:,:85]=False
    if name=='disco':
        yy,xx=np.ogrid[:h,:w]; fg&=((xx-w/2)**2+(yy-h/2)**2)<=(min(w,h)/2)**2
    a[:,:,3]=np.where(fg,255,0)
    out=Image.fromarray(a.astype('uint8'))
    bb=out.getchannel('A').getbbox()
    out=out.crop(bb)
    if out.width>maxw: out=out.resize((maxw,int(out.height*maxw/out.width)),Image.LANCZOS)
    out.save('assets/'+name+'.png',optimize=True)
    print(name,out.size)
S2='Screenshot_2026-09-28_at_10_07_58_PM.png'
cut('Screenshot_2026-09-28_at_10_07_27_PM.png',None,'kitty_cake',(229,229,229),10)
cut('Screenshot_2026-09-28_at_10_08_40_PM.png',None,'plush',(255,255,255),14)
W=(255,255,255)
cut(S2,(40,25,310,175),'tag',W,14,300)
cut(S2,(280,25,372,240),'party_hat',W,14,140)
cut(S2,(372,25,582,232),'disco',W,14,220)
cut(S2,(22,222,592,445),'happy_birthday',W,14,560)
cut(S2,(30,452,375,676),'camera',W,14,300)
cut(S2,(376,438,540,738),'iloveyou',W,14,170)
cut(S2,(28,678,455,1040),'cake',W,14,400)
cut(S2,(30,688,130,795),'sun',W,14,100)
cut(S2,(385,745,520,852),'green_star',W,14,120)
cut(S2,(25,105,160,235),'blue_star',W,14,120)
cut(S2,(25,222,120,312),'gold_star',W,14,90)
