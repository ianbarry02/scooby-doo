import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Read CSV files
df = pd.read_csv('Scooby_doo_intro_median_hue_per_frame.csv')
df['num'] = np.arange(len(df))

### Plot data
df.plot(x="num", y=["1969_s1_intro_hue", "1970_s2_intro_hue", "1972_new_movies_s1_intro", "1976_scooby_doo_show_intro_hue", 
"1977_laff_a_lympics_intro_hue", "1979_scooby_and_scrappy_intro_hue", "1980_richie_rich_scooby_doo_hue", "1983_new_scooby_scrappy_intro_hue",
"1985_13_ghosts_scooby_doo_hue", "1985_scary_scooby_funnies_intro_hue", "1988_a_pup_scooby_doo_intro_hue", "2002_whats_new_intro_hue",
"2006_shaggy_scooby_get_clue_intro_hue", "2010_scooby_doo_mystery_inc_intro_hue", "2015_be_cool_scooby_doo_intro_hue", "2019_scooby_doo_guess_who_intro_hue"],
label = ["1969", "1970", "1972", "1976", "1977", "1979", "1980", "1983", "1985 (1)", "1985 (2)", "1988", "2002", "2006", "2010", "2015", "2019"],
        kind="line", figsize=(10, 10))
plt.title("Scooby Doo - Median Hue in Intro Sequences")
plt.xlabel("Frame Number")
plt.ylabel("Median Hue")
plt.legend()
plt.show()
