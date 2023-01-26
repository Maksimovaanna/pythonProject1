import os
import json
pylint = os.popen('pylint ./views.py').read()
if pylint:
     print('Ошибки качества кода')

os.system('bandit -iii -lll -q -r ./views.py -o bandit.json -f json ')
with open('bandit.json', 'r') as f:
    b = json.load(f)
if b['results']:
    print('В коде присутсвуют ошибки')
