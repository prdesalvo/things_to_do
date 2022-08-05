# import requests #requests is imported via google search. Google search also uses an older version of requests
from googlesearch import search
import requests
from bs4 import BeautifulSoup

header = {"User-Agent": "Requests"}
import pandas as pd


def the_knot_places(city):

    knot_lst = []
    headings = []  #collect the headings
    places = pd.DataFrame(columns=['heading', 'description', 'site', 'place'])

    query = f"{city} wedding website things to do the knot"

    link_lst = search(query, tld="co.in", num=10, stop=10, pause=2)

    for link in link_lst:
        if ('theknot' in link) & ('marketplace' not in link):
            poi_link = "/".join(str.split(link, "/")[:5] + ["things-to-do"])
            knot_lst.append(poi_link)
            print(poi_link)

            #scrap the page
            page = requests.get(poi_link, headers=header)
            soup = BeautifulSoup(page.content, "html.parser")

            #Grab the headings and places
            h_and_p_tags = soup.find_all(['h3', 'h4', 'h5', 'h6', 'p'])

            if 'p' in [
                    tag.name for tag in h_and_p_tags
            ]:  #check if there are paragraphs because it means the person actually spent time making the list
                for i in h_and_p_tags:
                    if 'h' in i.name:
                        headings.append(i.text)
                        print(i.text)
                    elif 'p' in i.name and headings:
                        places.loc[len(places)] = [
                            headings[-1], i.text, poi_link, city
                        ]
                    else:
                        pass
            else:
                pass
        else:
            pass

    results = places.groupby([
        'heading', 'site', 'place'
    ])['description'].apply('<br>'.join).reset_index().sort_values(by=['site'])
    results_lst = results.values.tolist()

    return results_lst