from unittest.mock import patch

import requests

import unittest


def send_email_via_mailgun(recipient, subject, text):
    DOMAIN_NAME = "sandboxeaf5b10da15243b2af8bd56a4f6476f2.mailgun.org"
    API_KEY = "9586a3fdd432caf3db0b22ca4603ad47-77316142-e8784074"

    return requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN_NAME}/messages",
        auth=("api", API_KEY),
        data={"from": f"Excited User <mailgun@{DOMAIN_NAME}>",
              "to": [recipient],
              "subject": subject,
              "text": text})


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxeaf5b10da15243b2af8bd56a4f6476f2.mailgun.org/messages",
        auth=("api", "9586a3fdd432caf3db0b22ca4603ad47-77316142-e8784074"),
        data={"from": "Excited User <mailgun@sandboxeaf5b10da15243b2af8bd56a4f6476f2.mailgun.org>",
              "to": ["michaellu239@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomeness!"})





if __name__ == '__main__':
    send_email_via_mailgun("michaellu239@gmail.com","Thanks","your abx")