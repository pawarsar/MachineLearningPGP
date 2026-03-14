import pandas as pd
import numpy as np

# csv = pd.read_csv('StockData.csv')
# excel = pd.read_excel('StockData.xlsx')
# books = pd.read_csv('books.csv')

# books_df = pd.DataFrame(books)

# print(books_df.shape)
# print(books_df.describe(include='all'))
# object_columns = books_df.select_dtypes(include='object')
# num_object_columns = len(object_columns.columns)
# print(num_object_columns)
# print(books_df.columns)


# #  Count number of object-type columns
# num_object_columns = books_df.select_dtypes(include=['object']).shape[1]

# print("Number of object datatype columns:", num_object_columns)

# print(books_df[books_df['average_rating']>4])

# print(books_df[books_df['average_rating']>4 and books_df['ratings_count']<10])
# print(books_df[(books_df['average_rating']>4.5) & (books_df['ratings_count']<10)])

# print(books_df.groupby('language_code')['average_rating'].mean().loc['eng'])

# print(books_df.iloc[0:5,0:4])
# print(books_df.loc[[1,4],['language_code', 'num_pages', 'ratings_count']])

# print(books_df['num_pages'].median())
# print(books_df['num_pages'].max())
# print(books_df['num_pages'].mode())
# print(books_df['num_pages'].mean())

# print(books_df[books_df['year']==2010])

# print(books_df[(books_df['publisher'] == 'DAW') & (books_df['average_rating'] > 4)])

# print(books_df[(books_df['num_pages'] > 500) & (books_df['year'] > 2010)])

# print(books_df[books_df['author'] == 'Agatha Christie'])

# print(books_df[(books_df['language_code'] == 'spa') & (books_df['year'] > 2000)])

# print(np.random.randint(10,20,1000))

rating = pd.read_csv('ratings.csv')

rating_df = pd.DataFrame(rating)
print(rating.head())
rating.groupby(['user_id'] != 196)['rating'].mean()