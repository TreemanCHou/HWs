import sys
from tqdm import tqdm

if __name__ == '__main__':
    filestream = open('train.001', 'r', encoding='GBK')
    freq = {}
    for line in filestream:
        for single in line:
            if single not in freq:
                freq[single] = 0
            if single in freq:
                freq[single] += 1
    total = len(freq)
    rsltfile = open('rslt.txt', 'w', encoding='GBK')

    mark_str = '\n\t\r `1234567890-=~!@#$%^&*()_+,./;\'[]\\<>?:\"{}|～！…￥（）——`～{}|·「」、；‘’“”，。/《》？'
    combine_dict = {}
    print(total)
    filestream.seek(0)
    print('READING&COUNTING: ')
    for line in tqdm(filestream):
        for i in range(len(line)-1):
            # print('COMBINATION:'+str(line[i]) + ' AND ' + str(line[i+1]))
            if line[i] in mark_str or line[i+1] in mark_str:
                continue
            comb = str(line[i]) + str(line[i+1])
            if comb not in combine_dict:
                combine_dict[comb] = 1
            else:
                combine_dict[comb] += 1
    print('WRITING :', end='')
    for item in tqdm(list(combine_dict)):
        print(item+' : '+str(f"{combine_dict[item]/freq[item[0]]:.20f}"))
        rsltfile.write(str(item[0]) + ' ' + str(item[1]) + ' ' + str(f"{combine_dict[item]/freq[item[0]]:.20f}") + '\r\n')

    rsltfile.close()
    filestream.close()
