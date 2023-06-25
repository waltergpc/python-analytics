import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


base_url = "https://www.cbssports.com/mlb/schedule/"

add_on = "20230626/"

response = requests.get(base_url + add_on)

soup_mlb_schedule = bs(response.content, "html.parser")

tbody = soup_mlb_schedule.select(".TableBase-table > tbody")

tbody_list = tbody[0].select(".TableBase-bodyTr")


def construct_team_name_selector(team_cell_number: int):
    return f"td:nth-child({team_cell_number}) > span > div > .TeamLogoNameLockup-nameContainer > .TeamLogoNameLockup-name > span"


def construct_starting_pitcher_selector(starting_pitcher_cell: int):
    return f"td:nth-child({starting_pitcher_cell}) > .CellPlayerName--long > span"


for game in tbody_list:
    away_team_cell = 1
    home_team_cell = 2
    home_starting_pitcher_cell = 5
    away_starting_pitcher_cell = 6
    away_team = game.select(construct_team_name_selector(away_team_cell))
    home_team = game.select(construct_team_name_selector(home_team_cell))
    away_team = away_team[0].a.string
    home_team = home_team[0].a.string
    current_game = away_team + " vs " + home_team
    home_starting_pitcher_info = game.select(
        construct_starting_pitcher_selector(home_starting_pitcher_cell)
    )
    home_starting_pitcher = home_starting_pitcher_info[0].a.string
    home_starting_pitcher_era = (
        home_starting_pitcher_info[0]
        .span.string.strip()
        .replace("(", "")
        .replace(")", "")
        .split(", ")[1][0:4]
    )
    away_starting_pitcher_info = game.select(
        construct_starting_pitcher_selector(away_starting_pitcher_cell)
    )
    away_starting_pitcher = away_starting_pitcher_info[0].a.string
    away_starting_pitcher_era = (
        away_starting_pitcher_info[0]
        .span.string.strip()
        .replace("(", "")
        .replace(")", "")
        .split(", ")[1][0:4]
    )
    print(home_starting_pitcher + ", ERA " + home_starting_pitcher_era)
    print(away_starting_pitcher + ", ERA " + away_starting_pitcher_era)
