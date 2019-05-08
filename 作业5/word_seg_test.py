import re
import string
import jieba
import jieba.posseg as pseg
def load_word_list():
    max_length = 0
    word_dict = set()
    with open('./data/corpus.dict.txt',encoding='utf-8',errors='ignore') as f:
        for line in f.readlines():
            if(max_length<len(line)):
                max_length = len(line)
            word_dict.add(line.strip())
    return {
        'max_length': max_length,
        'word_dict': word_dict
    }

# 最大正向匹配
def max_left_match(line, word_list):
    new_line = ""
    while line != "":
        length = word_list["max_length"]
        if(line[:length] in word_list["word_dict"]):
            new_line = new_line+line[:length]+"/"
            line = line[length:]
        else:
            while length > 1:
                length-=1
                if(line[:length] in word_list["word_dict"]):
                    break
            new_line = new_line+line[:length]+"/"
            line = line[length:]
    return new_line

# 最大逆向匹配
def max_right_match(line, word_list):
    new_line = ""
    while line != "":
        length = word_list["max_length"]
        if(line[len(line)-length:] in word_list["word_dict"]):
            new_line = line[len(line)-length:]+"/"+new_line
            line = line[:len(line)-length]
        else:
            while length > 1:
                length-=1
                if(line[len(line)-length:] in word_list["word_dict"]):
                    break
            new_line = line[len(line)-length:]+"/"+new_line
            line = line[:len(line)-length]
    return new_line

def calcPRF():
    standard_dict = set()
    with open('./data/corpus.standard.txt',encoding='utf-8',errors='ignore') as f:
        for line in f.readlines():
            for w in line.strip().split(" "):
                standard_dict.add(w)
    FMM_dict = set()
    with open('./data/corpus.out_FMM.txt',encoding='utf-8',errors='ignore') as f:
        for line in f.readlines():
            for w in line.strip('/').split("/"):
                    FMM_dict.add(w)
    BMM_dict = set()
    with open('./data/corpus.out_BMM.txt',encoding='utf-8',errors='ignore') as f:
        for line in f.readlines():
            for w in line.strip('/').split("/"):
                    BMM_dict.add(w)
    BIMM_dict = set()
    with open('./data/corpus.out_BIMM.txt',encoding='utf-8',errors='ignore') as f:
        for line in f.readlines():
            for w in line.strip('/').split("/"):
                    BIMM_dict.add(w)
    
    print(len(standard_dict))
    print("FMM:")
    C = len(FMM_dict.intersection(standard_dict))/len(FMM_dict)
    R = len(FMM_dict.intersection(standard_dict))/len(standard_dict)
    print("Correct ratio: ", C)
    print("Recall retio: ", R)
    print("F-measure: ", 2*C*R/(C+R))
    print("BMM:")
    C = len(BMM_dict.intersection(standard_dict))/len(BMM_dict)
    R = len(BMM_dict.intersection(standard_dict))/len(standard_dict)
    print("Correct ratio: ", C)
    print("Recall retio: ", R)
    print("F-measure: ", 2*C*R/(C+R))
    print("BIMM:")
    C = len(BIMM_dict.intersection(standard_dict))/len(BIMM_dict)
    R = len(BIMM_dict.intersection(standard_dict))/len(standard_dict)
    print("Correct ratio: ", C)
    print("Recall retio: ", R)
    print("F-measure: ", 2*C*R/(C+R))

# 测试
def main():
    words  = []
    word_list = load_word_list()
    # FMM
    outFMM = open('./data/corpus.out_FMM.txt', 'w', encoding='utf-8')
    # BMM
    outBMM = open('./data/corpus.out_BMM.txt', 'w', encoding='utf-8')
    # BIMM
    outBIMM = open('./data/corpus.out_BIMM.txt', 'w', encoding='utf-8')
    for line in open('./data/corpus.sentence.txt',encoding='utf-8',errors='ignore').readlines():
        # 词性标注
        words.extend(pseg.cut(line))
        # 去标点
        illegal_char = string.punctuation + u'.,;《》？！“”‘’@#￥%…&×（）——+【】{};；●，。&～、|\s:：'
        pattern = re.compile('[%s]'%re.escape(illegal_char))
        line = pattern.sub(u'', line)
        # 最大匹配
        lineFMM = max_left_match(line.strip(), word_list)
        lineBMM = max_right_match(line.strip(), word_list)
        lineBIMM = (lineFMM if(len(lineFMM.split('/')) < len(lineBMM.split('/'))) else lineBMM)
        # 结果
        outFMM.write(lineFMM+"\n")
        outBMM.write(lineBMM+"\n")
        outBIMM.write(lineBIMM+"\n")

    # 计算正确率，召回率，测度值
    calcPRF()

    # 输出词性标注
    for w in words:
        print(w.word, w.flag)

if __name__ == '__main__':
    main()