#!/usr/bin/env python
import os, shutil

mainDir = os.getcwd()

f = open("Makefile.local", "r")
VERSIONSTRING = f.readline()[8:-1]
f.close()

packageDir = "package-release/wolfcamql%s" % VERSIONSTRING
os.system("rm -r %s/" % packageDir)
if not os.path.exists(packageDir):
    os.makedirs(packageDir)
os.system("cp -a package-files/* %s/" % packageDir)
os.system("cp COPYING.txt COPYING-backtrace.txt CREDITS-wolfcam.txt CREDITS-openarena.txt README-ioquake3.txt README-wolfcam.txt version unifont-LICENSE.txt %s/" % packageDir)
os.system("cp code/libs/SDL.dll code/libs/backtrace.dll %s/" % packageDir)
os.system("cp build/release-linux-i386/ioquake3.i386 %s/wolfcamql.i386" % packageDir)
os.system("cp -a build/release-linux-i386/baseq3/*.so %s/wolfcam-ql/" % packageDir)
os.system("cp build/release-mingw32-x86/ioquake3.x86.exe %s/wolfcamql.exe" % packageDir)
os.system("cp build/release-mingw32-x86/baseq3/*.dll %s/wolfcam-ql/" % packageDir)
os.system("cp code/libs/macosx/libSDL-1.2.0.dylib %s/" % packageDir)
os.system("cp mac-binaries/wolfcamqlmac %s/" % packageDir)
os.system("cp mac-binaries/*.dylib %s/wolfcam-ql/" % packageDir)
os.system("cp ui/wcmenudef.h %s/wolfcam-ql/ui/" % packageDir)

os.system("rm -r /tmp/wolfcamql-src/")
os.system("mkdir /tmp/wolfcamql-src/")
os.system("cp * /tmp/wolfcamql-src/")
os.system("cp -a code/ ui/ misc/ /tmp/wolfcamql-src/")
os.chdir("/tmp/wolfcamql-src/")
# uhmmm... this is dangerous
os.system("rm -r .hg .hgignore tmp build demos package* code/libs macwolfcambuild update-mac-binaries.sh")
os.chdir("/tmp")
os.system("tar -zcvf wolfcamql-src.tar.gz wolfcamql-src/")

os.chdir(mainDir)
os.system("cp -a /tmp/wolfcamql-src.tar.gz %s/" % packageDir)
os.chdir(packageDir)
os.chdir("..")
os.system("zip -r wolfcamql-%s.zip wolfcamql%s" % (VERSIONSTRING, VERSIONSTRING))

