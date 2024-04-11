import requests as r
import os, re
from bs4 import BeautifulSoup as b
user_agent={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
img_name=input("Enter image name to download: ")
url=f'https://www.google.com/search?q={img_name}&source=lnms&tbm=isch'
res=r.get(url, headers=user_agent).text
pattern = r'\"https://[^"]+\.jpg\"'
images=re.findall(pattern,res)
print(f"Total images = {len(images)}")
no_of_img=int(input("enter no of images do you want: "))
os.makedirs(img_name, exist_ok=True)
os.chdir(img_name)
for i in images[:no_of_img]:
    img_name=i.split('/')[-1].replace('"','')
    img_url=i.replace('"','')
    with open(img_name, 'wb') as f:
        f.write(r.get(img_url).content)
    


