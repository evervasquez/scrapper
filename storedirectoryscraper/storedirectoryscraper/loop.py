
import commands
import time

for ruc in range(20500100000, 20500100010):
    time.sleep(60)
    command = 'scrapy crawl rapipago -a ruc=%d' % ruc
    commands.getoutput(command)
