
import sys
import os
import argparse
import tempfile
import json

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if not os.path.exists(storage_path):
    f = open(storage_path, 'w')
    f.close()

# читаем все данные
f = open(storage_path, 'r')
s = f.read()
f.close()
list_storage = []
if len(s) > 0:
    list_storage = list(json.loads(s))
 
if args.val is None:
    # поиск
    out_str = ""
    for cur_pair in list_storage:
        if cur_pair[0] == args.key:
            if len(out_str) == 0:
                out_str = str(cur_pair[1])
            else:
                out_str = out_str + ", " + cur_pair[1]
    print(out_str)
else:
    # запись нового
    list_storage.append([args.key,args.val])
    with open(storage_path, 'w') as f:
        s = json.dumps(list_storage)
        f.write(s)
        