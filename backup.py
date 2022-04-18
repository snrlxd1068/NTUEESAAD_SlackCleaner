from slack_cleaner2 import SlackCleaner
from datetime import datetime
s = SlackCleaner("Your User OAuth Token", sleep_for=1)
print('start')
for c in s.ims:
    if not c.user.is_bot:
        msgs = list(c.msgs())
        msgs.reverse()
        if len(msgs) != 0:
            log = open('./%s.txt'%(str(c.user.real_name)),'w',encoding='UTF-8') 
            for msg in msgs:
                if msg.text == '': continue
                if msg.has_replies:
                    log.write('--------\n')
                log.write(str(msg.user.real_name)+':  '+str(msg.text)+'\t@'+datetime.fromtimestamp(msg.ts).strftime("%Y/%m/%d, %H:%M:%S")+'\n')
                for reply in msg.replies():
                    log.write('(Re)'+str(reply.user.real_name)+':  '+str(reply.text)+'\t@'+datetime.fromtimestamp(reply.ts).strftime("%Y/%m/%d, %H:%M:%S")+'\n')
                if msg.has_replies:
                    log.write('--------\n')
                log.write('\n')
