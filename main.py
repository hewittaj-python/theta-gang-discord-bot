from dotenv import load_dotenv
import api_call as ac
import discord
import json
import os
import requests

user_trades = ac.get_user_trades("hewittaj")