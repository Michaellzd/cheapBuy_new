from unittest.mock import patch

import requests

import configparser



def send_email_via_mailgun(recipient, subject, text):

    DOMAIN_NAME = "*"
    API_KEY = "*"

    return requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN_NAME}/messages",
        auth=("api", API_KEY),
        data={"from": f"Excited User <mailgun@{DOMAIN_NAME}>",
              "to": [recipient],
              "subject": subject,
              "text": text})







if __name__ == '__main__':
    send_email_via_mailgun("michaellu239@gmail.com","Thanks","your abx")