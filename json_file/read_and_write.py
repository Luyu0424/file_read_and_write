import json


all_d=[]
num=0
#read
with open('_train.jsonl','r',encoding='utf-8') as f:
    for line in f:
        lin=json.loads(line)
        all_d.append(lin)

new_dict=all_d[:10]
print(len(new_dict))

#write
with open('_saved.jsonl','w',encoding='utf-8')as f:
    for value in new_dict:
        a=json.dumps(value,ensure_ascii=False)
        f.writelines(a+'\n')