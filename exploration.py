import pandas as pd

df = pd.read_csv('/Users/kevinwon/Desktop/quant/data.csv')

print("Original dataset size: ", len(df))
print("Original number of stocks: ", len(set(df['PERMNO'])))

# feature_vectors_filtered = {permno: rets for permno, rets in feature_vectors.items() if len(rets) == 48}

# print(len(feature_vectors))
# print(len(feature_vectors_filtered))
# print(feature_vectors_filtered.keys())