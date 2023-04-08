import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd


ff1.Cache.enable_cache("cache")

bahrain_r_2023 = ff1.get_session(2022, "Austria", "R")

bahrain_r_2023.load()

driver_1, driver_2 = "PER", "LEC"

laps_driver_1 = bahrain_r_2023.laps.pick_driver(driver_1)
laps_driver_2 = bahrain_r_2023.laps.pick_driver(driver_2)

fastest_driver_1 = laps_driver_1.pick_fastest()
fastest_driver_2 = laps_driver_2.pick_fastest()

telemetry_driver_1 = fastest_driver_1.get_telemetry().add_distance()
telemetry_driver_2 = fastest_driver_2.get_telemetry().add_distance()

team_driver_1 = fastest_driver_1["Team"]
team_driver_2 = fastest_driver_2["Team"]

delta_time, ref_tel, compare_tel = utils.delta_time(fastest_driver_1, fastest_driver_2)

plot_size = [15, 15]
plot_title = f"{bahrain_r_2023.event.year} {bahrain_r_2023.event.EventName} - {bahrain_r_2023.name} - {driver_1} VS {driver_2}"
plot_ratios = [1, 3, 2, 1, 1, 2, 1]
plot_filename = plot_title.replace(" ", "") + ".png"
