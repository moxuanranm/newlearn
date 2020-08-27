filename = 'E:/GitPro/alice.txt'

try:
    with open(filename,encoding = 'UTF-8') as f:
        contents = f.read()
except FileNotFoundError:
    msg = 'Sorry'
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print('The file ' + filename + ' has about ' + str(num_words) + ' words.')

