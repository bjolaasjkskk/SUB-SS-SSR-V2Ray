#!/usr/bin/python
import base64
import time
import sys,os
import socket

configfilepath='configfile/'

def ToBase64(file, txt):
    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64_data = base64.b64encode(image_data)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()

def ToFile(txt, file):
    with open(txt, 'r') as fileObj:
        base64_data = fileObj.read()
        ori_image_data = base64.b64decode(base64_data)
        fout = open(file, 'wb')
        fout.write(ori_image_data)
        fout.close()

def merge(file1, file2,file3):
    f3 = open(file3, 'w', encoding='utf-8')
    with open(file1, 'r', encoding='utf-8') as f1:
        for i in f1:
            f3.write(i)
    with open(file2, 'r', encoding='utf-8') as f2:
        for i in f2:
            f3.write(i)

#merge("url_ss_ssr.txt", "url_v2ray.txt","url_all.txt")
    
#生成指定文件名的base64文件
base64file_all=configfilepath+"base64_all.txt"
links_file=configfilepath+"url_all.txt"

if os.path.exists(links_file):
    if os.path.exists(links_file+'.bak'):
       os.remove(links_file+'.bak')
    os.rename(links_file,links_file+'.bak')
merge(configfilepath+"url_ss_ssr.txt", configfilepath+"url_v2ray.txt",configfilepath+"url_all.txt")
ToBase64(links_file,base64file_all)
