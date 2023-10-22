import streamlit as st
import requests
import webbrowser
from classes.queryParams import params

webbrowser.open(f"https://oauth.battle.net/oauth/authorize?response_type=code&client_id=1bc88a090bc14ad48d20b0e9e7d1e917&redirect_uri=https://bnetstats.streamlit.app/code&state={params.state}")