# FetchWeather

FetchWeather collects information from openweathermap.org for the given city

## Preliminary

Install third party module: Requests

```bash
pip install requests
```

### 1.Obtain an [API key](https://openweathermap.org/api)
Change the API key on line 13 to your personal key

### 2. Obtain [2 digit country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
Select your desired country code to input with the city.

## Usage

```python
import json, requests

APPID = 'YOUR API KEY HERE' #line 13
```