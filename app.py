from credentials import get_service
from messages import fetch_messages
from pprint import pprint


def main():
    service = get_service()  # prepare gmail API
    messages = fetch_messages(service)  # get all messages from wakatime weekly
    data = get_wakatime_data(messages)  # get wakatime data as a dictionary


def get_wakatime_data(messages):
    data = []

    for msg in messages:
        body = str(msg["body"])  # save body to variable
        message_data = {}  # init dict to store message data

        # save variable to keep track of which part of the body that has useful data
        active_section = None
        sections = ["Projects:", "Languages:", "Editors:",
                    "Operating Systems:", "Categories:", "Machines:"]

        # add a dictionary for each section
        for section in sections:
            message_data[section[:-1]] = {}

        #  separate lines to easier handle data
        for line in body.split('\n'):
            line = line.strip()  # remove spaces

            # search for sections with useful data

            # mark line of information with section and exclude the actual section name
            if line in sections:
                active_section = line[:-1]
                continue
            elif line == "":
                active_section = None

            # handle information on useful sections
            if active_section:

                # split name and time
                parts = line.split(" : ")
                name = parts[0]
                time = parts[1]

                # ! Handle time with (time = time.strptime("01:05:22", "%H:%M:%S")) ?

                message_data[active_section].update({name: time})

    pprint(message_data)  # debug print

    # https://stackoverflow.com/questions/10663720/converting-a-time-string-to-seconds-in-python
    return data


if __name__ == "__main__":
    main()
