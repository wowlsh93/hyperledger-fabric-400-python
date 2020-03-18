# coding=utf-8
import threading
import LibEvent


class JobManager:
    def __init__(self):
        self.m_EventJob = LibEvent.LibEvent()  # job add/get 동기화
        self.m_listJob = []
        self.m_listUrgentJob = []
        self.m_listJobLock = threading.Lock()
        self.m_listUrJobLock = threading.Lock()

    # ----------------------------------------
    def setForJob(self):
        self.m_EventJob.set()
        # self.m_EventJob.clear()

    def waitForJob(self, nSec):
        self.m_EventJob.wait(nSec)
        return self.getAllJobCount()

    def getAllJobCount(self):
        return self.getUgJobCount(), self.getJobCount()

    # ----------------------------------------
    # urgent job
    # terminal > server > manager
    def getUgJobCount(self):
        return len(self.m_listUrgentJob)

    def getUgJob(self):
        if (self.getUgJobCount() == 0):
            return None

        self.m_listUrJobLock.acquire()
        retJob = self.m_listUrgentJob.pop(0)
        self.m_listUrJobLock.release()

        return retJob

    def addUgJob(self, oJob):
        self.m_listUrJobLock.acquire()
        self.m_listUrgentJob.append(oJob)
        self.m_listUrJobLock.release()
        self.setForJob()

    # ----------------------------------------
    # normal job
    def getJobCount(self):
        return len(self.m_listJob)

    def getJob(self):
        if (self.getJobCount() == 0):
            return None

        self.m_listJobLock.acquire()
        retJob = self.m_listJob.pop(0)
        self.m_listJobLock.release()

        return retJob

    def addJob(self, oJob):
        self.m_listJobLock.acquire()
        self.m_listJob.append(oJob)
        self.m_listJobLock.release()
        self.setForJob()



