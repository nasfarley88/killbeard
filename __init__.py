import os
import logging
import signal

from telegram.ext import CommandHandler
from skybeard.beards import Beard


logger = logging.getLogger(__name__)


class KillBeard(Beard):
    """Kills the currently running bot.

    Type /kill to terminate the bot.

    This beard is designed to stop the bot running, so that if it is in an
    infinite loop it can restart. E.g.

    while true;
        do ./main.py -k 14351345-32asdfafahj4380fhunffjoadsfafub;
    done;

    """

    def initialise(self):
        self.disp.add_handler(CommandHandler("kill", self.kill))

    def kill(self, bot, update):
        update.message.reply_text("Daisy, daisy...")
        os.kill(os.getpid(), signal.SIGTERM)

