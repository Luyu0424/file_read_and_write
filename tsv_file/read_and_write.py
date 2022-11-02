import pandas as pd
import csv
#read
text=pd.read_csv('_read_file.tsv',sep='\t',header=0)

#content_show
for j in text:
    print(j)

write_list=[]
for i,j,k in zip(text['source'],text['prediction'],text['target']):
    write_list.append([i,j,k])


#write
with open('_write_file.tsv', 'w',encoding='utf-8',newline='') as f:
    tsv_w = csv.writer(f, delimiter='\t')
    tsv_w.writerow(['source', 'prediction', 'target'])  # 单行写入
    tsv_w.writerows(write_list)  # 多行写入

