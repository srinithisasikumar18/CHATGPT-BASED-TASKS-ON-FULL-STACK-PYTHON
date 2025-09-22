try:
    fp=open('abc.txt','r')
    data=fp.read()
    print(data)

except FileNotFoundError :
    
    print("File not found")

finally:
    print("File handling complete")
