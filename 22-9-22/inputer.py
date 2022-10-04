import msvcrt
import os


def load():
    ret = {}
    filestream = open('rslt.txt', 'r', encoding='GBK')
    for line in filestream:
        arr = line.strip('\n').split(' ')
        ret[arr[0]] = arr[1:]
    filestream.close()
    return ret


class inputer:
    def __init__(self):
        self.choose_list = []
        self.input_list = []
        self.result = []
        self.current_page = 0
        self.position = 0
        self.choice = -1

    def new_input_list(self, inputlist):
        self.input_list = inputlist

    def new_choose_list(self, choose_list: list):
        self.choose_list = choose_list

    def next_page(self):
        if self.position + 10 < len(self.choose_list):
            self.position += 10
            self.print_candi()
        else:
            pass

    def last_page(self):
        if self.position != 0:
            self.position -= 10
            self.print_candi()
        else:
            pass

    def print_candi(self):
        os.system('cls')
        print('INPUT :', end=' ')
        for item in self.result:
            print(item, end=' ')
        for item in self.input_list[len(self.result):]:
            print(item, end='')
        print(' ')
        for i in range(10):
            if (self.position + i) >= len(self.choose_list):
                # print('[DEBUG]inputer.print_candi returned .')
                break
            else:
                print(str(i+1)+'.'+self.choose_list[self.position+i]+'   ', end='')
        print('\n=====================================================================')
        print('CHOOSE:')

    def choose_candidate(self):
        # print('[DEBUG]choose_candidate printing:')
        self.position = 0
        self.print_candi()
        action = msvcrt.getch()
        ret = ""
        while True:
            # print('[DEBUG]choose_candidate\'s Loop .')
            if action == b'=':
                self.next_page()
            if action == b'-':
                self.last_page()
            if action in b"123456789":
                ret += self.choose_list[self.position+int(action)-1]
                self.result.append(ret)
                break
            if action == b'0':
                ret += self.choose_list[self.position + 10 - 1]
                self.result.append(ret)
                break
            if action == b' ':
                ret += self.choose_list[self.position + 1 - 1]
                self.result.append(ret)
                break
            else:
                pass
                # self.print_candi()
                # print('Wrong Input . Chose again .')
            action = msvcrt.getch()
        # print("[DEBUG]choose_candi:returning : \""+str(ret)+"\"")
        return ret


if __name__ == "__main__":
    diction = load()
    while True:
        input_method = inputer()
        os.system('cls')
        inputs = input('Type:')
        inputs = inputs.split(' ')
        result = ""
        input_method.new_input_list(inputs)  # Add input string tu the inputer .
        for item in inputs:
            # print('[DEBUG]Now at:'+str(item) + 'in total : '+str(inputs))
            if item in diction:
                candidate = diction[item]
                input_method.new_choose_list(candidate)
                result += input_method.choose_candidate()
                # print('[DEBUG]main: Adding to result . Now is : ' + result)
            else:
                print('bug')
        input_method.print_candi()
        print('\nRESULT:'+str(result))
        # print('\n\npress any key to continue ... ')
        msvcrt.getch()



