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
        body = msg["body"]

    return data
    

if __name__ == "__main__":
    main()
