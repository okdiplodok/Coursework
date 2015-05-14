#coding:utf-8
import codecs
import re
import os

#на вход - файл и частотный словарь Ляшевской и Шарова 
#(электронная версия доступна по ссылке http://dict.ruslang.ru/freq.php). На выходе - файл формата
#"лемма ipm вхождение_из_текста". Поиск слов, который НЕТ в словаре (с вычетом имен собственных и глаголов)
my_d = {}
g = codecs.open(u'fr2011.csv', 'r', 'utf-8')
for line in g:
    line = line.strip()
    line = line.split(u'\t')
    my_d[line[0]] = line[1]
        
check = set()
def rare_words(nfile):
    new = codecs.open(u'filter0423.csv', 'a', 'utf-8')
    excl = set([u'чь', u'ие', u'ец', u'ье', u'ик', u'ок', u'ек', u'ий', u'ый', u'ой', u'ач'])
    excl1 = set([u'очка', u'ство', u'ость', u'ечка', u'ушка', u'тель'])
    global check
    global my_d
    s = codecs.open(nfile, 'r', 'utf-8-sig')
    for line in s:
        res = line.strip()
        line = line.split(u'\t')
        search = line[0]
        token = line[2]
        if search not in check and my_d[search] == u's' and search[-2:] not in excl and search[-3:] != u'ица' and search[-4:] not in excl1 and token[0] not in u'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ' and len(search) > 3:
            check.add(search)
            #return m.group(1)
            new.write(res + u'\r\n')
    s.close()
    new.close()


ss = rare_words(u'haha0423.csv')
f  = codecs.open(u'filter0423.csv', 'r', 'utf-8')
l = codecs.open(u'filter0423_def.csv', 'a', 'utf-8')
z = codecs.open(u'haha_def.csv', 'r', 'utf-8')
words = set()
for line1 in z:
    line1 = line1.split(u'\t')[0]
    words.add(line1)
    
for line in f:
    for_final = line.strip()
    n = 0
    line = line.split(u'\t')
    print line[0]
    reg = u'<p><b>' + line[0].upper() + u'</b>'
    if line[0] not in words:
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
z.close()
