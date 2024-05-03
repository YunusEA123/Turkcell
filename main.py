import requests
from bs4 import BeautifulSoup

def find_song_title(lyrics):
    # Şarkı adını bulmak için bir sorgu oluştur
    query = lyrics.replace(' ', '+') + '+lyrics'

    # Google'da arama yap
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)

    # Sayfa içeriğini analiz et.
    soup = BeautifulSoup(response.text, 'html.parser')

    # İlk sonuçtan şarkı adını al
    song_title = soup.find('div', class_='BNeawe tAd8D AP7Wnd').get_text()

    return song_title

# Kullanıcıdan şarkı sözlerini al
lyrics = input("Şarkı sözleri: ")

# Şarkı adını bul
song_title = find_song_title(lyrics)
print("Şarkı Adı:", song_title)