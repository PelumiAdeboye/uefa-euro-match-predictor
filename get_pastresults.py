from bs4 import BeautifulSoup
import requests 
import pandas as pd

years = [1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]


def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/UEFA_Euro_{year}'
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    matches = soup.find_all('div', class_='footballbox')


    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        away.append(match.find('th', class_='faway').get_text())

    dict_football = {'home': home, "score": score, 'away': away} 
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    return df_football

# Historical data
Uefa_Euros = [get_matches(year) for year in years]
df_uefa = pd.concat(Uefa_Euros, ignore_index=True)
df_uefa.to_csv('Uefa_euros_historical_data.csv', index=False)

#2024 Fixtures
df_fixture = get_matches(2024)
df_fixture.to_csv('Uefa_euros_fixture.csv', index=False)