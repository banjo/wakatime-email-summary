

def get_wakatime_label(service):
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        return None
    else:
        for label in labels:
            if "wakatime" in label['name'].lower():
                return label
