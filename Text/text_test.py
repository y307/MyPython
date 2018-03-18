

import pyowm

owm = pyowm.OWM('67f0d157b2ae7466f46377e76d4c5670')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
# observation = owm.weather_at_place('London,GB')
observation = owm.weather_at_place('Kyiv')
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>
