import plotly.offline as go_offline
import plotly.graph_objects as go
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/18X1VM1671d99V_yd-cnUI1j8oSG2ZgfU_q1HfOizErA/export?format=csv&id'
data = pd.read_csv(url)
data = data.fillna(0)

