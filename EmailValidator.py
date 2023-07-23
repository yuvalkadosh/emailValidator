import requests
import argparse
import terminal_banner

parser = argparse.ArgumentParser()
parser.add_argument('-e', dest="email", help='Email to validate')
parser.add_argument('-f', dest="file", help='List of emails to validate')
parser.add_argument('-o', dest="output", help='Output file for valid emails')
args = parser.parse_args()

def email_validation():
    email = args.email
    file = args.file
    output = args.output
    url = 'https://login.microsoftonline.com/common/GetCredentialType/'
    if (email is None) and (file is None):
        mytextBanner = "\nYou didn't enter any email to validate.\n\nUse -e to validate single email\nUse -f to validate a list of emails\nUse -o to export the valid emails to a file\n"
        mybanner = terminal_banner.Banner(mytextBanner)
        print(mybanner)
    
    elif email is not None:
        request = requests.post(url, data='{"Username":"%s"}' % email)
        response = request.json()
        if "IfExistsResult" in response:
            invalid = response["IfExistsResult"]==1
            valid = response["IfExistsResult"]==0
        else:
            print("no such header: IfExistsResult")
        if invalid:
            print(email + ' is invalid')
        if valid and output is None:
                print(email + ' is valid')
        if valid and output is not None:
            print(email + ' is valid')
            with open(output, 'w') as output_file:
                output_file.write(email+'\n')         
    
    elif file is not None:
        with open(file) as file:
            for line in file:
                s = requests.session()
                line = line.split()
                email = ' '.join(line)
                request = requests.post(url, data='{"Username":"%s"}' % email)
                response = request.json()
                if "IfExistsResult" in response:
                    invalid = response["IfExistsResult"]==1
                    valid = response["IfExistsResult"]==0
                else:
                    print("no such header: IfExistsResult")
                if invalid:
                    print(email + ' is invalid')
                if valid and output is None:
                    print(email + ' is valid')
                if valid and output is not None:
                    print(email + ' is valid')
                    with open(output, 'a+') as output_file:
                        output_file.write(email+'\n')         

if __name__ == "__main__":
    email_validation()
