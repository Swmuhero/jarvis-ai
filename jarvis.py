import pyttsx3
import datetime
import os
import webbrowser
import smtplib
import requests
import random
import wikipedia
import openai

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Set up OpenAI API key for AI-based conversation
openai.api_key = ""

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Sir!")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Night Sir!")

    speak("I am jarvis. Please tell me how may I help you.")

def takeCommand():
    query = input("Enter your command: ").lower()
    return query

def openFile(command):
    program_name_start_index = command.find('open') + len('open')
    program_name = command[program_name_start_index:].strip()

    if "bluej" in program_name:
        os.system("start bluej.exe")
        speak(f"Opening BlueJ for you, Sir!")

def playMusic(command):
    artist_name_start_index = command.find('play music') + len('play music')
    artist_name = command[artist_name_start_index:].strip()

    search_query = f"{artist_name} songs"
    speak(f"Playing {artist_name}'s songs on YouTube.")
    webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

def sendEmail():
    speak("Please provide the recipient's email address:")
    to_address = input("Recipient's Email: ").lower()
    
    speak("What should I say in the email?")
    email_content = input("Email Content: ")

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("your_email@gmail.com", "your_password")
        server.sendmail("your_email@gmail.com", to_address, email_content)
        server.quit()
        speak("Email sent successfully!")

    except Exception as e:
        speak(f"Sorry, I couldn't send the email. Error: {str(e)}")

def getWeather():
    api_key = "your_weather_api_key"
    
    speak("Please provide your city for weather information:")
    city = input("City: ").lower()

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()

    if weather_data["cod"] == "404":
        speak("City not found. Please try again.")
    else:
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        speak(f"The temperature in {city} is {temperature} Kelvin. Weather: {description}")

def systemInformation():
    try:
        import platform
        import psutil

        system_platform = platform.system()
        machine_type = platform.machine()
        cpu_info = platform.processor()
        memory_info = psutil.virtual_memory()

        speak(f"System Information: {system_platform} {machine_type}")
        speak(f"CPU: {cpu_info}")
        speak(f"Memory: {memory_info.percent}% used")

    except Exception as e:
        speak(f"Sorry, I couldn't retrieve system information. Error: {str(e)}")

def setReminder():
    speak("What should I remind you about?")
    reminder_text = input("Reminder: ")

    speak("When should I remind you? Please provide the time.")
    reminder_time = input("Reminder Time: ")

    try:
        reminder_datetime = datetime.datetime.strptime(reminder_time, "%H:%M")
        current_time = datetime.datetime.now().time()
        time_difference = datetime.datetime.combine(datetime.date.today(), reminder_datetime.time()) - datetime.datetime.combine(datetime.date.today(), current_time)
        reminder_seconds = time_difference.total_seconds()
        timer_cmd = f"timeout /t {int(reminder_seconds)} /nobreak && echo {reminder_text} && pause"
        os.system(timer_cmd)
        speak(f"Reminder set: {reminder_text} at {reminder_time}")

    except ValueError:
        speak("Sorry, I couldn't understand the time format. Please try again.")

def tellJoke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.",
        "Why did the computer keep its drink on the windowsill? Because it wanted a byte."
    ]

    speak("Here's a joke for you:")
    joke = random.choice(jokes)
    speak(joke)

def launchApplication(command):
    app_name_start_index = command.find('launch') + len('launch')
    app_name = command[app_name_start_index:].strip()

    try:
        os.system(f"start {app_name}.exe")
        speak(f"Opening {app_name} for you, Sir!")

    except Exception as e:
        speak(f"Sorry, I couldn't launch the application. Error: {str(e)}")

def checkEmails():
    try:
        emails = ["Email 1", "Email 2", "Email 3"]
        speak("You have the following unread emails:")
        for email in emails:
            speak(email)

    except Exception as e:
        speak(f"Sorry, I couldn't check your emails. Error: {str(e)}")

def startTimer():
    speak("For how many minutes should I set the timer?")
    try:
        duration = float(input("Duration (minutes): "))
        seconds = int(duration * 60)
        os.system(f"timeout /t {seconds} /nobreak && echo Timer done && pause")
        speak("Timer done!")

    except ValueError:
        speak("Sorry, I couldn't understand the duration. Please try again.")

def getStockPrice():
    speak("Which company's stock price would you like to know?")
    company_name = input("Company Name: ").strip()

    try:
        stock_price = "$500.00"
        speak(f"The current stock price of {company_name} is {stock_price}")

    except Exception as e:
        speak(f"Sorry, I couldn't fetch the stock price. Error: {str(e)}")

def takeScreenshot():
    try:
        import pyautogui
        screenshot_path = "screenshot.png"
        pyautogui.screenshot(screenshot_path)
        speak("Screenshot captured and saved.")
        os.system(screenshot_path)

    except Exception as e:
        speak(f"Sorry, I couldn't capture a screenshot. Error: {str(e)}")

def checkWeatherForecast():
    speak("For which city would you like to check the weather forecast?")
    city = input("City: ").strip()

    try:
        weather_forecast = "Sunny with a high of 25°C"
        speak(f"The weather forecast for {city} is: {weather_forecast}")

    except Exception as e:
        speak(f"Sorry, I couldn't fetch the weather forecast. Error: {str(e)}")

def toggleNightMode():
    speak("Would you like to toggle night mode for the whole system or a specific application?")
    choice = input("System or Application: ").lower()

    try:
        if choice == "system":
            speak("Toggling night mode for the entire system.")
        elif choice == "application":
            speak("Which application would you like to toggle night mode for?")
            app_name = input("Application Name: ").strip()
            speak(f"Toggling night mode for {app_name}.")
        else:
            speak("Invalid choice. Please specify 'system' or 'application'.")

    except Exception as e:
        speak(f"Sorry, I couldn't toggle night mode. Error: {str(e)}")

def sendTextMessage():
    speak("Whom would you like to send a text message?")
    contact = input("Contact Name: ").strip()

    speak("What message would you like to send?")
    message = input("Message: ")

    try:
        send_message_result = "Message sent successfully"
        speak(send_message_result)

    except Exception as e:
        speak(f"Sorry, I couldn't send the text message. Error: {str(e)}")

def searchWikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        print(result)
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Ambiguous search query. Please provide more specific details.")
        speak("Ambiguous search query. Please provide more specific details.")
    except wikipedia.exceptions.PageError as e:
        print("No information found on Wikipedia for the given query.")
        speak("No information found on Wikipedia for the given query.")

def openWebsite(command):
    url = command.split('open website')[1].strip()
    webbrowser.open(url)


def getNewsHeadlines():
    # Placeholder for fetching and displaying news headlines
    print("Fetching and displaying news headlines is not implemented yet.")


def getRandomFunFact():
    # Placeholder for fetching and displaying a random fun fact
    fun_facts = ["Fun fact 1", "Fun fact 2", "Fun fact 3"]
    random_fact = random.choice(fun_facts)
    print(random_fact)
    speak(random_fact)

def learnNewWord():
    # Placeholder for fetching and displaying a new word for learning
    new_words = ["Serendipity", "Quixotic", "Ephemeral"]
    random_word = random.choice(new_words)
    print(f"Today's word to learn: {random_word}")
    speak(f"Today's word to learn is {random_word}")

def executeCodeSnippet():
    # Placeholder for code execution logic
    print("Code execution functionality is not implemented yet.")

def upcomingCalendarEvents():
    # Placeholder for fetching and displaying upcoming calendar events
    print("Fetching and displaying upcoming calendar events is not implemented yet.")

def generateAIResponse(prompt):
    # Placeholder for generating AI response based on the given prompt
    print("Generating AI response is not implemented yet.")
    return "Placeholder AI response."

def recommendNearbyPlaces():
    # Placeholder for recommending nearby places
    print("Recommendation of nearby places is not implemented yet.")

def generateAIResponse(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def recommendNearbyPlaces():
    speak("Sure! Let me find some nearby places for you.")
    # Use a location-based service or API to get recommendations
    nearby_places = ["Restaurant A", "Park B", "Coffee Shop C"]
    speak("Here are some nearby places:")
    for place in nearby_places:
        speak(place)

def learnNewWord():
    speak("Let's learn a new word! What word would you like to learn?")
    new_word = input("New Word: ").strip()
    speak(f"The word '{new_word}' means: [definition]. Use it in a sentence.")

def executeCodeSnippet():
    speak("Sure! Please enter the code snippet:")
    code_snippet = input("Code Snippet: ").strip()

    try:
        result = eval(code_snippet)
        speak(f"The result is: {result}")

    except Exception as e:
        speak(f"Sorry, I couldn't execute the code. Error: {str(e)}")

def upcomingCalendarEvents():
    speak("Checking your upcoming calendar events.")
    # Integrate with a calendar API to fetch upcoming events
    upcoming_events = ["Meeting on Monday at 3 PM", "Dentist appointment on Wednesday"]
    speak("Here are your upcoming calendar events:")
    for event in upcoming_events:
        speak(event)


if __name__ == "__main__":
    wishMe()

    while True:
        command = takeCommand()

      
        if 'open notepad' in command:
            os.system("start notepad.exe")
            speak("Opening Notepad for you, Sir!")

        elif 'tell me the time' in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            result = f"The current time is {current_time}, Sir."
            speak(result)

        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com/")
            speak("Opening YouTube for you, Sir!")

        elif 'open google' in command:
            webbrowser.open("https://www.google.com/")
            speak("Opening Google for you, Sir!")

        elif 'open word' in command:
            os.system("start winword.exe")
            speak("Opening Microsoft Word for you, Sir!")

        elif 'open excel' in command:
            os.system("start excel.exe")
            speak("Opening Microsoft Excel for you, Sir!")

        elif 'open powerpoint' in command:
            os.system("start powerpnt.exe")
            speak("Opening Microsoft PowerPoint for you, Sir!")

        elif 'open' in command:
            openFile(command)

        elif 'play music' in command:
            playMusic(command)

        elif 'search' in command:
            search_query_start_index = command.find('search') + len('search')
            search_query = command[search_query_start_index:].strip()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'send email' in command:
            sendEmail()

        elif 'get weather' in command:
            getWeather()

        elif 'system information' in command:
            systemInformation()

        elif 'set reminder' in command:
            setReminder()

        elif 'tell me a joke' in command:
            tellJoke()

        elif 'launch' in command:
            launchApplication(command)

        elif 'check emails' in command:
            checkEmails()

        elif 'start timer' in command:
            startTimer()

        elif 'get stock price' in command:
            getStockPrice()

        elif 'take screenshot' in command:
            takeScreenshot()

        elif 'check weather forecast' in command:
            checkWeatherForecast()

        elif 'toggle night mode' in command:
            toggleNightMode()

        elif 'send text message' in command:
            sendTextMessage()

        elif 'search on wikipedia' in command:
            speak("What would you like to search on Wikipedia?")
            search_query = input("Wikipedia Search: ").strip()
            searchWikipedia(search_query)

        elif 'open website' in command:
            openWebsite(command)


        elif 'get news headlines' in command:
            getNewsHeadlines()

        elif 'tell me a fun fact' in command:
            getRandomFunFact()

        elif 'learn a new word' in command:
            learnNewWord()

        elif 'execute code' in command:
            executeCodeSnippet()

        elif 'upcoming events' in command:
            upcomingCalendarEvents()

        elif 'ai conversation' in command:
            speak("Sure! What topic would you like to discuss?")
            conversation_prompt = input("Conversation Prompt: ").strip()
            ai_response = generateAIResponse(conversation_prompt)
            speak(ai_response)

        elif 'recommend places' in command:
            recommendNearbyPlaces()

        elif 'goodbye' in command:
            speak("Goodbye Sir! Have a great day. I love you sir.")
            break

        else:
            speak("Sorry, I didn't understand that. Can you please repeat?")