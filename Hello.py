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
#import fastapi
#import uvicorn

LOGGER = get_logger(__name__)
KEY = "$2y$10$JBZsW3Td414dxemijbOinum8Eb.EJYfZdC3ZTyhVELQNr4OtJpLpe"
#app = fastapi.FastAPI()

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 👋")
    try:
      params.initialAppURL = st.experimental_get_query_params()["initialAppURL"][0]
      params.sessionKey = st.experimental_get_query_params()["sessionKey"][0]
      params.token = jwt.decode(params.sessionKey, key=KEY, algorithms='HS256')["initialTime"]
    except KeyError:
      pass
    
    params.state = jwt.encode({"initialAppURL" : params.initialAppURL+"api/code", "initalTime" : str(params.token)}, key=KEY)
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
    #uvicorn.run("Hello:app", port=8000, host="172.16.5.4")
