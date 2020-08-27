import json

username = input('What is your name? ')

filename = 'E:/GitPro/username.json'

with open(filename , 'w' ) as f:
    json.dump(username,f)
    print('We\'ll remember you when you come back, ' + username + "!")