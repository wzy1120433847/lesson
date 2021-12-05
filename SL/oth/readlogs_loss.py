# 作者:ZhaoYu Wang
# 日期:2021年10月04日
import matplotlib.pyplot as plt
plt.title("The performance of Loss function under Different Batch-size", fontsize=10)  # 标题，并设定字号大小
plt.xlabel(u'Epoch', fontsize=14)  # 设置x轴，并设定字号大小
plt.ylabel(u'Loss', fontsize=14)  # 设置y轴，并设定字号大小
color=['yellow','red','green','blue']
import os
path = r'C:\\Users\\HP\\Desktop\\Logs\\'
c=0
for filename in os.listdir(path):
    c+=1
    E=[]
    L=[]
    label=filename[filename.find('wpdc_batchsize')+14:filename.find('.')]
    print(label)
    for line in open(path+filename,"r",encoding='UTF-8'):
        if 'Val' in line[:]:
            index_epoch_1= line[:].find('Val: [')
            index_epoch_2= line[:].find(']	Loss')

            Epoch=line[index_epoch_1+6:index_epoch_2-6]
            epoch=int(Epoch)
            E.append(epoch)

            index_loss = line[:].find('Loss')
            Loss=line[index_loss+5:index_loss+11]
            loss=float(Loss)
            L.append(loss)

    plt.plot(E,L,color=color[c],linewidth=2,linestyle='-',label=label)
    plt.legend(loc=2)#图例展示位置，数字代表第几象限
    plt.savefig("batch_size.png")
