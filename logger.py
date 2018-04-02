# -*- coding:utf-8 -*-
# Logging System

import sys
import os
import logging

LOG_FILE_PATH = 'log/electricity-monitor.log'
OUTPUT_FORMAT = '%(asctime)s %(name)s %(levelname)s: %(message)s'
FILE_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
DATE_FORMAT = '%a, %d %b %Y %H:%M:%S'
FILE_LOG_LEVEL = logging.DEBUG
OUTPUT_LOG_LEVEL = logging.INFO

REAL_PATH = os.path.split(os.path.realpath(sys.argv[0]))[0]

def abspath(path):
    return os.path.join(REAL_PATH, path)

def register(name):
    # Configure logging
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(OUTPUT_FORMAT, datefmt=DATE_FORMAT)

    # Use FileHandler to output to file
    fh = logging.FileHandler(os.path.join(REAL_PATH, LOG_FILE_PATH))
    fh.setLevel(FILE_LOG_LEVEL)
    fh_formatter = logging.Formatter(FILE_FORMAT, datefmt=DATE_FORMAT)
    fh.setFormatter(fh_formatter)

    # Use StreamHandler to output to screen
    ch = logging.StreamHandler()
    ch.setLevel(OUTPUT_LOG_LEVEL)
    ch.setFormatter(formatter)

    # Add Handlers
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger