all_strs=[]
#read_txt
with open('_read_file.txt','r',encoding='utf-8') as f:
    for line in f:
        all_strs.append(line)

write_strs=all_strs[:10]

#write_txt
with open('./_write_file.txt', 'w', encoding='utf-8') as f:
    for line in write_strs:
        f.write(line)