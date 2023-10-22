import streamlit as st
from Hello import params
import webbrowser, requests


try:
    url = params.initialAppURL+f"api/getExistingCode?state={params.state}"
    exists = requests.get(url)
    st.write(exists.json())
    content = exists.json()
    if content["exists"] == False:
        webbrowser.open(f"https://oauth.battle.net/oauth/authorize?response_type=api/code&client_id=1bc88a090bc14ad48d20b0e9e7d1e917&redirect_uri={params.initialAppURL}code&state={params.state}")
    else:
        st.write(content["token"])
except requests.exceptions.ConnectionError :
    pass

webbrowser.open(f"https://oauth.battle.net/oauth/authorize?response_type=code&client_id=1bc88a090bc14ad48d20b0e9e7d1e917&redirect_uri={params.initialAppURL}api/code&state={params.state}")
