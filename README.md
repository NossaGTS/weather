# weather
Script to pull current conditions and put it into my polybar config

## Dependencies
### Python:
1. requests [https://pypi.org/project/requests/]
  `pip install requests`
2. python-dotenv [https://pypi.org/project/python-dotenv/]
  `pip install python-dotenv`
### Fonts:
1. Nerdfonts v3.2.1 [https://www.nerdfonts.com/#home]
2. Install your desired font onto your computer before configuring polybar script.

## How to Use
1. You must apply for an api key at https://openweathermap.org/api by signing up for an account.
2. Once you have an API key. Create a .env file in repository directory.
3. The .env file should follow the following format
     ```
     API_KEY=xxxx - api key received from openweathermap
     LAT = xx.xxxx - latitude of your current location
     LONG = xx.xxxx longitude of your current location
     METRIC = `  standard | metric | imperial - your preferred unit of measurement
     ```
## Polybar config
1. in your polybar config file, define where you would like the module to display (e.g. modules-left, modules-center, modules-right)
2. Once you define it, add the following section to your polybar config.ini
 ```
[module/weather]
type = custom/script
exec = /PATH/TO/PYTHON/SCRIPT
interval = time in miliseconds (please note, with this API you only get 1000 calls a day for free, so try to be mindful of what you set your interval to.)
[optional]
label-font = custom font you would like to use.
label-padding = 1 ; add padding around the module
label-foreground = ${colors.primary} ; theme label to follow color scheme (must have a section in your polybar config called [colors] with a color named primary else change it to whatever you named your colors)
```
