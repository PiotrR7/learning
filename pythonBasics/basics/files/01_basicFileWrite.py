fh = open('test.txt', 'w')
fh.write("Hello World")
fh.close()

fh2 = open('test.txt', 'a')
fh2.write("\ncontent")
fh2.close()