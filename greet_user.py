import json

filename = 'E:/GitPro/username.json'

with open (filename) as f:
    username = json.load(f)
    print('Welcome back, ' + username + '!')