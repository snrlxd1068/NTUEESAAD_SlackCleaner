from slack_cleaner2 import SlackCleaner
s = SlackCleaner("Your User Oauth Token", sleep_for=1)

for c in s.ims:
#    if c.name != "": 
        for msg in c.msgs():
            if msg.user == s.myself:
                msg.delete(replies=True,files=True)
            elif msg.has_replies:
                for reply in msg.replies():
                    if reply.user == s.myself:
                        reply.delete()
