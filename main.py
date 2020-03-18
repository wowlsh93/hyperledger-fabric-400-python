
import fabric
import UtilTime

def main() :
    print ("start -1")
    tTime = UtilTime.getCurrentClock()

    fb = fabric.Fabric()
    fb.start()

    for idx in range(1000000):
        fb.add_trans(str(idx), str(idx))

    tTime2 = UtilTime.getCurrentClock()
    print ("time : ", tTime2 - tTime)


    print("start -2")

main()