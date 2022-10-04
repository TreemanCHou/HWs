import re

def process():
    filestraeam = open('PINYIN.txt', 'r', encoding='GBK')
    diction = {}
    for line in filestraeam:
        # print(line)
        key = line[0]
        value = line[2:]
        value = re.sub('\d', '', value)
        value = re.sub('\n', '', value)
        value = value.split(' ')

        diction[key] = value

    # for item in diction:
    #     print(item,diction[item])

    dict2 = {}

    for item in diction:
        dict2[item] = 0

    for line in filestraeam:
        for item in line:
            if item in dict2:
                dict2[item] += 1

    # Now , Construct a new dict for PINYIN and its frequency
    already_done = []
    for key in diction:
        value = diction[key]
        for item in value:
            if item not in already_done:
                already_done.append(item)

    # print(already_done)
    # print(diction)
    pinyin_dict = {}
    for item in already_done:
        candi_chara = {}
        print('Analyzing: '+str(item))
        for key in diction:
            if item in diction[key]:
                candi_chara[key] = 0

        pinyin_dict[item] = candi_chara
        print(item, pinyin_dict[item])

    # Now : Analyse the frequency .

    filestraeam.close()

    filestream2 = open('train.001', 'r', encoding='GBK')

    freq = {}
    for line in filestream2:
        for single in line:
            if single not in freq:
                freq[single] = 0
            if single in freq:
                freq[single] += 1

    for item in freq:
        for pinyin in pinyin_dict:
            if item in pinyin_dict[pinyin]:
                pinyin_dict[pinyin][item] = freq[item]

    # print(pinyin_dict)
    # Now : Sort by frequency .
    for item in pinyin_dict:
        pinyin_dict[item] = sorted(pinyin_dict[item].items(), key=lambda x: x[1], reverse=True)
        pinyin_dict[item] = dict(pinyin_dict[item])
    print(pinyin_dict)
    filestream2.close()

    filestream3 = open('rslt.txt', 'w', encoding='GBK')
    for item in pinyin_dict:
        wstr = str(item)
        for chara in pinyin_dict[item]:
            wstr += ' '+str(chara)
        filestream3.writelines(wstr+'\n')
    filestream3.close()
    # for item in dict2:
    #     print(item,dict2[item])

process()
