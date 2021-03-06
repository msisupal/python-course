# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 16:10:51 2016

@author: phil
"""

import socket
import os
import timeit
import logging

# Set up the logging
logging.basicConfig(
    format="%(asctime)s - %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)

# Parameters
# host = 'TBC'
host = '127.0.0.1'
port = 1234
repeats = 100  # Keep this <= 100, please!
timeout = 5  # Number of seconds until giving up on connection


# IN HERE WE WILL WRITE THE NETWORK LATENCY CODE

logger.info("Average time taken: {delay} ms".format(delay=average_return_time))
