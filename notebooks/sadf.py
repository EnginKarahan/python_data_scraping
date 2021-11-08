import pandas as pd # import als 'pd' Kürzel für weniger Schreibarbeit
import json

with open('guardian_corona_parsed.json', 'r', encoding = 'utf-8') as f:
    guardian = json.load(f)
#print(guardian[0].keys())

df = pd.DataFrame(guardian)
#print(df.info())

#print(df['chars'].describe())

#print(df.tags.value_counts()[:5])

peter = '''The screen is filled by the face of PETER PARKER, a 17 year 
old boy. High school must not be any fun for Petttter, he's one 
hundred percent nerd- skinny, zitty, glasses. His face is just 
frozen there, a cringing expression on it, which strikes us odd 
until we realize the image is freeze framed.'''

print(peter)