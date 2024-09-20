import sys
import os 
import requests

from requests.auth import HTTPProxyAuth
from datetime import datetime
import random
import json



class Hmaster:
    def __init__(self):
        # Get the directory where the script is located
        main_dir = os.path.dirname(os.path.realpath(__file__))

        # Get the directory of the data file
        data_dir = os.path.join(main_dir, "data.json")

    