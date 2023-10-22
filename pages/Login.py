import streamlit as st
from Hello import params
import webbrowser, requests


try:
    exists = requests.get(params.initialAppURL+f"getExistingCode?state={params.state}")
    if not exists.json()["exists"] :
        webbrowser.open(f"https://oauth.battle.net/oauth/authorize?response_type=code&client_id=1bc88a090bc14ad48d20b0e9e7d1e917&redirect_uri={params.initialAppURL}code&state={params.state}")
    else:
        st.write(exists.json()["token"])
except requests.exceptions.ConnectionError :
    pass

webbrowser.open(f"https://oauth.battle.net/oauth/authorize?response_type=code&client_id=1bc88a090bc14ad48d20b0e9e7d1e917&redirect_uri={params.initialAppURL}code&state={params.state}")
