import os
import time
import msvcrt

def get_offset(chara):
    chara = chara.encode('gbk')  # change charactor to its code(gbk)
    if chara[0] & 0x80 == 0:
        # print('TRUE')
        ret = 32 * ((0xa3 - 0xa1) * 94 + (chara[0] + 128 - 0xa1))  # count offset . (details in the chara encoding file)
        return ret
    # print('fetching : '+str(chara))
    return 32 * (( chara[0] - 0xa1 ) * 94 + ( chara[1] - 0xa1))  # count offset . (details in the chara encoding file)


def show_chara(data):
    ret = []
    layer = []
    for i in range(32):
        if i % 2 == 0:
            layer = []
        for j in range(8):
            if (0x80 >> j) & data[i] == 0:
                layer.append(' ')
            else:
                layer.append('*')
        if i % 2 == 1:
            ret.append(layer)

    return ret


def get_chara_data(HZ,input_file):
    # chi_buffer = None

    # print('now at : '+ str(input_file) )
    offset = get_offset(HZ)
    input_file.seek(offset, 0)
    chi_buffer = input_file.read(32)
    # print('Now at : '+str(chi_buffer))

    output = show_chara(chi_buffer)
    count = 0

    ret = output
    return ret


def printline(array):
    for item in array:
        print('\033[1;31;40m'+str(item), end='')
    print('')


def print_charas(array):
    count = len(array)
    i = 0
    while True:
        os.system('cls')
        for j in range(len(array)):
            printline(array[(i+j) % count])
        time.sleep(0.5)
        i += 1


input_file = open('hzk.dat', 'rb')

HZs = "404 Not Found"
final_out = []

for i in range(16):
    final_out.append([])


for i in range(len(HZs)):
    cdata = get_chara_data(HZs[i], input_file)
    for j in range(len(cdata)):
        for k in range(len(cdata[j])):
            final_out[j].append(cdata[j][k])
    # for line in cdata:
        # final_out.append(line)

print_charas(final_out)


input_file.close()
