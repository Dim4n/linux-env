#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import glob
import subprocess
import random

music_dirs = [u'/home/dima/ya/Музыка/8bit/', u'/home/dima/ya/Музыка/8bit/ksa/', u'/home/dima/ya/Музыка/8bit/lhs/'] 
files = []

for music_dir in music_dirs:
    for filename in glob.glob(music_dir + "*.*"):
        files.append(filename)
		
random.shuffle(files)
		
for f in files:
    loop = random.randint(1, 5)
    print "file = %s, loop = %s" % (f, loop)
    for i in range(loop):
        print "loop number: %s" % i
        p = subprocess.Popen('zxtune123 --alsa = "%s"' % f, shell=True, stdout=subprocess.PIPE)
        p.wait()
