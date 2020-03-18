import threading
import queue


class RWSet:
    m_key = ""
    m_value = ""
    def __init__(self, key,value):
        self.m_key = key
        self.m_value = value


class Endorser(threading.Thread):
    m_msp = ""
    m_bEnd = False
    m_dataList = queue.Queue(100000)
    m_rwsetList = queue.Queue(100000)

    def __init__(self, msp):
        super(Endorser, self).__init__()
        self.m_msp = msp

    def terminateThread(self):
        self.m_bEnd = True

    def addMsg(self, szData):
        try:
            self.m_dataList.put(szData)
            return self.m_rwsetList.get()
        except:
            print (" exception!!.", szData)


    def getMsg(self):
        if (self.m_dataList.empty()):
            return None

        msg = self.m_dataList.get()
        return msg

    def run(self):

        while (not self.m_bEnd):
                msg = self.getMsg()
                if (msg == None):
                    continue

                self.m_rwsetList.put("rwset")




class Fabric:

    endorser = Endorser("org1")

    def __init__(self):
        pass

    def start(self):
        self.endorser.start()

    def add_trans(self,key,value):
        rwset = RWSet(key,value)
        self.endorser.addMsg(rwset)



