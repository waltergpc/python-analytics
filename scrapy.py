import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


base_url = "https://www.nfl.com/"
add_on = "stats/player-stats/category/passing/2022/post/all/passingyards/desc"

response = requests.get(base_url + add_on)

soup_player_stats = bs(response.content, "html.parser")

tbody_list = soup_player_stats.select(
    "#main-content > section:nth-child(4) > div > div > div > div > table > tbody"
)

tr_list = tbody_list[0].select("tr")

for players in tr_list:
    td_lst = players.select("td")
    player_params = td_lst[0].a["href"]
    temp_player_stats = requests.get(base_url + player_params)
    temp_soup_stats = bs(temp_player_stats.text, "html.parser")
    print(temp_soup_stats.select(".nfl-c-player-info__physical-data"))

    print(
        players.select("td")[0].a.string,
        list(
            map(
                lambda x: x.string,
                temp_soup_stats.select(
                    "#main-content > section:nth-child(5) > div > div.d3-l-col__col-8 > section > div > div > div > section > div > div.d3-l-col__col-12.nfl-c-player-info__content"
                ),
            )
        ),
    )
