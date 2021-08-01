"""
    Purpose: collection of tools to interact with a gmail account to set up alerts and monitoring tasks
"""
import os
import smtplib, ssl
import slack_sdk
# import slack_api
from datetime import datetime
# list should consist of any one who needs to know when the opcua server scraping and pushing to DB is
# down
import slack_sdk.webhook

# web hook for sadie random channel bot
web_hook = 'https://hooks.slack.com/services/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'
receiver_emails = ["gjones2@vols.utk.edu",
                   'xli27@utk.edu',
                   'jfreder9@vols.utk.edu',
                   ]# Enter receiver addresses

# set of generic messages for the issues we come across
SERVER_msg = "There is some issue with the opcua server at {}"
DB_msg = "There is some issue with Connecting to the DB:\n{}"

# Generic Gmail account class
class GMAIL_ACCOUNT:
    """
        Class representing a gmail account
    """
    def __init__(self, username, pwd, phone, fname=None, lname=None):
        self.username = username.strip() + "@gmail.com"
        self.password = pwd
        self.phone = phone
        self.fname = fname
        self.lname = lname

class SADIE_ALERT_SLACK_BOT:
    # this is the environment variable where the web hook should be stored
    # this is the name that the bot will look for when trying to get the hook
    # from the environment. It requires that an environmental variable be set with
    # the appropriate webhook for the terminal that will run the scrapper. This is done
    # for security purposes.
    web_hook_name = 'https://hooks.slack.com/services/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'

    def __init__(self, webhook=None):
        self.webhook=webhook


    def set_webhook(self):
        self.webhook = os.environ[self.web_hook_name]

    # post message to channel I am authorized to access
    def post_message(self, alert_message='Hi from OPCUA scrapper'):
        WHclient = slack_sdk.webhook.WebhookClient(self.webhook)
        return WHclient.send(
            text=alert_message,
            blocks=[
                {
                    "type": 'header',
                    'text': {
                        "type": 'plain_text',
                        'text': "*OPCUA ALERT*",
                    },
                },
                {
                    "type": 'section',
                    'text': {
                        "type": 'mrkdwn',
                        'text': alert_message,
                    },
                },

            ]
        )




class sadie_monitor:
    # Generic gmail account information
    gj_user = 'SADIEMONITORgj'
    gj_pwd = 'SADI3se@cr3t$'
    gj_screen_name = "_SADIE_MONITOR"

s_mon = sadie_monitor
# class for the sadie monitor gmail account
class SADIE_MONITOR_GMAIL(GMAIL_ACCOUNT):
    def __init__(self, username=s_mon.gj_user, pwd=s_mon.gj_pwd, phone=None, fname=None, lname=None, ):
        super().__init__(username, pwd, phone, fname, lname)

SADIE_Messenger = SADIE_MONITOR_GMAIL()

Sadie_sender_email = SADIE_Messenger.username # Enter your address
# password = input("Type your password and press enter: ")
Sadie_sender_password = SADIE_Messenger.password

sadie_alert_slack_bot = SADIE_ALERT_SLACK_BOT(webhook=web_hook)


# sends a single email with the given message using the sadie monitor as the sender
# by default
def send_alert_gmail(receiver_email=receiver_emails[0], sender_email=Sadie_sender_email, sender_pwd=Sadie_sender_password,
                     msg="From: Sadie Monitor\n to: {}\n\nEmpty message\n".format(receiver_emails)):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    print('sender {}, receiver {}'.format(sender_email + " " + sender_pwd,receiver_email))
    # set up context and sent the message
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_pwd)
        server.sendmail(sender_email, receiver_email, msg)


# Send multiple emails
def send_alert_gmails(receiver_emails=receiver_emails[0], sender_email=Sadie_sender_email, sender_pwd=Sadie_sender_password,
                     msg="From: Sadie Monitor\n to: {}\n\nEmpty message\n".format(receiver_emails)):
    for receiver_email in receiver_emails:
        send_alert_gmail(receiver_email, sender_email, sender_pwd, msg)


# sends alerts to the given receiver email and the slack bot with t
def send_alert_to_all(reciever=receiver_emails[0],
                      sender=Sadie_sender_email,
                      sender_pwd=Sadie_sender_password, alert_message=""):
    sadie_alert_slack_bot.post_message(alert_message)
    send_alert_gmail(reciever, sender, sender_pwd, alert_message)

