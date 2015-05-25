##Python Batch Reverse Geocoder
A small tool I made to take location data from Google Takeout (acquired through Google Maps), and make a call with the Google Maps Geolocation API to reverse geocode the coordinates. You'll need to convert the JSON file to a CSV for this tool, which can be done through [this script](https://github.com/Scarygami/location-history-json-converter). 

Use my batch file, with the above tool to convert the JSON to a CSV. As long it's all in the same folder, and you didn't change any filenames from their default values, double-clicking the batch file will auto-generate the CSV file for this project.

I used Anaconda Python 2.7 for this tool, pandas comes right with it.

Go to [Google Console](http://console.google.com/projects/) to create a Project and with it, a Google Maps Geolocation API Server Key. Then place that key in the 'AUTH_KEY' field of ReverseGeocoding.py.

The Geolocation API accepts Coordinates in the format "-xx.xxx,x.xxx" - with no space between the coordinates. I couldn't figure out if it accepted them as a string instead of two double values - and it seems that it does (which is dumb) but that's just how it's done. 