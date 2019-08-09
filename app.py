from credentials import get_service
from messages import fetch_messages


def main():
    service = get_service()  # prepare gmail API
    fetch_messages(service)  # get all messages


if __name__ == "__main__":
    main()
