from utils.printers import printer_basic

a = printer_basic()
print(a)

import json
with open('sample.json','r') as config_file:
    config = json.load(config_file)
print(config['job_name'])