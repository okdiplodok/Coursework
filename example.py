# -*- coding: utf-8 -*-
import codecs
import re

n = 5
check = set()
while n <= 5:
    fname = u'vol.' + str(n) + u'.xml'
    print fname
    f = codecs.open(fname, 'r', 'utf-8').readlines()
    l_def = codecs.open(u'extra_for_sam.csv', 'r', 'utf-8')
    s = codecs.open(u'extra_for_sam_sample.csv', 'a', 'utf-8')
    reg = re.compile(u'(<p id="p[0-9]+">)?([^\.\?!]*\\b1805\\b[^\.\?!]*[\.\?!])')
    for line in l_def:
        res = line.strip()
        line = line.split(u'\t')
        reg = u'(<p id="p[0-9]+">)?([^\.\?!]*\\b' + line[2] + u'\\b[^\.\?!]*[\.\?!])'
        r = re.compile(reg, flags=re.U)
        for line1 in f:
            m = r.search(line1)
            if m != None:
                if m.group(1) is not None:
                    if line[0] not in check:
                        print m.group(1) + m.group(2)
                        s.write(res + u'\t' + m.group(1) + m.group(2) + u'\r\n')
                        total += 1
                        check.add(line[0])
                else:
                    if line[0] not in check:
                        print m.group(2)
                        s.write(res + u'\t' + m.group(2) + u'\r\n')
                        check.add(line[0])
    n -= 1
s.close()
