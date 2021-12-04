from twilio.rest import Client 

account_sid = "AC31a5f228f4f1f75242b72aeacacc6749"
auth_token  = "feebc91eaccdcbbea1e0ba4b5edeeae0"
client =Client(account_sid, auth_token)
print ("GOla")

sms = client.sms.messages.create(body="All in the game, yo",
    to="+91MYNUMBER",
    from_="+1MY_TWILIO_NUMBER")
