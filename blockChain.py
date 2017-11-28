import hashlib
import json
import os
from time import time

BLOCKCHAIN_DIR = os.curdir + '/blocks/'

def check_blocks_integrity():
    result = []
    for i in range(2, int(get_next_block())):
        tmp ={'block' : '', 'result' : ''}
        cur_hash = json.load(open(BLOCKCHAIN_DIR + str(i) + '.json'))['hash']
        prev_hash = hashlib.sha256(open(BLOCKCHAIN_DIR + str(i-1) + '.json', 'rb').read()).hexdigest()
        if cur_hash != prev_hash:
            tmp['block'] = str(i-1)
            tmp['result'] = 'error'
        else:
            tmp['block'] = str(i-1)
            tmp['result'] = 'ok'
        result.append(tmp)

    return result


def check_block(index):
    index = str(int(index) + 1)
    result = []
    index_ = str(int(index) - 1)
    tmp ={'block' : '', 'result' : ''}
    cur_hash = json.load(open(BLOCKCHAIN_DIR + index + '.json'))['hash']
    prev_hash = hashlib.sha256(open(BLOCKCHAIN_DIR + index_ + '.json', 'rb').read()).hexdigest()
    if cur_hash != prev_hash:
        tmp['block'] = index_
        tmp['result'] = 'error'
    else:
        tmp['block'] = index_
        tmp['result'] = 'ok'
    result.append(tmp)
    return result

def get_hash(file_name):
    with open(BLOCKCHAIN_DIR + file_name + '.json', 'rb') as file:
        return hashlib.sha256(file.read()).hexdigest()


def get_next_block():
    files = os.listdir(BLOCKCHAIN_DIR)
    index_list = [int(file.split('.')[0]) for file in files]
    cur_index = sorted(index_list)[-1]
    next_index = cur_index + 1
    return str(next_index)


def get_work_proof(file_name, difficulty=1):
    with open(BLOCKCHAIN_DIR + file_name + '.json', 'rb') as file:
        if str(hashlib.sha256(file.read()).hexdigest())[:difficulty] == '0'*difficulty:
            return true



def write_block(text):
    cur_index = get_next_block()
    prev_index = str(int(cur_index) - 1)
    prev_block_hash = get_hash(prev_index)
    cur_block_hash = get_hash(cur_index)
    data = {'text' : text,
            'prev_hash' : prev_block_hash,
            'cur_hash' : cur_block_hash,
            'timestamp' : time(),
            'proof' : ' ',
            'index' : cur_index
            }  

    with open(BLOCKCHAIN_DIR + cur_index + '.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    for i in range(2,10):
        write_block(str(i))
    print(check_blocks_integrity())


