from requests_html import HTMLSession

session = HTMLSession()

url = 'http://gutenberg.org/files/11/11-0.txt'

r = session.get(url)
contents = r.html.text
with open('E:/GitPro/alice.txt','w',encoding = 'utf-8') as f:
    f.write(contents)






