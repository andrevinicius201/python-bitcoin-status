import os
from twilio.rest import Client

#REMOVE CREDENTIAL AND ANY PRIVATE DATA
os.environ['TWILIO_ACCOUNT_SID'] = ''
os.environ['TWILIO_AUTH_TOKEN'] = ''
os.environ['TWILIO_PHONE_NUMBER'] = ''
os.environ['CELL_PHONE_NUMBER'] = ''

print(os.getenv('TWILIO_ACCOUNT_SID'))
print(os.getenv('TWILIO_AUTH_TOKEN'))
print(os.getenv('TWILIO_PHONE_NUMBER'))
print(os.getenv('CELL_PHONE_NUMBER'))

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

def send_message(bitcoin_cotation):
    client.messages.create(from_=os.environ.get('TWILIO_PHONE_NUMBER'), to=os.environ.get('CELL_PHONE_NUMBER'), body='Andre, a cotacao atual do bitcoin eh de R$' + str(bitcoin_cotation))
    



