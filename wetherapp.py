# import streamlit as st
# import requests
# import random
# st.header("Weather prediction app")
# st.write("The smart Weather app provides real time weather updates based on the city" \
# " name eneterd by the user. It also gives intelligent predictions and personalized " \
# "suggestions using live data from the open Weather API.")
# def weather_prediction(temp,desc,humidity):
#     desc=desc.lower()
#     if "rain" in desc or "drizzle" in desc:
#         return "lools rainy carry an umbrella and wear waterproof shoes."
#     elif "clear" in desc or "sun" in desc:
#         if temp>35:
#             return "its quite hot stay hydrated and avoid going out in the afternoon."
#         else:
#             return "nice and clear perfect day. "
#     elif "cloud" in desc:
#         return "cloudy skies ahead.you feel cool."
#     elif "snow" in desc:
#         return "its showing time for cup of coffee" 
#     elif humidity>80:
#         return "high humidity today-it might feel warmer than it is."
#     else:
#         return "the weather looks fine make the most of your day." 
# st.title("Smart weather Prediction App")
# st.write("enter your city name to get current weather details and smart prediction.") 
# city=st.text_input("city name")
# if st.button("get weather"):
#     if city.strip():
#         city=city.strip()

#         url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8f6b7b43f4f146c93fba5d4f4d0eabc2&units=metric"
#         #  url=f"https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
#         # url=f"https://api.openweathermap.org/data/2.5/forecast?q={city},IN&appid={API_KEY}&units=metric"
# "
#         res=requests.get(url)
#         data=res.json()
#         if str(data.get("cod"))==200:
#             temp=data["main"]["temp"]
#             humidity=data["main"]["humidity"]
#             desc=data["weather"][0]["description"]
#             st.subheader(f"weather in {city.title()}")
#             st.write(f"**Temprature:** {temp}°C")
#             st.write(f"**condition:** {humidity}%")
#             prediction=weather_prediction(temp,desc,humidity)
#             st.info(prediction)
#         else:
#             st.write("city not found please check the name")  
#     else:
#         st.write("please enter city name")          



import streamlit as st
import requests

st.header("🌦️ Smart Weather Prediction App")
st.write("""
The Smart Weather App provides real-time weather updates based on the city name entered by the user. 
It also gives intelligent predictions and personalized suggestions using live data from the OpenWeather API.
""")

def weather_prediction(temp, desc, humidity):
    desc = desc.lower()

    if "rain" in desc or "drizzle" in desc:
        return (
            "📌 **Suggested Plan:**\n"
            "🌧️ Looks like rain today!\n"
            "• Carry an umbrella or a light raincoat.\n"
            "• Try not to stay outside for too long.\n"
            "• Drive safely — roads may get slippery.\n\n"
            "🩺 **Doctor's Precautions:**\n"
            "• Keep yourself dry to avoid catching a cold.\n"
            "• Wash hands after getting wet to prevent infections.\n"
            "• Drink warm fluids like tea or soup."
        )

    elif "clear" in desc or "sun" in desc:
        if temp > 35:
            return (
                "📌 **Suggested Plan:**\n"
                "☀️ It's sunny and hot outside!\n"
                "• Avoid going out during peak afternoon hours.\n"
                "• Wear sunglasses and light cotton clothes.\n"
                "• Stay in shaded or cool areas.\n\n"
                "🩺 **Doctor's Precautions:**\n"
                "• Drink plenty of water and fresh juices.\n"
                "• Avoid dehydration and heat exposure.\n"
                "• Use sunscreen to protect your skin."
            )
        else:
            return (
                "📌 **Suggested Plan:**\n"
                "🌤️ Clear and pleasant weather.\n"
                "• Great time for outdoor plans or a walk.\n"
                "• Light and comfortable clothing is enough.\n"
                "• Enjoy the day and stay hydrated.\n\n"
                "🩺 **Doctor's Precautions:**\n"
                "• Maintain hydration by drinking water regularly.\n"
                "• Apply sunscreen to avoid sunburn.\n"
                "• If you have allergies, wear sunglasses to protect from dust and pollen."
            )

    elif "cloud" in desc:
        return (
            "📌 **Suggested Plan:**\n"
            "☁️ Cloudy skies today.\n"
            "• You might want to carry a light jacket.\n"
            "• Perfect for a calm outdoor stroll.\n\n"
            "🩺 **Doctor's Precautions:**\n"
            "• Keep your body warm to avoid mild cold.\n"
            "• Drink warm water if you feel chilly."
        )

    elif "snow" in desc:
        return (
            "📌 **Suggested Plan:**\n"
            "❄️ It's snowing outside!\n"
            "• Stay indoors if possible.\n"
            "• If you go out, wear warm clothes and boots.\n\n"
            "🩺 **Doctor's Precautions:**\n"
            "• Protect your skin from dryness.\n"
            "• Keep your head and ears covered.\n"
            "• Drink hot beverages to maintain body warmth."
        )

    elif humidity > 80:
        return (
            "📌 **Suggested Plan:**\n"
            "💧 High humidity today.\n"
            "• Avoid heavy outdoor work.\n"
            "• Stay in cool, ventilated areas.\n\n"
            "🩺 **Doctor's Precautions:**\n"
            "• Drink fluids with electrolytes.\n"
            "• Avoid spicy or oily foods.\n"
            "• Rest in shade to avoid fatigue."
        )

    else:
        return (
            "📌 **Suggested Plan:**\n"
            "🌈 The weather looks fine today!\n"
            "• Great time for outdoor activities.\n"
            "• Enjoy a walk or meet friends.\n\n"
            "🩺 **Doctor's Precautions:**\n"
            "• Maintain hydration.\n"
            "• Eat light, healthy meals.\n"
            "• Keep a balanced routine for good health."
        )



st.write("Enter your city name:")
city = st.text_input("City Name")

API_KEY = "2351bf4aed20a254d4ac522995ae8c61"  

if st.button("Get Weather"):
    if city.strip():
        city = city.strip()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        res = requests.get(url)
        data = res.json()

        

        if str(data.get("cod")) == "200":
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            desc = data["weather"][0]["description"]

            st.subheader(f"🌍 Weather in {city.title()}")
            st.write(f"**🌡️ Temperature:** {temp}°C")
            st.write(f"**💧 Humidity:** {humidity}%")
            st.write(f"**🌤️ Condition:** {desc.title()}")

            prediction = weather_prediction(temp, desc, humidity)
            st.info(prediction)
        else:
            st.error(f" City not found! (Details: {data.get('message', 'unknown error')})")
    else:
        st.warning("Please enter a city name.")
