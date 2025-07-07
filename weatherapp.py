#Pakistan weather app using openweatherapi 
#importing all of them important modules
import requests
import sys

#creating class
class WeatherApp:
    def __init__(self):
        self.api_key = "YourOpenWeatherApiKeyHere"
        self.ip_api()
    def ip_api(self):
         try:
              response = requests.get("http://ip-api.com/json/")
              location_data = response.json()
              self.lat = location_data["lat"]
              self.lon = location_data["lon"]
              self.city_name = location_data["city"]
              self.state_code = location_data["regionName"]  # optional if you still want
              self.api_setting()
         except Exception:
              print("❌ Error while detecting location from IP.")

    def api_setting(self):
        try:
            self.weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.api_key}&units=metric"
            self.data_fetching = requests.get(self.weather_api_url)
            self.data = self.data_fetching.json()
            self.show_weather_info()
        except Exception:
             print("""-- An Error Occured --
1: Check Wether All Info is Added Correctly
2: Check Your Internet Connection
3: Check If the Server Site Is Responding or Not""")
        
    def show_weather_info(self):
         print(f"<--- Weather Report for {self.city_name}, {self.state_code} --->")
         self.temp_celcius = self.data["main"]["temp"]
         self.temp_farenheit = (self.temp_celcius * 9/5) + 32
         print(f"Temperature in celcius ->{self.temp_celcius:.1f} | Fareneheit is ->{self.temp_farenheit:.1f}")
         self.feels_like_temp = self.data["main"]["feels_like"]
         print(f"Feels Like {self.feels_like_temp:.1f}")
         if self.temp_celcius >= 45:
              print("🔥 Extremely Hot (Stay hydrated)")
         elif self.temp_celcius > 35 and self.temp_celcius < 44.9:
              print("🥵 Very Hot (Limit outdoor activity)")
         elif self.temp_celcius > 30 and self.temp_celcius < 34.9:
              print("🌞 Hot (Sunblock recommended)")
         elif self.temp_celcius > 25 and self.temp_celcius < 29.9:
              print("☀️ Warm (Pleasant but sunny)")
         elif self.temp_celcius > 15 and self.temp_celcius < 24.9:
              print("🙂 Mild (Comfortable weather)")
         elif self.temp_celcius > 5 and self.temp_celcius < 14.9:
              print("🧥 Cool (Light jacket weather)")
         elif self.temp_celcius > 0 and self.temp_celcius < 4.9:
              print("❄️ Cold (Bundle up)")
         elif self.temp_celcius > -10 and self.temp_celcius < -0.1:
              print("🥶 Very Cold (Limit exposure)")
         elif self.temp_celcius < -10:
              print("🧊 Freezing (Dangerously cold)")

         self.user_input = 0
         self.user_choice_menu()

    def user_choice_menu(self):
         while True:
          try:
               self.user_input = int(input("""-- Enter Your Choice --
1: More Info
2: Deep Info
3: Exit --> """))
               if self.user_input == 1:
                    self.more_basic_info()
               elif self.user_input == 2:
                    self.deep_info()
               elif self.user_input == 3:
                    sys.exit()  
               else:
                    print("Kindly enter the number in range")               
          except ValueError:
               print("""-- Error --
1: Do not Enter Something else e.g(/,*,+ or a,b,hello)
2: Check Wether Your Entered Number is in Range or Not""")
               
    def more_basic_info(self):
         self.humidity = self.data["main"]["humidity"]
         self.pressure = self.data["main"]["pressure"]
         print(f"Humidity is --> {self.humidity}%")
         if self.humidity < 30:
                print("🧴 Dry air – you may feel parched or have dry skin.")
         elif 30 <= self.humidity <= 50:
                print("😊 Comfortable humidity – you’re chilling.")
         elif 51 <= self.humidity <= 60:
                print("😐 Slightly humid – you might feel a little sweaty.")
         elif 61 <= self.humidity <= 70:
                print("😓 Humid – the air is getting sticky.")
         elif 71 <= self.humidity <= 85:
                print("🥵 Very humid – feels heavy and sticky.")
         else:
                print("🌧️ Extremely humid – like walking through soup.")

         print(f"Pressure is --> {self.pressure} hpa")

    def deep_info(self):
         self.wind_speed = self.data["wind"]["speed"]
         self.wind_direction = self.data["wind"]["deg"]
         self.visibility = self.data["visibility"]
         print(f"Wind Speed Is --> {self.wind_speed}m/s")
         print(f"Wind Direction Is --> {self.wind_direction}°")
    
         visibility_km = self.visibility / 1000

         if visibility_km >= 10:
           clarity = "Excellent"
         elif visibility_km >= 6:
           clarity = "Good"
         elif visibility_km >= 2:
           clarity = "Moderate"
         else:
           clarity = "Poor"

         print(f"👁️  Visibility: {visibility_km:.1f} km ({clarity})")

weather_app = WeatherApp()
