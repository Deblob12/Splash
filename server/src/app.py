from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import json

from config import firebase


app = Flask(__name__)
group_count = 0

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """
        1: Login to Venmo
        2: Create an empty group
        3: Add members to your group (name, phone number, their Venmo)
        4: Create a charge
            a. OPTIONAL - Place/event
            b. How much to charge each person
        5: Push charges (resets the charge count)
        6: End trip
    """
    number = request.form['From']
    message_body = request.form['Body']

    msg = Messenger()

    # respone_body = ''

    # if '1' in message_body:
    #     msg.venmo_login(message_body)
    # elif '2' in message_body:
    #     msg.create_group(message_body)
    # elif '3' in message_body:
    #     msg.add_member(message_body)
    # elif '4' in message_body:
    #     msg.create_charge(message_body)
    # elif '5' in message_body:
    #     msg.push_charges(message_body)
    # elif '6' in message_body:
    #     msg.end(message_body)
    # else:
    #     response_body = 'Please specify one of the options!'

    resp = MessagingResponse()
    resp.message(response_body)

    return str(resp)


@app.route('/random', methods=['GET', 'POST'])
def random():
    number = 1234567890
    message_body = '$10 for gas'
    return 'Hello World'


if __name__ == "__main__":
    app.run(debug=True)
