import threading
import time
import tracemalloc

def mwpoller():
  while 1:
    time.sleep(0.2)
    mwpoll()

def mwpoll():
    snapshot = tracemalloc.take_snapshot()

    for stat in snapshot.statistics("lineno"):
        if str(stat.traceback).__contains__("trace.py"):
            print(stat)

tracemalloc.start()
threading.Thread(target=mwpoller).start()

l1 = [i for i in range(10000)]
l2 = [i*i for i in range(10000)]
l3 = [i*i*i for i in range(10000)]
#
# for trace in snapshot.traces:
#     print(trace)

# tracemalloc.stop()
exit()