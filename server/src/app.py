from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import json


from config import firebase

app = Flask(__name__)

db = firebase.database()

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    number = request.form['From']
    message_body = request.form['Body']

    resp = MessagingResponse()

    # Add a message
    resp.message("Yes he is!")

    db.child('random2').push('This also works!')

    return str(resp)

@app.route('/random', methods=['GET', 'POST'])
def random():
    db.child('test').push('This works!')
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)
