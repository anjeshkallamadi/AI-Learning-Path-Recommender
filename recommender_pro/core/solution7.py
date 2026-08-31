import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

print("Training and freezing model...")
train_df = pd.read_csv('train.csv')

tfidf = TfidfVectorizer(max_features=35000, stop_words='english', ngram_range=(1, 2), sublinear_tf=True)
train_matrix = tfidf.fit_transform(train_df['Reviews'])

# Save the Vectorizer, the Matrix, and the Train DataFrame for quick lookup
joblib.dump(tfidf, 'tfidf_vectorizer.pkl')
joblib.dump(train_matrix, 'train_matrix.pkl')
joblib.dump(train_df, 'train_data.pkl')

print("Model successfully saved!")