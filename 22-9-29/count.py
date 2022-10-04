if __name__ == '__main__':
    filestream = open('train.001', 'r', encoding='GBK')
    freq = {}
    for line in filestream:
        for single in line:
            if single not in freq:
                freq[single] = 0
            if single in freq:
                freq[single] += 1
    print(len(freq))

    rsltfile = open('rslt.txt', 'w', encoding='GBK')

    for char1 in freq:
        for char2 in freq:
            count = 0
            doublec = str(char1)+str(char2)
            # print(doublec)
            # 在这里修正一下指针位置试试
            filestream.seek(0, 0)
            for line in filestream:
                count += line.count(doublec)
            P = count / freq[char1]
            if P != 0:
                # print('writing :'+str(char1) + ' ' + str(char2) + ' ' + str(P))
                rsltfile.write(str(char1) + ' ' + str(char2) + ' ' + str(P) + '\n')

    rsltfile.close()
    filestream.close()
