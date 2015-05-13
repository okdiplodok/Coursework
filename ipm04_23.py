#coding:utf-8
import codecs
import re

#на вход - файл и частотный словарь Ляшевской и Шарова 
#(электронная версия доступна по ссылке http://dict.ruslang.ru/freq.php). На выходе - файл формата
#"лемма ipm вхождение_из_текста". Поиск слов, который НЕТ в словаре (с вычетом имен собственных и глаголов)
my_d = {}
g = codecs.open(u'fr2011.csv', 'r', 'utf-8')
for line in g:
    line = line.strip()
    line = line.split(u'\t')
    if (line[1] == u's' or line[1] == u'a') and int(float(line[2])) <= 2.3:
        my_d[line[0]] = line[2]
        
check = set()
def rare_words(nfile):
    excl = set([u'ть', u'чь', u'ти', u'ся', u'ие', u'ок', u'ек'])
    global check
    global my_d
    r = re.compile(u'([а-яА-Я]+){([а-я]+)}', flags=re.U)
    s = codecs.open(nfile, 'r', 'utf-8-sig')
    for line in s:
        line = line.split()
        for element in line:
            m = r.search(element)
            if m != None:
                if m.group(2) in my_d and m.group(2) not in check:
                    check.add(m.group(2))
                    #return m.group(1)
                    return m.group(2) + u'\t' + my_d[m.group(2)] + u'\t' + m.group(1) + u'\r\n'
    s.close()

#ф-я rare_write() на каждом шаге цикла читает размеченный файл и вызывает ф-ю rare_words()
def rare_write():
    n = 1
    new = codecs.open(u'haha0408.csv', 'a', 'utf-8')
    while n <= 361:
        filen = u'C:\\Users\\diplodok\\Desktop\\Fipl\\War_and_Peace\\mystem\\a' + str(n) + u'.txt'
        el = rare_words(filen)
        if el != None:
            new.write(el)
        n += 1
    new.close()

#ss = rare_write()

#ф-я собирает определения из файла комментариев Соболева. На выходе - файл формата 'lemma  ipm  token  def'
def def_collect():         
    y = codecs.open('haha0408.csv', 'r', 'utf-8')
    g = codecs.open(u'def.txt', 'r', 'utf-8').readlines()
    f = codecs.open(u'haha_def.csv', 'a', 'utf-8')
    for line in y:
        res = line.strip()
        word = line.split('\t')[0]
        #ipm = line.split(';')[1]
        for definition in g:
            n = definition.split(' -')[0]
            if n.startswith(word) and len(word) > 2:
                line1 = res + u'\t' + definition + u'\r\n'
                print line1
                f.write(line1)
    y.close()
    f.close()

#sss = def_collect()

