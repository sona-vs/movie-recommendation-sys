"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# ---- 2. Load the dataset ----
df = pd.read_csv("netflix_titles.csv")
 
# ---- 3. Explore the data ----
print(df.head())          # first 5 rows
print(df.info())          # column types + missing value counts
 
# ---- 4. Check missing values ----
print(df.isnull().sum())
 
# ---- 5. Fill missing values ----
df['director'] = df['director'].fillna('Not Given')   # fixed: avoids inplace warning
df['cast'] = df['cast'].fillna('Not Given')
df['country'] = df['country'].fillna('Unknown')
 
# ---- 6. Confirm missing values are handled ----
print(df.isnull().sum())
 
# ---- 7. Movies vs TV Shows: count ----
print(df['type'].value_counts())
 
# ---- 8. Movies vs TV Shows: bar chart ----
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows on Netflix")
plt.show()
 
# ---- 9. Content released over the years: line chart ----
df['release_year'].value_counts().sort_index().plot(kind='line')
plt.title("Netflix Content Released Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()
 
# ---- 10. Top 10 content-producing countries ----
top_countries = df['country'].value_counts().head(10)
print(top_countries)
 
top_countries.plot(kind='bar')
plt.title("Top 10 Content Producing Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.show()
 
# ---- 11. Split multi-genre column into separate columns ----
genres = df['listed_in'].str.split(', ', expand=True)
 
# ---- 12. Top 10 genres ----
genre_count = genres.stack().value_counts().head(10)
print(genre_count)
 
genre_count.plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()
 
# ---- 13. Ratings distribution ----
sns.countplot(
    y='rating',
    data=df,
    order=df['rating'].value_counts().index
)
plt.title("Netflix Ratings Distribution")
plt.show()
 
# ---- 14. Check duration column format ----
print(df['duration'].head())
 
# ---- 15. Top 5 actors ----
actors = df['cast'].str.split(', ').explode()          # one actor per row
actors = actors[actors != 'No cast specified']          # remove placeholder values
top5Actors = actors.value_counts().head(5).reset_index()
top5Actors.columns = ['Actor', 'Total Count']
 
sns.barplot(data=top5Actors, x='Total Count', y='Actor')
plt.title('Top 5 Actors on Netflix')
plt.show()
 
# ---- 16. Movies vs TV Shows trend by year ----
df1 = df[['type', 'release_year']]
df1 = df1.rename(columns={"release_year": "Release Year", "type": "Type"})
 
# group by year + type, count how many titles in each group
df2 = df1.groupby(['Release Year', 'Type']).size().reset_index(name='Total Count')
print(df2)
 
# ---- 17. Plot trend (Movies vs TV Shows) after year 2000 ----
df2_filtered = df2[df2['Release Year'] >= 2000]
movies = df2_filtered[df2_filtered['Type'] == 'Movie']
tvshows = df2_filtered[df2_filtered['Type'] == 'TV Show']
 
plt.plot(movies['Release Year'], movies['Total Count'], label='Movie')
plt.plot(tvshows['Release Year'], tvshows['Total Count'], label='TV Show')
plt.title('Trend of Content Produced on Netflix')
plt.xlabel('Release Year')
plt.ylabel('Total Count')
plt.legend()
plt.show()"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Fill missing values
df['director'] = df['director'].fillna('Not Given')
df['cast'] = df['cast'].fillna('Not Given')
df['country'] = df['country'].fillna('Unknown')

# Create a 3x2 grid
fig, axes = plt.subplots(3, 2, figsize=(22, 18), constrained_layout=True)

# ------------------- Graph 1 -------------------
sns.countplot(x='type', data=df, ax=axes[0,0])
axes[0,0].set_title("Movies vs TV Shows")

# ------------------- Graph 2 -------------------
df['release_year'].value_counts().sort_index().plot(
    kind='line',
    ax=axes[0,1]
)
axes[0,1].set_title("Content Released Over Years")
axes[0,1].set_xlabel("Year")
axes[0,1].set_ylabel("Titles")

# ------------------- Graph 3 -------------------
top_countries = df['country'].value_counts().head(10)
top_countries.plot(kind='bar', ax=axes[1,0])
axes[1,0].set_title("Top 10 Countries")
axes[1,0].tick_params(axis='x', rotation=45)

# ------------------- Graph 4 -------------------
genres = df['listed_in'].str.split(', ', expand=True)
genre_count = genres.stack().value_counts().head(10)
genre_count.plot(kind='bar', ax=axes[1,1])
axes[1,1].set_title("Top 10 Genres")
axes[1,1].tick_params(axis='x', rotation=45)

# ------------------- Graph 5 -------------------
sns.countplot(
    y='rating',
    data=df,
    order=df['rating'].value_counts().index,
    ax=axes[2,0]
)
axes[2,0].set_title("Ratings Distribution")

# ------------------- Graph 6 -------------------
actors = df['cast'].str.split(', ').explode()
actors = actors[actors != 'Not Given']
top5Actors = actors.value_counts().head(5).reset_index()
top5Actors.columns = ['Actor', 'Total Count']

sns.barplot(
    data=top5Actors,
    x='Total Count',
    y='Actor',
    ax=axes[2,1]
)
axes[2,1].set_title("Top 5 Actors", pad=15)
plt.show()