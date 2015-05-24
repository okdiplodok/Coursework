#coding:utf-8
import codecs
import os

f  = codecs.open(u'notind.csv', 'r', 'utf-8')
l = codecs.open(u'notind_def.csv', 'a', 'utf-8')

for line in f:
    for_final = line.strip()
    n = 0
    line = line.split(u'\t')
    print line[0]
    reg = u'<p><b>' + line[0].upper() + u'</b>'
    #if line[0] not in words
    for root, dirs, files in os.walk(u'.'):
        if n == 1:
            break
        else:
            for fname in files:
                if root.endswith(line[0][0]):
                    s = codecs.open(os.path.join(root,fname), 'r', 'utf-8').read()
                    if s.startswith(reg):
                        n += 1
                        print line[0] + u'---' + s
                        l.write(for_final + u'\t' + s + u'\r\n')
                        break
                        
f.close()
