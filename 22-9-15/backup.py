def HZOffset(HZ):
    HZ = HZ.encode("gbk")
    if HZ[0]&0x80==0:
        return 32 * ((0xa3 - 0xa1) * 94 + (HZ[0]+128 - 0xa1))
    return 32 * ((HZ[0] - 0xa1) * 94 + (HZ[1] - 0xa1))


def Show(HZBuff):
    for i in range(32):
        for j in range(8):
            if (0x80 >> j) & HZBuff[i] == 0:
                print(" ", end="")
            else:
                print("*", end="")
        if i % 2 == 1:
            print("")


def ShowHZ(HZ,Handle):
    Offset = HZOffset(HZ)
    In.seek(Offset, 0)
    HZBuff = In.read(32)
    Show(HZBuff)


def GetHZArray(HZ[i],In,HZsArray):

def Link(HZsArray,HZArray):

def ShowHZs(HZsArray):

HZs = "fxxking crazy"
In = open("hzk.dat", "rb")
HZsArray=[]
for i in range(len(HZs)):
    GetHZArray(HZs[i],In,HZsArray)
    Link(HZsArray,HZsArray)
In.close()

ShowHZs(HZsArray)