fp=open('message.txt','w')
fp.write('Python is fun!')
print("new folder created")

fp=open('movies.txt','w')
fp.writelines('1.queen of Tears' \
'2.hi nanna' \
'3.court' \
'4.hit-3' \
'5.kingdom')
print("a new file with muiltiple lines")