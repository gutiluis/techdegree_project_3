#!/usr/bin/env python

# file: app.py
# descr:


import logging
import time
from logging import getLogger
from phrasehunter.game import Game


logger = logging.getLogger(__name__)
# only the root logger needs to be configured # logging.info()
logging.basicConfig(level=logging.INFO)




if __name__ == "__main__":
    game = Game()
    
    #logger.info(game.active_phrase.phrase)
    #
    # second line top
    #logging.info(time.asctime()) # logging is the highest level logger is root logger

    game.start()