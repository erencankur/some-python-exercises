import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense # type: ignore

# Excel'den veri oku
df = pd.read_excel('orders.xlsx')
df['date'] = pd.to_datetime(df['date'])
df['total_price'] = df['quantity'] * df['price']

# SQLite veritabanı bağlantısı
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id TEXT,
    product TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL,
    date TEXT,
    region TEXT,
    total_price REAL
)
''')

df.to_sql('orders', conn, if_exists='replace', index=False)

print("Veriler veritabanına yazıldı.")

# Veritabanından veri çek
df_sql = pd.read_sql_query("SELECT * FROM orders", conn)

# --- Görselleştirme 1: En çok sipariş edilen kategoriler
plt.figure(figsize=(8,6))
sns.countplot(data=df_sql, x='category', order=df_sql['category'].value_counts().index)
plt.title('En Çok Sipariş Edilen Kategoriler')
plt.xlabel('Kategori')
plt.ylabel('Sipariş Sayısı')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Görselleştirme 2: Bölgelere göre toplam satış
region_sales = df_sql.groupby('region')['total_price'].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
sns.barplot(x=region_sales.index, y=region_sales.values, palette='Blues_d')
plt.title('Bölgelere Göre Toplam Ciro')
plt.ylabel('Toplam Satış (₺)')
plt.xlabel('Bölge')
plt.show()

# --- TensorFlow Model: quantity & price → total_price
X = df_sql[['quantity', 'price']].values
y = df_sql['total_price'].values

model = Sequential()
model.add(Dense(10, input_dim=2, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, y, epochs=50, verbose=0)

sample = np.array([[2, 150]])
predicted = model.predict(sample)
print(f"[🤖] Tahmini toplam fiyat (2 adet 150₺ ürün): {predicted[0][0]:.2f} ₺")

# --- Görselleştirme 3: En çok satılan ürünler
top_products = df_sql.groupby('product')['quantity'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
plt.title('En Çok Satılan Ürünler (Adet)')
plt.xlabel('Toplam Adet')
plt.ylabel('Ürün')
plt.show()

conn.close()