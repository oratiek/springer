import os
import requests
import csv
import pandas as pd

save_directory = "books"

path = "data.xlsx"
df = pd.read_excel(path)
for name, url in zip(df["Book Title"], df["DOI URL"]):
    url = "https://link.springer.com/content/pdf/" + url.strip("https://doi.org") + ".pdf"
    filename = "'{}/{}.pdf'".format(save_directory,name)
    command = "wget -O " + filename + " " + url
    print(command)
    os.system(command)


