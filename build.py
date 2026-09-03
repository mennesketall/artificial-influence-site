#!/usr/bin/env python3
import shutil, os
src=os.path.dirname(os.path.abspath(__file__)); dst=os.path.join(src,"public")
if os.path.exists(dst): shutil.rmtree(dst)
os.makedirs(dst)
skip={".git","public","build.py","firebase.json","scale-data.json"}
for item in os.listdir(src):
 if item in skip: continue
 s=os.path.join(src,item); d=os.path.join(dst,item)
 shutil.copytree(s,d) if os.path.isdir(s) else shutil.copy2(s,d)
print(f"Built to {dst}")
