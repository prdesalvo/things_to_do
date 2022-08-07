# import requests #requests is imported via google search. Google search also uses an older version of requests
from googlesearch import search
import requests
from bs4 import BeautifulSoup

header = {"User-Agent": "Requests"}
import pandas as pd


def the_knot_places(city):
    knot_lst = []
    headings = []  #collect the headings
    place_images = []
    places = pd.DataFrame(columns=['heading', 'description', 'place_image', 'site', 'place', 'couples_names', 'wedding_date'])

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

            #Get the couple names
            if soup.find("h1", {"data-testid": "header-couple-names"}):
                couples_names = soup.find("h1", {"data-testid": "header-couple-names"}).text
            else:
                pass

            #Get the wedding date
            if soup.find("div", {"data-testid": "header-wedding-date-location"}):
                wedding_date = soup.find("div", {"data-testid": "header-wedding-date-location"}).text
            else:
                pass

            #Grab the headings and places
            elements = soup.find_all(['h3', 'h4', 'h5', 'h6', 'p', 'img'])

            if 'p' in [tag.name for tag in elements]:  #check if there are paragraphs because it means the person actually spent time making the list
                for i in elements:
                    if 'h' in i.name:
                        headings.append(i.text)
                        place_images.append('No image')
                        print(i.text)
                    
                    elif i.has_attr("data-nimg"):
                      place_images[-1] = i['src']

                    elif 'p' in i.name and headings:
                        description = i.text
                        heading_for_place = headings[-1]
                        image_for_place = place_images[-1]
                        places.loc[len(places)] = [heading_for_place, description, image_for_place, poi_link, city, couples_names, wedding_date]
                    else: 
                        pass
            else:
                pass
        else:
            pass
    
    results = places.groupby(['heading', 'site', 'place', 'place_image', 'couples_names', 'wedding_date'])['description'].apply('<br>'.join).reset_index().sort_values(by=['site'])
    results_lst = results.values.tolist()

    return results_lst
    # return results
