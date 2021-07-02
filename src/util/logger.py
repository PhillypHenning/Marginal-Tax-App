import os
import sys
import logging
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler
FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
FILE_NAME = 'app.log'
FILE_PATH = './logs'

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler

def get_file_handler(): 
    file_handle = os.environ.get('LOG_FILENAME', FILE_NAME)
    file_handle_folder = os.environ.get('LOG_PATH', FILE_PATH)

    LOG_FILE = "{}/{}".format(file_handle_folder, file_handle)

    open(LOG_FILE, 'a').close()
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    return file_handler

def get_logger(logger_name, file_name=None, log_dir=None, item_format=False):

    if file_name: 
        global FILE_NAME 
        FILE_NAME = file_name
    if log_dir: 
        global FILE_PATH 
        FILE_PATH = log_dir
    
    if item_format == True:
        global FORMATTER
        FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(logname)s: %(message)s")
    

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.propagate = 0
        logger.addHandler(get_console_handler())
        logger.addHandler(get_file_handler())
    return logger