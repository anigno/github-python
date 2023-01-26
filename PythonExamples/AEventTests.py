import time, datetime
from AEvent import AEvent, AEventArgsBase



class MyTimerEventArgs(AEventArgsBase):
    def __init__(self, count):
        self.Time = datetime.datetime.now()
        self.Count = count



class MyTimer:
    OnTimerTick = AEvent()

    def TimerFunction(self, counts: int):
        for a in range(0, counts):
            time.sleep(0.5)
            self.OnTimerTick.Raise(MyTimerEventArgs(a))

    def TimerFunctionAsync(self, counts: int):
        for a in range(0, counts):
            time.sleep(0.5)
            self.OnTimerTick.RaiseAsync(MyTimerEventArgs(a))



def handler_A(myTimerEventArgs):
    print('handler A', myTimerEventArgs.Time,myTimerEventArgs.Count)
    time.sleep(0.6)

def handler_B(myTimerEventArgs):
    print('handler B', myTimerEventArgs.Time,myTimerEventArgs.Count)
    time.sleep(0.8)



m = MyTimer()

m.OnTimerTick += handler_A
m.OnTimerTick += handler_B

m.TimerFunction(5)
print('Async raise')
m.TimerFunctionAsync(5)
