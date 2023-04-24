from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors'
responde = requests.get(URL)

soup = BeautifulSoup(responde.text, 'html.parser')

titles = soup.title


page_datas = soup.find_all(class_="data-table__value")

datas = []
data = []
i = 0
for page_data in page_datas:
    if i == 6:
        datas.append(data)
        i = 0
        data = []
        data.append(page_data.text)
        i += 1
    else:
        data.append(page_data.text)
        i += 1

rank = []
major = []
degree = []
early_career_pay = []
mid_career_pay = []
high_meaning = []

for data in datas:
    rank.append(data[0])
    major.append(data[1])
    degree.append(data[2])
    early_career_pay.append(data[3])
    mid_career_pay.append(data[4])
    high_meaning.append(data[5])


data = {'Rank': rank,
        'Major': major,
        'Degree Type': degree,
        'Early Career Pay': early_career_pay,
        'Mid-Career Pay': mid_career_pay,
        '% High Meaning': high_meaning}

df = pd.DataFrame(data)
print(df)
df.to_csv("file1.csv")

