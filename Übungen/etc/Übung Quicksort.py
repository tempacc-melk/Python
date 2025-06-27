import sys
sys.path.append('./')
from Lib import meinmodul as mm, sortierungsmodul as sm
import time as t

liste = mm.randomliste (1, 100_000, 10_000)
start = t.time()
sm.quicksort (liste, 0, len (liste) - 1)
stop = t.time()
print (f"Quicksort (10.000): {stop-start:.3f}s")

liste = mm.randomliste (1, 100_000, 20_000)
start = t.time()
sm.quicksort (liste, 0, len (liste) - 1)
stop = t.time()
print (f"Quicksort (20.000): {stop-start:.3f}s")

liste = mm.randomliste (1, 100_000, 40_000)
start = t.time()
sm.quicksort (liste, 0, len (liste) - 1)
stop = t.time()
print (f"Quicksort (40.000): {stop-start:.3f}s")

liste = mm.randomliste (1, 100_000, 100_000)
start = t.time()
sm.quicksort (liste, 0, len (liste) - 1)
stop = t.time()
print (f"Quicksort (100.000): {stop-start:.3f}s")
