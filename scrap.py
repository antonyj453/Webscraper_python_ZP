from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
            
            s = "https://www.zoopla.co.uk/to-rent/houses/en1/?identifier=en1&property_type=houses&q=EN1&radius=0&page_size=10&pn=2"
            response = get(sapo, headers=headers)
            
            html_soup = BeautifulSoup(response.text, 'html.parser')
            house_containers = html_soup.find_all('div', class_="listing-results-right clearfix")
            p=str(house_containers)
            file1 = open("F:/house_rent_page2.txt","w")
            file1.writelines(p) 
            file1.close()
