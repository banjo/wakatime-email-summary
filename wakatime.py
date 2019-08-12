def get_wakatime_data(messages):

    # dict with total values
    total = {}

    # name all sections
    sections = ["Projects:", "Languages:", "Editors:",
                "Operating Systems:", "Categories:", "Machines:"]

    # add a dict for each in total file
    for section in sections:
        total[section[:-1].lower()] = {}

    for msg in messages:
        body = str(msg["body"])  # save body to variable

        # save variable to keep track of which part of the body that has useful data
        active_section = None

        #  separate lines to easier handle data
        for line in body.split('\n'):
            line = line.strip()  # remove spaces

            # mark line of information with section and exclude the actual section name
            if line in sections:
                active_section = line[:-1].lower()
                continue
            elif line == "":
                active_section = None

            # handle information if useful sections
            if active_section:

                # split name and time
                parts = line.split(" : ")
                name = parts[0].lower()
                time = parts[1]

                seconds = get_seconds(time)

                # add total stats for all weeks to "total"
                add_to_total(total, active_section, name, seconds)

    return total


def get_seconds(time):
    time_data = {"hr": 0,
                 "min": 0,
                 "sec": 0}

    # get time in seconds
    if "hr" in time or "hrs" in time:  # get hours
        time_data["hr"] = int(time.split()[0])

    if "min" in time or "mins" in time:  # get minutes

        # if hours are included
        if "hr" in time or "hrs" in time:
            time_data["min"] = int(time.split()[2])
        else:
            time_data["min"] = int(time.split()[0])

    if "secs" in time:  # get seconds
        time_data["sec"] = int(time.split()[0])

    # convert time to seconds
    seconds = (time_data["hr"] * 60 * 60) + \
        (time_data["min"] * 60) + time_data["sec"]
    return seconds


def add_to_total(total, active_section, name, seconds):
    try:
        # if it already exists, update it
        current_sec = total[active_section][name]
        total[active_section][name] = current_sec + seconds
    except:
        # if content on "active section", update it. Else, add it.
        if total[active_section]:
            total[active_section].update({name: seconds})
        else:
            total[active_section] = {name: seconds}
