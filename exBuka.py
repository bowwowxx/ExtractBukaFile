# -*- coding: cp950 -*-

#20120520 extract  buka file
#ref http://de.wikipedia.org/wiki/JPEG_File_Interchange_Format->Dataformat
import os, sys, zipfile, shutil
out = None
i = 1

fn_buka = raw_input('Please Input xx.buka (ex C:\\ibuka\\131073.buka):') #"C:\\Downloads\131073.buka"
target = raw_input('Please Input zip FileName(ex 131073):') #C:\\Downloads\131073'
source_name=os.path.splitext(os.path.basename(fn_buka))[0]
#print source_name
#print target
target=target.strip()
if target=="" :
 target1 = "./" + source_name
else:
 target1 = "./" + target

#zip_name =sys.argv[3] #'131073'
#fz = zipfile.ZipFile(zip_name + '.zip', 'w' ,zipfile.ZIP_DEFLATED)

if os.path.exists(target1):
 shutil.rmtree(target1)

if os.path.exists(fn_buka):
 os.makedirs(target1)
with open(fn_buka, "rb") as f:
    byte = f.read(1)
    while byte != "":
        # begin
        if ord(byte) == 0xff:
            b2 = f.read(1)
            if ord(b2) == 0xd8:
                fn = os.path.join(target1, '%03d.jpg' % i)
                print 'extracting %s' % os.path.basename(fn)
                out = open(fn, 'wb')
                out.write(chr(0xff))
                out.write(chr(0xd8))
                i+=1
                #print 'start'
            elif ord(b2) == 0xd9:
                out.write(chr(0xff))
                out.write(chr(0xd9))
                out.close()
                out = None
                #print 'close'
                #break
            else:
                if not out is None:
                    out.write(byte)
                    out.write(b2)
                    #print 'write'
            byte = f.read(1)
            continue
        else:
            if not out is None:
                out.write(byte)
                #print 'write #2'





        byte = f.read(1)
if not out is None:
    out.close()

if os.path.exists(target1 + '.zip'):
 os.remove(target1 + '.zip')

zf = zipfile.ZipFile(target1 + '.zip','w',zipfile.ZIP_DEFLATED)
os.chdir(target1)
for root, folders, files in os.walk('./'):
        for sfile in files:
            aFile = os.path.join(root, sfile)
            zf.write(aFile)
zf.close()
os.chdir(os.path.abspath(os.pardir))
if os.path.exists(target1):
 shutil.rmtree(target1)

print '%s extract ok!' % os.path.basename(fn_buka)
