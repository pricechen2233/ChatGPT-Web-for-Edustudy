import LRU_cache 
import pickle
import json

with open('./data/all_user_dict_v3.pkl', 'rb') as f:
    data = pickle.load(f)
f.close()
    
for key in list(data.keys()):
    if key == 'user888,123456ccnu' or key == 'user999,123456ccnu':
        continue
    with open('./data/haveread.txt', 'a') as f:
        f.write(key+'\n')
        f.write(json.dumps(data.get(key), ensure_ascii=False))
        f.write('\n')
    f.close()