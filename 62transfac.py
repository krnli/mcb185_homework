import sys
import gzip
import re
import json

transfac = sys.argv[1]

with gzip.open(transfac, 'rt') as fp:
    record = []
    id_list = list()
    for line in fp:
        linewords = line.split()
        if linewords[0] == 'ID': 
            id = linewords[1]
            if id not in record: 
                id_rec = {}
                id_rec['id'] = id
                record.append(id_rec)
                id_list.append(id)
        if re.search('[0123456789]', linewords[0]): 
            if id not in id_list: pwm_id = []
            pwm = {}
            pwm['A'] = linewords[1]
            pwm['C'] = linewords[2]
            pwm['G'] = linewords[3]
            pwm['T'] = linewords[4]
            if id not in id_list: 
                pwm_id.append(pwm)
                id_rec['pwm'] = pwm_id
            else: 
                idx = id_list.index(id)
                record[idx]['pwn'].append(pwm)

            
    fp.close()

print(json.dumps(record[:4], indent=4)) 
      
d = dict()

