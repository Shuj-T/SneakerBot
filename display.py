class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


divider = "\n--------------------------------\n"
title = f"""
██████     ██████     ██ ████████ ██     ██ 
██   ██    ██   ██    ██    ██    ██     ██ 
██████     ██████     ██    ██    ██  █  ██ 
██   ██    ██   ██    ██    ██    ██ ███ ██ 
██████  ██ ██████  ██ ██ ██ ██ ██  ███ ███       
Before we being make sure you have already
entered {bcolors.WARNING}payment info{bcolors.ENDC}, {bcolors.WARNING}account info{bcolors.ENDC} and {bcolors.WARNING}
proxies{bcolors.ENDC}
============================================"""