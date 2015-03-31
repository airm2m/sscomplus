__author__ = 'Administrator'

import struct
import common
import trace
#host协议编解码处理

ID = 0xA2
RESET = b"\x00\x55\x00\x00\x00"      #重启

#id 与 data中的每一个为进行异或
def calccrc(id,data):
    val = id                        #bit.bxor(0,id)
    for i in data:
        val = val ^ i

    return val
# end calccrc

def urat_encode(data):
    l = len(data)
    #print("l=",l,data,type(data),data[-2],data[-1])
    outd = struct.pack(">BHB%dsB"%l,0xAD,l+1,ID,data,calccrc(ID,data))
    #print("urat_encode type(outd)=",type(outd))

    #转义
    #5c -> 5c a3 bytearray(send_data,'utf-8')
    outd = outd.replace(b"\x5c", b"\x5c\xa3")
    # 11 -> 5c ee
    outd = outd.replace(b"\x11",b"\x5c\xee")
    # 13 -> 5c ec
    outd = outd.replace(b"\x13",b"\x5c\xec")

    return outd
#end urat_encode

olddata = {
    "e_char" : False,
    "l_data" : b"",
    "e_data" : b"",
    "r_len" : -1,
}

def urat_decode(data):
    if data == None or data == b"" :
        return
    #end

    if olddata["e_char"] == True:
        data = b"\x5c" + data
    #end

    #-- 判断是否存在分离的转义字符
    if data[-1] == 0x5c:
        olddata["e_char"] = True
        data = data[0:-1]
    else:
        olddata["e_char"] = False
    #end

    # 对数据进行反转义
    #  5c ee -> 11
    data = data.replace(b"\x5c\xee",b"\x11")
    # 5c ec -> 13
    data = data.replace(b"\x5c\xec",b"\x13")
    #-- 5c a3 -> 5c
    data = data.replace(b"\x5c\xa3",b"\x5c")

    #data = common.bytestousc2(data)
    data = olddata["e_data"] + data
    olddata["e_data"] = b""
    #print("olddata.l_data=",olddata.l_data)
    #pos
    while data or data == b"":
        #print("while data=",data)
        pos = data.find(b"\xAD")
        if pos == -1 :
            #print("oooooooooooooo")
            olddata["l_data"] = olddata["l_data"] + data
            olddata["e_data"] = data
            data = None
            return
        #end

        if pos == 0 and olddata["l_data"] == b"":
            pos = data.find(b"\xAD",1)
            if pos == -1 :
                #olddata["l_data"] = data
                olddata["e_data"] = data
                data = None
                #print("1111")
                return
            #end
            #print("2222")
            olddata["l_data"] = data[:pos]
            data = data[pos:]

        elif pos > 0 :
            #print("33333")
            olddata["l_data"] = olddata["l_data"] + data[:pos]
            data = data[pos:]

        elif pos == 0 and olddata["l_data"] != b"" :			#专门针对ad 00 06 ff ad .....(16进制表示)
            #print("444")
            pos = data.find(b"\xAD",1)
            if pos == -1:
                #olddata.l_data = olddata.l_data .. data
                olddata["e_data"] = olddata["l_data"] + data
                olddata["l_data"] = b""
                data = None
                #print("444111")
                return
            #end
            #print("4442222")
            olddata["l_data"] = olddata["l_data"] + data[:pos]
            data = data[pos:]
        #end

        #--解析数据头
        valid_data = check_pack(olddata["l_data"])
        if valid_data == "lack":
            print("valid_data == lack")
        elif valid_data == "invalid" :
            olddata["l_data"] = b""
        else:
            #local p,l,d = string.unpack(valid_data,">bz")
            l = len(valid_data)
            d = valid_data
            #print("l,d=",l,d,string.len(d))

            olddata["l_data"] = b""
            valid_data = b""
            return d
        #end
    #end
#end


def check_pack(data):
    #print("check_pack data=",data)
    if data == b"" or len(data) <= 4 :
        #--print("adadadadadadadadadada1")
        return "lack"
    #end
    #--AD0007A2  0D0A4F4B0D 0AA6
    head = data[0:4]

    #print("head =",len(head))
    p_head = struct.unpack(">BHB",head)
    start = p_head[0]
    size = p_head[1]
    id = p_head[2]

    #print("sss=",start,size,id)
    valid_data = data[4:]
    valid_len = len(valid_data)
    if id == 0x80 :
        valid_data = valid_data[2:-1]

    if id == 0xff :
        trace.SaveTrace(common.GetNowTime() + " id:" , hex(id), " valid_data: ",valid_data[:-1], "hexs:", common.bytestohexs(data))
        #trace.SaveTrace(common.GetNowTime() + " id:" , hex(id), " hexs:",common.bytestohexs(data))

    #ad 00 06 ff  00 55 00 00  00 aa
    if start == 0xad and (id == ID or id == 0xff) :
        if size <= valid_len :
            '''
            if id == ID :
                #print("size =",size,"len=",len,valid_data,common.bytestohexs(valid_data))
                pass
            #end
            '''
            src = valid_data[size -1]
            valid_data = valid_data[0:size -1]     #	--为了防止读出多余没用的数据AD0007A20D0A4F4B0D0AA6（13111311）
            '''
            if id == ID :
                pass
                #print("bytestohexs(valid_data)=",common.bytestohexs(valid_data))
            #end
            '''

            #print("src,calccrc(id,valid_data)=",src,calccrc(id,valid_data),"valid_data=",valid_data)
            if src == calccrc(id,valid_data) :
                if id == 0xff :
                    if valid_data == RESET :
                        #--返回一个，或通过一个函数调用
                        return b"\x10restart OK"
                    #end
                    return "invalid"
                #end
                return valid_data
            #end
        elif size > valid_len :
            print("lcak")
            return "lack"
        #end
    #end
    return "invalid"
#end

#msg_ori = b'\x45\xD4\x98\xdd\x34'
#msg = b'\xAD\x00\x07\xA2\x0D\x0A\x4F\x4B\x0D\x0A\xA6\xAD'

#data_i = urat_encode(msg_ori)
#data_o = urat_decode(msg)
#data_c = check_pack(msg)
#print("data=",data_c)
#print("data=",data_i[4])
