from webexteamsbot import TeamsBot
import os
from file_read_backwards import FileReadBackwards
import re
import logging


# Setup logging
logging.basicConfig(filename='redacted/path', filemode='w', format='%(asctime)s - %(levelname)s - '
                                                                                      '%(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)


# Start Ngrok
logging.info("Starting ngrok (http) on port redacted, then sleeping for 5 sec...")
os.system("ngrok http redacted &")
os.system("sleep 5")


# Use FileReadBackwards to search most recent ngrok.log entries first
logging.info("Opening ngrok.log with FileReadBackwards...")
with FileReadBackwards("redacted/path", encoding="utf-8") as frb:
    # getting lines by lines starting from the last line up
    for line in frb:
        try:
            new_url = str(line)
            # Look for the "url=blahblahblah" chunk of chars
            logging.info("Looking for most recent string url=...")
            url_chunk = re.findall(r"url=https://[A-Za-z0-9\-]+\.ngrok-free\.app", new_url)
            # Ignore blank result lines
            if str(url_chunk) != "[]":
                # Pull the actual url from "url=blahblahblah"
                url = re.findall(r"https://[A-Za-z0-9\-]+\.ngrok-free\.app", str(url_chunk))
                # Strip the brackets from url contents in simplest way possible
                ngrok_logged_url = url[0]
                logging.info("...Found ngrok.log url: " + ngrok_logged_url)
                # Immediately exit the loop, creating a "first match wins" loop
                break
        except:
            logging.critical("...FAILED to find ngrok.log url via regex.")
            quit()


# Bot Variables.
bot_email = "redacted"
teams_token = "redacted"
bot_url = ngrok_logged_url
bot_name = "redacted"
approved_users = ["redacted"]


# Create a Bot Object.
logging.info("Creating bot object...")
bot = TeamsBot(
        teams_bot_name=bot_name,
        teams_bot_token=teams_token,
        teams_bot_url=bot_url,
        teams_bot_email=bot_email,
        approved_users=approved_users,
)


# A simple command that returns a basic string that will be sent as a reply
logging.info("Declaring def do_something...")


def do_something(incoming_msg):
    """
    Sample function to do some action.
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    return "i did what you said - {}".format(incoming_msg.text)


# Add new commands to the box.
logging.info("Adding new commands to the bot...")
bot.add_command("/dosomething", "help for do something", do_something)


if __name__ == "__main__":

    # Run Bot
    logging.info("Starting bot, host 0.0.0.0, port redacted...")
    bot.run(host="0.0.0.0", port=redacted)
