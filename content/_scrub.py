#!/usr/bin/env python3
"""Strip all metadata from exported PNGs and stamp operator authorship.
Removes every ancillary/text/time/software chunk (no tool, AI, or source trace),
keeps only the pixels, and writes neutral operator credits + a virtual path.
Pure stdlib, no dependencies. Usage: python3 _scrub.py file1.png file2.png ...
"""
import sys, struct, zlib
SIG=b'\x89PNG\r\n\x1a\n'
KEEP={b'IHDR',b'PLTE',b'tRNS',b'sRGB',b'IDAT',b'IEND'}   # critical render chunks only
META=[('Author','Tibi Serbaneci'),
      ('Copyright','(c) 2026 Tibi Serbaneci'),
      ('Software','Ultron Content Studio'),
      ('Source','ultron-content/exports')]               # virtual path, no real origin
def _c(typ,data): return struct.pack('>I',len(data))+typ+data+struct.pack('>I',zlib.crc32(typ+data)&0xffffffff)
def _t(k,v): return _c(b'tEXt',k.encode('latin-1')+b'\x00'+v.encode('latin-1'))
def scrub(path):
    raw=open(path,'rb').read()
    if raw[:8]!=SIG: print("skip (not PNG):",path); return
    out=bytearray(SIG); i=8
    while i<len(raw):
        ln=struct.unpack('>I',raw[i:i+4])[0]; typ=raw[i+4:i+8]; data=raw[i+8:i+8+ln]; i+=12+ln
        if typ==b'IEND':
            for k,v in META: out+=_t(k,v)
            out+=_c(b'IEND',b''); break
        if typ in KEEP: out+=_c(typ,data)
    open(path,'wb').write(out)
    print("scrubbed:",path)
if __name__=='__main__':
    for p in sys.argv[1:]: scrub(p)
