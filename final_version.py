#ф-я делит цельный текст романа на главы и распределяет файлы по папкам (для каждого тома - своя папка)
def files_create(fname, x, z):
    f = codecs.open(fname, 'r', 'utf-8')
    n = 0
    l = 1
    arr = []
    for line in f:
        if line.startswith(u'<h3'):
            n += 1
            final = n + x
            name_dirs = u'Part_' + str(final)
            if not os.path.exists(name_dirs):
                os.makedirs(name_dirs)
            arr.append(line)
        elif n == 0:
            arr.append(line)
        elif line.startswith(u'<div class="section"'):
            if arr[-2].startswith(u'<h3'):
                arr.append(line)
            else:
                name = str(l + z) + u'.txt'
                dirs = u'./' + name_dirs
                s = codecs.open(os.path.join(dirs, name), 'a', 'utf-8')
                for element in arr:
                    s.write(element)
                s.close()
                arr = []
                arr.append(line)
                l += 1
        else:
            arr.append(line)
    new_name = str(l + z) + u'.txt'
    m = codecs.open(os.path.join(dirs, new_name), 'a', 'utf-8')
    for element in arr:
        m.write(element)
    m.close()
    return l

#first = files_create(u'09.htm', 0, 0)
#second = files_create(u'12.htm', 11, 259)

#ф-я запускает mystem и производит морфологическую разметку (приписывает леммы и копирует все из входных файлов на выход)
def annotation():
    count = 1
    if not os.path.exists(u'mystem'):
        os.makedirs(u'mystem')
    app = "C:\\Users\\diplodok\\Desktop\\Fipl\\Paper\\mystem.exe"
    for root, dirs, files in os.walk(u'.'):
        for fname in files:
            if fname.endswith(u'.txt'):
                new_name = u'C:\\Users\\diplodok\\Desktop\\Fipl\\War_and_Peace\\mystem\\' + u'a' + str(count) + u'.txt'
                route = u'"' + app + u' -cd ' + os.path.join(root, fname) + u' ' + new_name + u'"'
                print route
                os.system(route)
                count += 1

#result = annotation()
