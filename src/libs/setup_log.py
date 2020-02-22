
import time
import logging


class SetupLogging:

    @staticmethod
    def setup_logging():
        the_level = logging.INFO
        tss = str(time.time())[:9]
        fname = "balanceTransfers" + tss + ".log"
        logging.basicConfig(filename=fname, level=the_level)
