import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

age = np.random.randint(10000, 25000, n)
gender = np.random.choice([1, 2], n)
height = np.random.normal(165, 8, n).astype(int)
weight = np.random.normal(70, 15, n)
ap_hi = np.random.normal(120, 15, n).astype(int)
ap_lo = np.random.normal(80, 10, n).astype(int)

for i in range(10):
    idx = np.random.randint(0, n)
    ap_hi[idx], ap_lo[idx] = ap_lo[idx], ap_hi[idx] + 10

height[0:5] = 50
height[5:10] = 220
weight[10:15] = 30.0
weight[15:20] = 180.0

cholesterol = np.random.choice([1, 2, 3], n, p=[0.7, 0.2, 0.1])
gluc = np.random.choice([1, 2, 3], n, p=[0.8, 0.15, 0.05])
smoke = np.random.choice([0, 1], n, p=[0.9, 0.1])
alco = np.random.choice([0, 1], n, p=[0.95, 0.05])
active = np.random.choice([0, 1], n, p=[0.3, 0.7])

cardio_prob = 0.1 + (age / 100000) + (weight / 500) + (ap_hi / 500)
cardio_prob = np.clip(cardio_prob, 0, 1)
cardio = np.random.binomial(1, cardio_prob)

df = pd.DataFrame({
    'id': range(n),
    'age': age,
    'gender': gender,
    'height': height,
    'weight': weight,
    'ap_hi': ap_hi,
    'ap_lo': ap_lo,
    'cholesterol': cholesterol,
    'gluc': gluc,
    'smoke': smoke,
    'alco': alco,
    'active': active,
    'cardio': cardio
})

df.to_csv('medical_examination.csv', index=False)
print("Successfully created medical_examination.csv with 500 randomized rows!")