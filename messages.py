import base64
import dateutil.parser as parser
from datetime import datetime
import datetime
from bs4 import BeautifulSoup
import time


def fetch_messages(service):
    print("Fetching mail IDs...")
    # get all messages
    response = service.users().messages().list(
        userId='me', q="subject:(WakaTime Weekly)", maxResults=1000).execute()

    # add them to a list
    messages = []
    if 'messages' in response:
        messages.extend(response["messages"])

    print("Fetching mails...")
    # get each message and add to list
    final_messages = []
    for i, message in enumerate(messages):
        print(f'{i + 1}/{len(messages)}')

        msg_id = message["id"]  # get id of message
        msg = service.users().messages().get(
            userId='me', id=msg_id).execute()  # fetch message using API

        msg_json = decode_message(msg)
        final_messages.append(msg_json)

    return final_messages


def decode_message(msg):
    temp_dict = {}

    payld = msg['payload']  # get payload of the message
    headr = payld['headers']  # get header of the payload

    for one in headr:  # getting the Subject
        if one['name'] == 'Subject':
            msg_subject = one['value']
            temp_dict['Subject'] = msg_subject
        else:
            pass

    for two in headr:  # getting the date
        if two['name'] == 'Date':
            msg_date = two['value']
            date_parse = (parser.parse(msg_date))
            m_date = (date_parse.date())
            temp_dict['date'] = str(m_date)
        else:
            pass

    for three in headr:  # getting the Sender
        if three['name'] == 'From':
            msg_from = three['value']
            temp_dict['sender'] = msg_from
        else:
            pass

    temp_dict['snippet'] = msg['snippet']  # fetching message snippet

    try:

        # Fetching message body
        mssg_parts = payld['parts']  # fetching the message parts
        part_one = mssg_parts[0]  # fetching first element of the part
        part_body = part_one['body']  # fetching body of the message
        part_data = part_body['data']  # fetching data from the body
        # decoding from Base64 to UTF-8
        clean_one = part_data.replace("-", "+")
        # decoding from Base64 to UTF-8
        clean_one = clean_one.replace("_", "/")
        # decoding from Base64 to UTF-8
        clean_two = base64.b64decode(bytes(clean_one, 'UTF-8'))
        soup = BeautifulSoup(clean_two, "lxml")
        mssg_body = soup.body()
        # mssg_body is a readible form of message body
        # depending on the end user's requirements, it can be further cleaned
        # using regex, beautiful soup, or any other method
        temp_dict['body'] = mssg_body

    except:
        temp_dict['body'] = None
        pass
    return temp_dict
