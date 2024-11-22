# 建立所有标签列表labels
def labeltext(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        labels = [line.strip() for line in f]
    return labels


# 将输出概率转化为标签，并输出
def pro2label(filename, writename, threshold):
    # 所有label标签列表
    labels = labeltext('data/data/label_list.txt')
    # print(labels)
    with open(filename,'r', encoding='utf-8') as f:
        with open(writename,'w', encoding='utf-8') as w:
            for i, line in enumerate(f):
                # 预测输入标签列表
                label = []
                # 按空格分隔概率值
                pro = [float(value) for value in line.split()]
                # print(pro)
                for j,k in enumerate(pro):
                    if pro[30] < threshold:
                        if k > threshold:
                            label.append(labels[j])
                    # 只标记No_Mentioned
                    else:
                        label = [labels[30]]
                for a,lab in enumerate(label):
                    if a < len(label) - 1:
                        w.write(lab + ",")
                    else:
                        w.write(lab)
                w.write('\n')

pro2label('result\\test_results.tsv','result\\yjq5.txt',0.05)