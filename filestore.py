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

def loadConfig(path):
    print("load configuration")
    dataConfig = {}
    file = open(path)
    try:
        while 1:
            line = file.readline()
            if not line:
                break
            if line[0:4] == "baud":
                dataConfig.update({"baud":line[5:-1]})
            elif line[0:4] == "data":
                dataConfig.update({"data":line[5:-1]})
            elif line[0:4] == "stop":
                dataConfig.update({"stop":line[5:-1]})
            elif line[0:4] == "str1":
                dataConfig.update({"str1":line[5:-1]})
            elif line[0:4] == "str2":
                dataConfig.update({"str2":line[5:-1]})
            elif line[0:4] == "str3":
                dataConfig.update({"str3":line[5:-1]})
            elif line[0:4] == "str4":
                dataConfig.update({"str4":line[5:-1]})
            elif line[0:4] == "str5":
                dataConfig.update({"str5":line[5:-1]})
            elif line[0:4] == "str6":
                dataConfig.update({"str6":line[5:-1]})
    finally:
        file.close()
    return dataConfig

def writeConfig(path,arg,value):
    print("write configuration")
    content = ""
    file = open(path)
    try:
        while 1:
            line = file.readline()
            if not line:
                break
            if line.find(arg) == 0:
                print(line)
                line = arg + "=" + value +"\n"
            content = content + line
    finally:
        file.close()
    file = open(path,"wt")
    print(content)
    file.writelines(content)
    file.close()

