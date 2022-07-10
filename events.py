def get_event(event):
    events = {
        "start": "[*] Record start!",
        "stop": "[*] Record successful finished!",
        "parsing": "[*] Parsing config...",
        "success": "[*] Succesful!",
        "cfg_error":"[*] Invalid values in config.txt",
        "empty_list":"[*] Please, try again!",
        "done":"[*] Program has completed its work"
    }
    return events[event]