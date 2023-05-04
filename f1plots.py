import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd
from plotnine import *
from plotnine.animation import PlotnineAnimation


ff1.Cache.enable_cache("cache")

baku_r_2023 = ff1.get_session(2023, "Baku", "R")

baku_r_2023.load()

driver_1 = "PER"

laps_driver_1 = baku_r_2023.laps.pick_driver(driver_1)

telemetry = laps_driver_1.get_telemetry()

fastest_driver_1 = laps_driver_1.pick_fastest()

fastest_telemetry = fastest_driver_1.get_telemetry().add_distance()

telemetry_df = pd.DataFrame.from_dict(fastest_telemetry)

print(telemetry_df.columns)

plots = list()

for index, row in telemetry_df.iterrows():
    current_frame = pd.DataFrame(row)
    print(current_frame.axes)
    plots.append(current_frame.columns)

print(plots[0].columns)

plt1 = ggplot(telemetry_df, aes(x="X", y="Y")) + geom_point()
