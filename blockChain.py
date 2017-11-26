import hashlib
import json
import os

BLOCKCHAIN_DIR = os.curdir + '/blocks/'

def check_blocks_integrity():
    result = []
    for i in range(2, int(get_next_block())):
        tmp ={'block' : '', 'result' : ''}
        cur_hash = json.load(open(BLOCKCHAIN_DIR + str(i) + '.json'))['hash']
        prev_hash = hashlib.md5(open(BLOCKCHAIN_DIR + str(i-1) + '.json', 'rb').read()).hexdigest()
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
    prev_hash = hashlib.md5(open(BLOCKCHAIN_DIR + index_ + '.json', 'rb').read()).hexdigest()
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
        return hashlib.md5(file.read()).hexdigest()


def get_next_block():
    files = os.listdir(BLOCKCHAIN_DIR)
    index_list = [int(file.split('.')[0]) for file in files]
    cur_index = sorted(index_list)[-1]
    next_index = cur_index + 1
    return str(next_index)


def write_block(text):
    cur_index = int(get_next_block()) - 1
    prev_block_hash = get_hash(str(cur_index))
    data = {'text' : text,
            'hash' : prev_block_hash}  

    with open(BLOCKCHAIN_DIR +  get_next_block() + '.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    print(check_blocks_integrity())
    print(check_block('2'))

if __name__ == '__main__':
    main()