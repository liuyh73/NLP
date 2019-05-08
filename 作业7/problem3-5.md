**Problem 3**

使用二值化多项式朴素贝叶斯不会改变最终的判断，在这种模式下，n+ = 8，p(+|"predictable with no originality")=(2/5)*(1/28)^2=0.0005102，此计算结果依然要小于p(-|"predictable with no originality")

**Problem 4**

在add-1拉普拉斯平滑中，我们假设我们看到了所有的单词，不论他在原始的集合中是否出现，因此，分母中我们加上|V|。测试集没有在训练集中的单词我们标记为“unk”。

**Problem 5**

当c为+时，p(c|"predictable with no originality")=0，因为p("predictable"|+)=p("no"|+)=0