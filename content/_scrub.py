#!/usr/bin/env python3
"""Strip all metadata from exports (PNG / PDF / MP4) and stamp operator authorship.
Removes every ancillary/text/time/software chunk (no tool, AI, or source trace),
keeps only the pixels, and writes neutral operator credits + a virtual path.
Stdlib only for PNG and PDF; MP4 stream-copies through ffmpeg when one is available.
Usage: python3 _scrub.py file1.png film.mp4 deck.pdf ...
"""
import sys, struct, zlib, re
SIG=b'\x89PNG\r\n\x1a\n'
KEEP={b'IHDR',b'PLTE',b'tRNS',b'sRGB',b'IDAT',b'IEND'}   # critical render chunks only
META=[('Author','Tibi Serbaneci'),
      ('Copyright','(c) 2026 Tibi Serbaneci'),
      ('Software','Ultron Content Studio'),
      ('Source','ultron-content/exports')]               # virtual path, no real origin
def _c(typ,data): return struct.pack('>I',len(data))+typ+data+struct.pack('>I',zlib.crc32(typ+data)&0xffffffff)
def _t(k,v): return _c(b'tEXt',k.encode('latin-1')+b'\x00'+v.encode('latin-1'))
def scrub_pdf(path):
    """Neutralize PDF Info Producer/Creator (drops renderer names like Skia/Chromium).
    Replacements are the exact same byte length, so the xref table stays valid."""
    raw=open(path,'rb').read()
    if raw[:5]!=b'%PDF-': print("skip (not PDF):",path); return
    def neutralize(m):
        key,inner=m.group(1),m.group(2)
        base=b'Ultron Studio' if key==b'Producer' else b'Ultron'
        nv=base.ljust(len(inner))[:len(inner)]      # exact same length -> offsets unchanged
        return m.group(0).replace(b'('+inner+b')',b'('+nv+b')',1)
    raw=re.sub(rb'/(Producer|Creator)\s*\(([^)]*)\)',neutralize,raw)
    open(path,'wb').write(raw)
    print("scrubbed (pdf):",path)
def scrub_mp4(path):
    """Re-mux an MP4 with no metadata and operator credits stamped on.
    Atoms cannot be edited in place (moov holds chunk offsets into mdat, so resizing it
    corrupts them), so we stream-copy instead: no re-encode, no quality loss, and
    -bitexact keeps ffmpeg from writing its own encoder string into udta."""
    import subprocess,os,shutil
    ff=shutil.which('ffmpeg')
    if not ff:
        try:
            import imageio_ffmpeg; ff=imageio_ffmpeg.get_ffmpeg_exe()
        except ImportError: print("skip (no ffmpeg):",path); return
    tmp=path+'.scrub.mp4'
    cmd=[ff,'-y','-i',path,'-c','copy','-map_metadata','-1',
         '-fflags','+bitexact','-flags:v','+bitexact','-flags:a','+bitexact',
         '-movflags','+faststart']
    for k,v in [('artist',META[0][1]),('author',META[0][1]),('copyright',META[1][1]),
                ('encoder',META[2][1]),('comment',META[3][1])]:
        cmd+=['-metadata',f'{k}={v}']
    cmd.append(tmp)
    r=subprocess.run(cmd,capture_output=True)
    if r.returncode!=0 or not os.path.exists(tmp):
        print("skip (mux failed):",path); return
    os.replace(tmp,path)
    # -bitexact above normally stops the mov muxer writing its own 'Lavf<version>' encoder
    # atom. Belt and braces for ffmpeg builds that write it anyway: overwrite in place at
    # identical byte length, which leaves every chunk offset valid. Usually a no-op.
    # (Do not verify this with `-f ffmetadata`, which adds an encoder line of its own and
    #  makes a clean file look stamped. Read the raw bytes or the ffmpeg header dump.)
    raw=open(path,'rb').read()
    def same_len(m):
        return b'Ultron Content Studio'.ljust(len(m.group(0)))[:len(m.group(0))]
    patched,n=re.subn(rb'Lavf[0-9]+\.[0-9]+\.[0-9]+',same_len,raw)
    if n: open(path,'wb').write(patched)
    print(f"scrubbed (mp4): {path}{f' [{n} encoder tag]' if n else ''}")
def scrub(path):
    if path.lower().endswith('.pdf'): return scrub_pdf(path)
    if path.lower().endswith(('.mp4','.m4v','.mov')): return scrub_mp4(path)
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
