import pandas as pd, numpy as np, plotly.express as px, datetime, plotly.io as pio

pio.renderers.default = 'vscode'

df_raw = pd.read_csv(r'https://query.data.world/s/3awolttfgoorbr2rfjhrvxfrdlgvbe')
colnames = ['Date', 'Country_Region', 'Province_State', 'Case_Type', 'Cases', 'Lat', 'Long']
df = df_raw[colnames]

df['Date'] = pd.to_datetime(df['Date'])

polska = df.loc[df['Country_Region'] == 'Poland']

#polska_pivot = polska.pivot_table(index = 'Date',columns = 'Case_Type', values = 'Cases', aggfunc="sum")

#polska_pivot = polska_pivot.loc['2020-03-01':datetime.date.today()-datetime.timedelta(days=1)]

polska.set_index('Date')

start = datetime.date(2020,3,1)

polska = polska[polska['Date'] > start]

fig = px.area(polska, x = 'Date', y = 'Cases', color = 'Case_Type')
fig.show()