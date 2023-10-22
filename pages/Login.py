import streamlit as st
from Hello import params
import webbrowser, requests
from streamlit_javascript import st_javascript


try:
    url = params.initialAppURL+f"api/getExistingCode?state={params.state}"
    exists = requests.get(url)
    content = exists.json()
    if content["exists"] == False:
        url = f"https://oauth.battle.net/oauth/authorize?response_type=api/code&client_id=1bc88a090bc14ad48d20b0e9e7d1e917&redirect_uri={params.initialAppURL}code&state={params.state}"
        js = f'window.open("{url}", "_blank").then(r => window.parent.location.href);'
        st_javascript(js)
    else:
        st.write(content["token"])
except requests.exceptions.ConnectionError :
    url = f"https://oauth.battle.net/oauth/authorize?response_type=api/code&client_id=1bc88a090bc14ad48d20b0e9e7d1e917&redirect_uri={params.initialAppURL}code&state={params.state}"
    js = f'window.open("{url}", "_blank").then(r => window.parent.location.href);'
    st_javascript(js)