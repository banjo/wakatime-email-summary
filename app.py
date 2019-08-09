from credentials import get_service
from messages import fetch_messages
from labels import get_wakatime_label


def main():
    service = get_service()  # prepare gmail API
    label = get_wakatime_label(service)  # get wakatime label
    # get all messages with wakatime label
    messages = fetch_messages(service, label)
    data = get_wakatime_data(messages)  # get wakatime data as a dictionary


def get_wakatime_data(messages):
    data = {}
    for msg in messages:
        body = str(msg["body"])  # save body to variable

        # save variable to keep track of which part of the body that has useful data
        active_section = None

        #  separate lines to easier handle data
        for line in body.split('\n'):
            line = line.strip()  # remove spaces

            if line == "Projects:":
                active_section = line[:-1]
            elif line == "Languages:":
                active_section = line[:-1]
            elif line == "Editors:":
                active_section = line[:-1]
            elif line == "Operating Systems:":
                active_section = line[:-1]
            elif line == "Categories:":
                active_section = line[:-1]
            elif line == "Machines:":
                active_section = line[:-1]
            elif line == "":
                active_section = None

            if active_section:
                print(line)

                # https://stackoverflow.com/questions/10663720/converting-a-time-string-to-seconds-in-python

    return data


if __name__ == "__main__":
    main()
