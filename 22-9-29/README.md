## 说明
___
- 两个py文件：
  - <font color='10bbff'>[count.py]</font>统计<font color='10FF10'>[train.001]</font>里的文本，并给出所有的两个汉字组合的概率，存储于<font color='10FF10'>[rslt.txt]</font>中。
  - <font color='10bbff'>[main.py]</font>是句子生成算法主体程序。由于已经统计好<font color='10FF10'>[rslt.txt]</font>，直接运行<font color='10bbff'>[main.py]</font>即可。
  - <font color='red'>[注意1]</font><font color='orange'>由于训练语料train.001规模较小，
  很多常见组合在语料中没有涉及或比例偏低，生成的句子不尽如人意。</font>
  - <font color='red'>[注意2]</font><font color='10bbff'>[main.py]</font><font color='orange'>里面有很多测试时加入的print，可以比较直观地看出程序运行过程。如果不想看，请把</font>
<font color='10bbff'>[main.py]</font>开头的DEBUG_MODE设为false.
- 文本文件：
  - <font color='10FF10'>[py_hz.txt]</font> 是拼音与汉字对照表，用于构建基础输入法，根据用户输入的拼音建造汉字候选列表。
  - <font color='10FF10'>[rslt.txt]</font> 是经过<font color='10bbff'>[count.py]</font>处理后得出的2-gram两字组合概率表。
<font color='10bbff'>[main.py]</font>会直接根据其中数据构造概率决策链路。
  - <font color='10FF10'>[train.001]</font> 训练语料 provided by 荀恩东。如果希望得到更好的效果可以换用更大的语料。保持名字是train.001并重新运行<font color='10bbff'>[count.py]</font>
