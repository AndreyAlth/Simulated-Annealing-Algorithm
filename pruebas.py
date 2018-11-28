from progress.bar import Bar
import time

bar = Bar('Processing', max=100)

time.sleep(2)
bar.next()
time.sleep(2)
bar.next()
bar.finish()
