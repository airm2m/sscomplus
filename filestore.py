__author__ = 'Administrator'

def Save(path,data):
    print("save")
    file = open(path,"wt")
    file.write(data)
    file.close( )
def load(path):
    print("load")
    read_data = ""
    file = open(path,"rt")
    print("file=",file,type(file))
    try:
        read_data = file.read()
    finally:
        file.close()
    return read_data

def loadConf(path):
    print("load configuration")
    dataConf = []
    file = open(path)
    while 1:
        line = file.readline()
        if not line:
            break
        dataConf.append(line[5:-1])
    file.close()
    return dataConf

def writeConf(path,arg,value):
    print("write configuration")
    content = ""
    file = open(path)
    while 1:
        line = file.readline()
        if not line:
            break
        if line.find(arg) == 0:
            print(line)
            line = arg + "=" + value +"\n"
        content = content + line
    file.close()
    file = open(path,"wt")
    print(content)
    file.writelines(content)
    file.close()

