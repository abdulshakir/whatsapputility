from twilio.rest import Client

def msg_mom_and_dad(event=None, context=None):

    # get your sid and auth token from twilio
    twilio_sid = 'ghjgjjhkhkjkhkhkhkh'
    auth_token = 'jjhklhjgjhhghgljll'

    whatsapp_client = Client(twilio_sid, auth_token)

    # keep adding contacts to this dict to send
    # them the message
    contact_directory = {'shakir':'+919128778989'}

    for key, value in contact_directory.items():
        msg_loved_ones = whatsapp_client.messages.create(
                body = 'Assalam Alaikum ,wake up{} !'.format(key),
                from_= 'whatsapp:+14155238886',
                to='whatsapp:' + value,

            )

        print(msg_loved_ones.sid)
