# emailValidator
**Description**

emailValidator.py is a Python script designed to validate Office 365 (o365) email addresses. It provides a simple command-line interface to check the validity of single emails, a file containing a list of emails, and allows you to output the valid emails to a specified file.


**Usage**

Execute the script using the following command format:

python3 emailValidator.py [flags] [arguments]

The script accepts the following flags:

-e: Validates a single email address.

-f: Validates a file containing a list of email addresses.

-o: Specifies the output file for valid email addresses.


**Examples**

To validate a single email address:

python3 emailValidator.py -e example@example.com

To validate a file containing a list of email addresses:

python3 emailValidator.py -f path/to/email_list.txt

To specify an output file for valid email addresses:

python3 emailValidator.py -f path/to/email_list.txt -o path/to/valid_emails.txt


**Requirements**

-requests

-argparse

-terminal_banner
