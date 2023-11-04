# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
from classes.queryParams import params
import jose.jwt as jwt
from utils import openURL
import time
from streamlit.delta_generator import DeltaGenerator
import requests
#import fastapi
#import uvicorn

LOGGER = get_logger(__name__)
KEY = "$2y$10$JBZsW3Td414dxemijbOinum8Eb.EJYfZdC3ZTyhVELQNr4OtJpLpe"
#app = fastapi.FastAPI()

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
        menu_items={
          "About" : "BattleNetStats, an app made by Lich911. \n By using it, you accept the following :"
        }
    )
    page = st.empty()
    with page.container():
      st.write("""
      # BNetStats, un outil de statistiques Blizzard
             
        Bienvenue dans **VOTRE** outil de statistiques. Vous trouverez de nombreuses fonctionnalités.
        Qu'attendez-vous ? Plongez dans la découverte de votre WEB application personnelle ! :-)
      """)

    try:
      params.initialAppURL = st.experimental_get_query_params()["initialAppURL"][0]
      params.sessionKey = st.experimental_get_query_params()["sessionKey"][0]
      params.sessionKey = jwt.decode(params.sessionKey, key=KEY, algorithms='HS256')["initialTime"]
    except KeyError:
      pass
    redirect = params.initialAppURL+"api/code"
    params.state = jwt.encode({"initialAppURL" : redirect, "initialTime" : str(params.sessionKey)}, key=KEY, algorithm='HS256')
    canvas = st.empty()

    def launchLogin():
      if "loggingState" not in st.session_state:
         st.session_state.loggingState = True
      else:
         st.session_state.loggingState = True
      url = f"https://oauth.battle.net/oauth/authorize?response_type=code&client_id=1bc88a090bc14ad48d20b0e9e7d1e917&redirect_uri=https://short.universjeux.info/bnetStats/&state={params.state}&scope=openid"
      openURL(url)
      canvas.empty()
    
    def Login():
        if "loggingState" in st.session_state:
            if st.session_state.loggingState:
              while requests.get(params.initialAppURL+f"api/getExistingCode?state={params.state}").text.find("token") == -1:
                time.sleep(1)
                canvas.button("En attente de la connexion...", disabled=True)
              st.write("Connexion réussie !")
              st.session_state.loggingState = False
        else:
          st.session_state.loggingState = False
          url = params.initialAppURL+f"api/getExistingCode?state={params.state}"
          exists = requests.get(url)
          content = exists.json()
          print(exists.text)
          try:
            if content["exists"] == False:
                raise KeyError()
            else:
                params.token = content["token"]
                canvas.empty()
                canvas.write("Vous êtes déjà connecté ! Explorez les outils qui s'offrent à vous ci-dessous :")
          except KeyError:
            canvas.empty()
            with canvas.container():
              st.write("Vous ne semblez pas connecté, connectez-vous avec le bouton ci-dessous :")
              st.button(label="Se connecter avec BattleNet", on_click=launchLogin)
    
    Login()
        
    st.sidebar.caption("By using this app you accept Blizzard's TOS and BnetStat's one.")
    col1, col2 = st.sidebar.columns(2)
    with col1:
      st.link_button("Blizzard TOS", "https://www.blizzard.com/en-us/legal/a4380ee5-5c8d-4e3b-83b7-ea26d01a9918/blizzard-entertainment-online-privacy-policy")
    
    with col2:
        st.button("BnetStats TOS")


if __name__ == "__main__":
    run()
    #uvicorn.run("Hello:app", port=8000, host="172.16.5.4")
