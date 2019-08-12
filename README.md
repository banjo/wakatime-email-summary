# Wakatime Email Summary

Wakatime Email Summary is a python script that fetches all your Wakatime Weekly emails from the Gmail API and summarizes the data into a json file. The time is set to seconds.

## Installation

- Install [Python](https://www.python.org/) and [Git](https://git-scm.com/)
- Download repository from Github
```bash
# Clone repository
$ git clone https://github.com/banjoanton/wakatime-summary.git

# Change directory to repository
$ cd "wakatime-summary"

# Install requirements
$ pip install -r requirements.txt
# or pip3 in some cases
$ pip3 install -r requirements.txt
```
- Add [Gmail API credentials](https://developers.google.com/gmail/api/quickstart/python) to directory.

## Usage
Run `app.py` and login to Google. A file named `wakatime.json` will be created with all your data.

## Contributing
Pull requests are welcome. Feel free to add anything.
