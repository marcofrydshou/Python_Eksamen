World Population API
http://api.population.io/#!/countries/listCountries

Run through a List with a List
https://stackoverflow.com/questions/1012185/in-python-how-do-i-index-a-list-with-another-list

Countryname to CountryCode
https://stackoverflow.com/questions/38523559/is-it-possible-to-make-plotly-choropleth-use-iso-3166-1-alpha-2-country-codes-in

Extract Json
https://www.youtube.com/watch?v=19-LOqdI61k


Get countries

import urllib.request, json 
with urllib.request.urlopen("http://api.population.io:80/1.0/countries") as url:
    data = json.loads(url.read().decode())
    print(data)
    
    
Get population for specific country

date = '2015-12-24'
country = 'Brazil/'
url = "http://api.population.io:80/1.0/population/"
with urllib.request.urlopen(url + country + date) as url:
    data = json.loads(url.read().decode())
    print(data)


