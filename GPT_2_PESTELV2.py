"""
GPT_2_PESTELV2
"""

#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


from openai import OpenAI
from docx import Document

# Configuración de la clave de la API de OpenAI
# falta añadir el panorama internacional
client = OpenAI(api_key="YOUR_API_KEY_HERE")


# In[ ]:





# In[8]:


import requests
from datetime import datetime

def fetch_imf_country_data(country_code, start_year, end_year):
    """
    Fetch macroeconomic indicators for a given country and time range from the IMF API.

    :param database_id: ID of the database to query (e.g., 'IFS' for International Financial Statistics).
    :param country_code: ISO country code (e.g., 'BO' for Bolivia).
    :param start_year: Starting year of the data range.
    :param end_year: Ending year of the data range.
    :return: Response from the IMF API as a JSON object.
    """
    base_url = "https://www.imf.org/external/datamapper/api/v1"

    #https://www.imf.org/external/datamapper/api/v1/NGDP_RPCH?periods=2019,2020
    #https://www.imf.org/external/datamapper/api/v1/NGDP_RPCH.?startPeriod=2019&endPeriod=2024
    # Generate periods string
    periods = ','.join(str(year) for year in range(start_year, end_year + 1))

    # Prepare the query URL (Querying for all available indicators)
    query_url = f"{base_url}/{country_code}.?Period={start_year},{end_year}"
    print(query_url)
    # Make the request to the IMF API
    response = requests.get(query_url)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"

# Example usage: Fetching data for Bolivia from the International Financial Statistics database for the last 5 years
#database_id = 'IFS'
country_code = 'NGDP_RPCH'
current_year = datetime.now().year
start_year = current_year - 5
end_year = current_year - 4

data = fetch_imf_country_data(country_code, start_year, end_year)

print(data)


# In[ ]:






if __name__ == "__main__":
    pass
