import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd


ff1.Cache.enable_cache("cache")

baku_r_2023 = ff1.get_session(2023, "Baku", "R")

baku_r_2023.load()

driver_1 = "PER"

laps_driver_1 = baku_r_2023.laps.pick_driver(driver_1)

print(laps_driver_1)

fastest_driver_1 = laps_driver_1.pick_fastest()

print(fastest_driver_1)


telemetry_driver_1 = fastest_driver_1.get_telemetry().add_distance()

team_driver_1 = fastest_driver_1["Team"]


# plot_size = [15, 15]
# plot_title = f"{bahrain_r_2023.event.year} {bahrain_r_2023.event.EventName} - {bahrain_r_2023.name} - {driver_1} VS {driver_2}"
# plot_ratios = [1, 3, 2, 1, 1, 2, 1]
# plot_filename = plot_title.replace(" ", "") + ".png"
