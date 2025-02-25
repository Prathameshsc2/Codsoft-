# Importing necessary libraries
import numpy as np
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Define user-item matrix (ratings matrix)
data = {
    'Avatar: The Way of Water': [5, 4, 3, 0, 0],
    'Black Panther: Wakanda Forever': [3, 0, 5, 2, 1],
    'Spider-Man: No Way Home': [4, 5, 0, 1, 2],
    'The Batman': [0, 3, 0, 5, 4],
    'Doctor Strange in the Multiverse of Madness': [2, 0, 1, 4, 5],
    'Jurassic World: Dominion': [5, 2, 4, 1, 3],
    'Top Gun: Maverick': [4, 0, 5, 3, 2],
    'Thor: Love and Thunder': [3, 5, 2, 1, 0],
    'Minions: The Rise of Gru': [1, 4, 3, 5, 2],
    'The Flash': [4, 2, 5, 0, 1],
}

# Step 2: Create DataFrame (User-Item Matrix)
df = pd.DataFrame(data, index=['User1', 'User2', 'User3', 'User4', 'User5'])

# Step 3: Singular Value Decomposition (SVD) for Dimensionality Reduction
svd = TruncatedSVD(n_components=2)  # Using 2 components for simplicity
decomposed_matrix = svd.fit_transform(df)

# Step 4: Reconstruct the approximated user-item matrix
approx_matrix = np.dot(decomposed_matrix, svd.components_)

# Step 5: Create DataFrame for approximated matrix
approx_df = pd.DataFrame(approx_matrix, columns=df.columns, index=df.index)

# Step 6: Calculate similarity between items (movies) based on the approximated matrix
item_similarity = cosine_similarity(approx_df.T)

# Step 7: Convert similarity matrix to DataFrame for better understanding
item_similarity_df = pd.DataFrame(item_similarity, index=df.columns, columns=df.columns)

# Step 8: Display the Item Similarity Matrix (Improved)
print("Enhanced Item Similarity Matrix (Using SVD):\n", item_similarity_df)

# Step 9: Function to recommend movies based on a given movie
def recommend_movies_svd(movie_name, top_n=3):
    similar_scores = item_similarity_df[movie_name]
    similar_movies = similar_scores.sort_values(ascending=False)
    recommended_movies = similar_movies.drop(movie_name).head(top_n)
    return recommended_movies.index.tolist()

# Step 10: Example Usage - Recommend movies similar to 'Avatar: The Way of Water'
recommended_movies_svd = recommend_movies_svd('Avatar: The Way of Water', top_n=3)
print("\nRecommended Movies for 'Avatar: The Way of Water' (Using SVD):", recommended_movies_svd)
