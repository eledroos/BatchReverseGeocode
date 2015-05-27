# import necessary modules
import pandas as pd
import json, requests, logging

# configure logging for our tool
lfh = logging.FileHandler('reverseGeocoderLOG.log')
lfh.setFormatter(logging.Formatter('%(levelname)s %(asctime)s %(message)s'))
log = logging.getLogger('reverseGeocoder')
log.setLevel(logging.INFO)
log.addHandler(lfh)

# load the gps coordinate data
df = pd.read_csv('LocationHistory - Batch 5.csv')

# create new columns
df['geocode_data'] = ''
df['city'] = ''
df['country'] = ''



df.head()

# function that handles the geocoding requests
def reverseGeocode(latlng):   
    result = {}
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    #apikey = 'API_KEY_GOES_HERE' #Project 1


    try:
		response = requests.get(url, params={"key":apikey, "latlng":latlng})
		response.raise_for_status()
    except requests.exceptions.RequestException as e:
		# this will log the whole traceback
		logger.exception("call failed with %s", e)
		# here you either re-raise the exception, raise your own exception,
		# or return anything
		return None

    data = response.json()
    log.info(data)

    if len(data.get('results')) > 0:
    	result = data['results'][0]['address_components']
    	#results = data['results'][0]
    	return result
    #else:
    #	return {
    #	    'city': '',
    #        'country': ''
    #	}

    #for item in result:
    #    if 'locality' in item['types']:
    #        city = item['long_name']
    #    elif 'country' in item['types']:
    #        country = item['long_name']



    #return {
    #    'city': city,
    #    'country': country
    #}

# comment out the following line of code to geocode the entire dataframe
#df = df.head()

for i, row in df.iterrows():
    # for each row in the dataframe, geocode the lat-long data
    df['geocode_data'][i] = reverseGeocode(df['Location'][i])
    #df['city'] = revGeocode['city']
    #df['country'] = revGeocode['country']
    print "Reverse Geocoding Row: ", i
df.head()

for i, row in df.iterrows():
    print "Determining City & Country: ", i
    #if 'address_components' in row['geocode_data']:
        
    # first try to identify the country
    for component in row['geocode_data']:#['address_components']:
        if 'country' in component['types']:
            df['country'][i] = component['long_name']
    
    # now try to identify the municipality
    for component in row['geocode_data']:#['address_components']:
        if 'locality' in component['types']:
            df['city'][i] = component['long_name']
            break
        elif 'postal_town' in component['types']:
            df['city'][i] = component['long_name']
            break
        elif 'administrative_area_level_2' in component['types']:
            df['city'][i] = component['long_name']
            break
        elif 'administrative_area_level_1' in component['types']:
            df['city'][i] = component['long_name']
            break

df.head()

df.loc[df['country']=='', 'country'] = ''
df.loc[df['city']=='', 'city'] = ''

df.to_csv('LocationHistory - Export 5.csv', encoding='utf-8', index=False)

print "Completed successfully"