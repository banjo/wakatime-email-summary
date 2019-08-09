import base64
import email


def fetch_messages(service):
    # get all messages
    response = service.users().messages().list(userId='me').execute()

    # add them to a list
    messages = []
    if 'messages' in response:
        messages.extend(response["messages"])

    # get each message and add to list
    final_messages = []
    for message in messages:
        msg_id = message["id"]

        msg = service.users().messages().get(
            userId='me', id=msg_id).execute()  # fetch message using API


    # https://github.com/abhishekchhibber/Gmail-Api-through-Python/blob/master/gmail_read.py
