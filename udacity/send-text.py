from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACbbd854ddc120b95321c966b7ef847aef" 
AUTH_TOKEN = "bc7d1fd646749542dd300452806f1b69" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
        body="This is a test",
        to="+14159527314",
	from_="+14158010018"
)
