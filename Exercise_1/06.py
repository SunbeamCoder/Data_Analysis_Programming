# DangQuocToan_20051051_51
with open('D:\GT\DangQuocToan_20051051\in.txt') as rf:
    line = rf.readline()
    index = 1
    while line:
        print('Line {}: {}'.format(index, line))
        index += 1
        line = rf.readline()