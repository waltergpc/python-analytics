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

max_x_value = telemetry_df["X"].max()
min_x_value = telemetry_df["X"].min()
max_y_value = telemetry_df["Y"].max()
min_y_value = telemetry_df["Y"].min()


plots = list()

for index, row in telemetry_df.iterrows():
    test_data = row.to_frame()
    data_from_s = {
        "Speed": [row["Speed"]],
        "nGear": [row["nGear"]],
        "Throttle": [row["Throttle"]],
        "Brake": [row["Brake"]],
        "DRS": [row["DRS"]],
        "X": [row["X"]],
        "Y": [row["Y"]],
        "Z": [row["Z"]],
    }

    new_frame = pd.DataFrame(data=data_from_s)

    current_plot = (
        ggplot(new_frame, aes(x="X", y="Y"))
        + geom_point()
        + xlim(min_x_value, max_x_value)
        + ylim(min_y_value, max_y_value)
    )
    plots.append(current_plot)


plt1 = ggplot(telemetry_df, aes(x="X", y="Y")) + geom_point()
ggsave(filename="track.png", plot=plt1)
plots_anim = PlotnineAnimation(plots, interval=0.0001, repeat=500)
plots_anim.save("animation.gif")
