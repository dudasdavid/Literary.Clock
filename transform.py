import codecs
f = codecs.open('data.csv', 'r', 'UTF-8')
f2 = codecs.open('data.js', 'w', 'UTF-8')
for line in f:
    line = line.replace('"', '“')
    split_data = line.split("|")

    new_line = '\t}, {\n\t\t"time": "' + split_data[0] + '",\n\t\t"descriptive": "' + split_data[1] + '",\n\t\t"quote": "' + split_data[2] + '",\n\t\t"source": "' + split_data[3] + '",\n\t\t"author": "' + split_data[4] + '"\n'
    #print(new_line)
    f2.write(new_line)

f.close()
f2.close()