from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="",
                     from_='+19285698470',
                     to='+18106890251‬'
                 )

print(message.sid)