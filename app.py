from credentials import get_service
from messages import fetch_messages
from wakatime import get_wakatime_data
import json


def main():
    service = get_service()  # prepare gmail API
    messages = fetch_messages(service)  # get all messages from wakatime weekly
    data = get_wakatime_data(messages)  # get wakatime data as a dictionary

    print("Saving data to 'wakatime.json'...")

    # write to json file
    with open('wakatime.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
