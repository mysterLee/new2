import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

music_info = soup.select('table.list-wrap > tbody> tr')
rank = 0
for music in music_info:
    rank += 1
    title_el = music.select('a')
    artist_el = music.select('a.artist.ellipsis')

    title = title_el[2].text
    title = title.lstrip()

    point = artist_el[0].text

    print(rank, title, "/", point)