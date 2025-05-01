import requests
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_news():
    api_key = "YOUR_API_KEY"  # <-- Replace this with your actual NewsAPI key
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"

    response = requests.get(url)
    news_data = response.json()

    articles = news_data["articles"]
    print("\n📰 Today's Top Headlines:\n")

    for i, article in enumerate(articles[:5], 1):  # Get top 5 headlines
        title = article["title"]
        print(f"{i}. {title}")
        speak(title)

if __name__ == "__main__":
    get_news()
