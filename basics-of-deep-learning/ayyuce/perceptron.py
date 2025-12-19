import numpy as np

# Başlangıç Değerleri:
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

weights = np.random.rand(2)
bias = np.random.rand(1)
learning_rate = 0.1

# Threshold (Eşik Değer):
def activation_function(z):
    return 1 if z >= 0 else 0

# Eğitim:
epochs = 10
for epoch in range(epochs):
    print(f"Epoch {epoch+1}")
    are_all_errors_zero = 0

    for i in range(len(x)):

        z = np.dot(weights, x[i]) + bias
        y_pred = activation_function(z)
        
        error = y[i] - y_pred
        
        weights += learning_rate * error * x[i]
        bias += learning_rate * error
        
        print(f"Giriş: {x[i]}, Gerçek Çikiş: {y[i]}, Tahmin: {y_pred}, Hata: {error}")

        if error != 0:
            are_all_errors_zero += 1
    
    print(f"Ağirliklar: {weights}, Bias: {bias}")
    print("-" * 30)

    if are_all_errors_zero == 0:
        break

# Sonuç:
print("\nEğitim Tamamlandi!")
for i in range(len(x)):
    z = np.dot(weights, x[i]) + bias
    y_pred = activation_function(z)
    print(f"Giriş: {x[i]} -> Tahmin: {y_pred}")
    