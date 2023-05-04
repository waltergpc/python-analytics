import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd
from plotnine import *


ff1.Cache.enable_cache("cache")

baku_r_2023 = ff1.get_session(2023, "Baku", "R")

baku_r_2023.load()

driver_1 = "PER"

laps_driver_1 = baku_r_2023.laps.pick_driver(driver_1)

telemetry = laps_driver_1.get_telemetry()

fastest_driver_1 = laps_driver_1.pick_fastest()

fastest_telemetry = fastest_driver_1.get_telemetry().add_distance()

telemetry_df = pd.DataFrame.from_dict(fastest_telemetry)

print(fastest_telemetry["DRS"])

print(telemetry_df.columns)

plt1 = ggplot(telemetry_df, aes(x="X", y="Y")) + geom_point()

ggsave(filename="plot1.png", plot=plt1)
