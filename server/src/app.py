from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import json
import maps
from addressDB import storeMapping, getMapping
from config import firebase
import re
import datetime
from werkzeug.exceptions import abort
from flask.json import jsonify

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

def is_request_valid(request):
    is_token_valid = request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']
    return is_token_valid



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


@app.route('/travel-time', methods=['POST'])
def travel_time():
    print(request)
    if not is_request_valid(request):
        abort(400)
    msg = request.form['text']
    destinations = msg.split(';')
    for i in range(len(destinations)):
        destinations[i] = destinations[i].strip().lower()
    if len(destinations) != 2:
        return jsonify(
            repsonse_type='in_channel',
            text='Please enter starting address and end address.'
        )
    address1 = getMapping(request.form['user_id'], destinations[0])
    address2 = getMapping(request.form['user_id'], destinations[1])
    if type(address1) is str:
        destinations[0] = address1
    if type(address2) is str:
        destinations[1] = address2
    
    try:
        t = maps.get_directions_duration(destinations[0].strip(), destinations[1].strip())
    except:
        return jsonify(
            response_type='in_channel',
            text='Invalid Address, Please re-enter.'
        )

    return jsonify(
        response_type='in_channel',
        text= t
    )

@app.route('/random', methods=['GET', 'POST'])
def random():
    number = 1234567890
    message_body = '$10 for gas'
    return 'Hello World'


if __name__ == "__main__":
    app.run(debug=True)
