# coding=utf-8
import threading
class LibEvent:
    def __init__(self):
        self.m_Event = threading.Event()
        self.m_Lock = threading.Lock()
        self.m_nCnt = 0

    def set(self):
        """
        self.m_Event.set()
        self.m_Event.clear() # 일반적으로 여기서 clear 하는 듯 한데
        """
        # plog ("set called")
        self.m_Lock.acquire()
        nCnt = self.m_nCnt
        self.m_nCnt += 1
        self.m_Lock.release()

        if (nCnt == 0):
            # wait 가 먼저 호출되지 않으면 여기서 잼이 걸린다.
            self.m_Event.set()
            self.m_Event.clear()
        # """
        # plog ("set end", nCnt)

    def wait(self, nSec):
        """
        self.m_Event.wait(nSec)
        #self.m_Event.clear() # 일반적으로 여기서 clear 를 호출하지 않는다
        """
        # plog ("wait called", nSec)
        self.m_Lock.acquire()
        nCnt = self.m_nCnt
        if (nCnt):
            # 이미 set 이 일어난 경우는 바로 return 한다
            self.m_nCnt -= 1
            self.m_Lock.release()
            # plog ("wait end1", nCnt)
            return
        self.m_Lock.release()

        # set 이 없어서 wait 하는데, 이 사이에 set 이 ( +1, set, clear ) 를 하고 지나가면 잼이 걸린다.
        self.m_Event.wait(nSec)

        self.m_Lock.acquire()
        if (self.m_nCnt):
            # 마이너스가 안되게 정리하고 나간다
            self.m_nCnt -= 1
        self.m_Lock.release()
        # """
        # plog ("wait end2", nCnt)

    def clear(self):
        """
        self.m_Event.clear()

        """
        self.m_Lock.acquire()
        self.m_nCnt = 0
        self.m_Lock.release()
        self.m_Event.clear()

        # """










