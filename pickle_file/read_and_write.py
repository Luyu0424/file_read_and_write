import pandas as pd
import pickle
#read
content=pd.read_pickle('_read_file.pickle')

write_content=content[:10]
print(len(write_content))
#write
with open('./_write_file.pickle','wb') as f:
    string=pickle.dumps(write_content)
    f.write(string)