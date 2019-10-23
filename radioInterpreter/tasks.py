""" Android Radio log Interpreter
Author: Lucas de Lima Barros
Team: Protocol TG

The idea of this project is to provide an interface capable of parsing log files in order to show the better matches for
analyze according with the problem. Some steps for this implementation:
1. Read logfile and split in lines
2. Identify radio buffer
3. Match Problem with Key Words ( For example, Emergency Numbers: [EmergencyTracker])
4. Show only the lines according with the problem
Once this is done, we are going to create an end point that can be used by PLM server, to download logs, parse
description and provide a comment automatically.
"""


def read_log(log_file_from_user):
    try:
        if 'logcat' in log_file_from_user:
            with open(log_file_from_user, 'r') as log_obj:
                log_str = log_obj.read()
            return log_str
        else:
            print("We are not dealing with dumpstate file yet!")

    except FileNotFoundError:
        return "Please verify file format! Accepted Dumpstate and logcat"


def get_problems():
    # It will get the problems from user
    pass


def get_key_words(problems):
    # For each problem, it will return a list os key words from DB
    pass


def parse_log_with_key_words(key_words):
    # It will parse the log getting all lines that have the key words
    pass


if __name__ == "__main__":
    print('Starting Project:')
    log_file = '/home/lucaslb/dev/Lessie/media/logcat_1.txt'

    log = read_log(log_file)
    print(log.readlines())
