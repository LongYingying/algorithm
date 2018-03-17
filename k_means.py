# -*- coding: utf-8 -*-
import  math
import  random
import matplotlib.pyplot as plt
from matplotlib import colors as m_colors
#生成样本点
def gen_random_sample(n_feat,lower,upper):
    sample=[random.uniform(lower,upper) for _ in range(n_feat)]
    return sample
#样本个数
n_samples=1000
#特征个数（特征维度）
n_feat=2
#特征数值范围
lower=0
upper=200
#聚类个数
n_cluster=4
#聚类样本点
samples=[gen_random_sample(n_feat,lower,upper) for _ in range(n_samples)]

#收敛阈值
cutoff=0.1
#聚类中心
cluster=[samples[random.randint(0,n_samples)] for _ in range(n_cluster)]

#重新计算聚类中心：
new_cluster=[]
#计算两点间距离
def cal_distance(a,b):
    s_sum=0
    for i in range(n_feat):
        s_sum+=pow(a[i]-b[i],2)
    dis=math.sqrt(s_sum)
    return dis
cutoff_dis=[1 for _ in cluster]
print(max(cutoff_dis))
#迭代次数
n_loop=1
while(max(cutoff_dis)> cutoff ):

    # 样本点图
    #for i_sample in samples:
        #x_sample.append(i_sample[0])
       # y_sample.append(i_sample[1])
    #plt.scatter(x_sample, y_sample)
    # 画出聚类中心
    #for cluster_point in cluster:
        #plt.scatter(cluster_point[0], cluster_point[1], c='red')
    #plt.title('samples&clusters(iteration:{})'.format(n_loop))
    #plt.show()
    #分类lists
    lists=[[]for _ in range(n_cluster)]
    #对样本遍历进行分类
    for sample_point in samples:
        dis=[cal_distance(sample_point,cluster_point) for cluster_point in cluster]
        min_dis=min(dis)
        index_cluster=dis.index(min_dis)
        lists[index_cluster].append(sample_point)
    #print(dis)

    print(lists)
    #设置不同聚类点的颜色
    color_names=list(m_colors.cnames)

    for i in lists:
        color_=[color_names[lists.index(i)]]*len(i)
        x=[]
        y=[]
        for classify_point in i:
            x.append(classify_point[0])
            y.append(classify_point[1])
        plt.scatter(x,y,c=color_)
        #重新计算聚集点中心
        new_cluster.append([sum(x)/len(x),sum(y)/len(y)])
        #对新产生的聚类中心作图
    for cluster_point in new_cluster:
        plt.scatter(cluster_point[0], cluster_point[1], c='red')
    plt.title('output of k_means(iteration:{})'.format(n_loop))
    plt.show()
    print(len(cluster),len(new_cluster))
    #计算新旧聚类中心的偏移距离
    for i in range(len(cluster)):
        print(i)
        cutoff_dis[i]=cal_distance(cluster[i],new_cluster[i])

    print('cluster',cluster)
    print('new_cluster:',new_cluster)
    print('cutoff_dis:',cutoff_dis)
    #对聚类中心重新赋值
    for i in range(len(cluster)):
        cluster[i]=new_cluster[i]

    new_cluster.clear()
    n_loop+=1




