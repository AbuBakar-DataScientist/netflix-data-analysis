import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("netflix_synthetic_dataset.csv")

print("First Five Rows for Understanding Data: \n" , df.head())

# print("Analysing whole data information: \n" , df.describe())
# print(df.info())


#clean data
df = df.dropna(subset=['type' , 'release_year' , 'rating' , 'country' , 'duration'])

type_count = df['type'].value_counts()
print(type_count)

plt.figure(figsize=(6,4))

plt.bar(type_count.index , type_count.values , color = ['blue' , 'orange'])
plt.title('Numebr of Movies VS TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
# plt.savefig('movies_vs_tvshows.png' , dpi = 300 , bbox_inches = 'tight')

rating_count = df['rating'].value_counts()
print(rating_count)

plt.figure(figsize=(6,4))

plt.pie(rating_count , labels=rating_count.index , autopct = '%1.1f%%')
plt.title('Percentage of Content Rating')
# plt.savefig('content_rating_pie.png' , dpi = 300 , bbox_inches = 'tight')

country_count = df['country'].value_counts().head(5)
print(country_count)

plt.figure(figsize=(6,4))

plt.bar(country_count.index , country_count.values , color = 'navy')
plt.title('Top 10 countries Number of shows')
plt.ylabel('country')
plt.tight_layout()
# plt.savefig('top10_countries.png' , dpi = 300 , bbox_inches = 'tight')
