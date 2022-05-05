import logging
from songcollection import SongCollection
from tracklister import TrackLister
from djcontroller import DjController
import essentia
import os

import loading
# LOG LEVEL - loggin.INFO
LOG_LEVEL = loggin.DEBUG
LOGFORMAT = "%(log_color)s%(message)s%(reset)s"
from colorlog import ColoredFormatter
logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOGFORMAT)
stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
logger = logging.getLogger('colorlogger')
logger.setLevel(LOG_LEVEL)
logger.addHandler(stream)

if __name__ == '__main__':

    sc = SongCollection()
    tl = TrackLister(sc)
    dj = DjController(tl)

    essentia.log.infoActive = False
    essentia.log.warningActive = False
    
    while(True):
        try:
            cmd_split = str.split(input('> : ', ' '))
        except KeyboardInterrupt:
            logger.info('Goodbye!')
            break
        cmd = cmd_split[0]
        if cmd == 'loaddir':
            if len(cmd_split) == 1:
                logger.warning('Please provide a directory name to load!')
                continue
            elif not os.path.isdir(cmd_split[1]):
                logger.warning(cmd_split[1] + ' is not a valid directory!')
                continue
            sc.load_directory(cmd_split[1])
            logger.info(str(len(sc.songs)) + ' songs loaded [annoted: ' + str(len(sc.get_annotated())) + ']')