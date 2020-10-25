import main

fin = open("test.txt", 'r') # входные данные с тест кейсами
fout = open("test_resalt.txt", 'w') # выходной файл с результами всех кейс текстов
count = 0
for line in fin: # парсинг
    count += 1
    line_param = line.split(' ')
    if line[-1] != '/n':
        arg = 1
    else:
        arg = 0
    if line[-1] == 'й' or line[-1] == 'к' or line[-1] == 'а':
        arg = 0


    if (main.main(' '.join(line_param[:-1])) == str(line_param[-1])[0:len(line_param[-1])-(1*arg)]):
        linetoout = str(count) + " succes; " + "\n"
    else:
        linetoout = str(count) + " error; " + "\n"
    fout.write(linetoout)

fout.close()
