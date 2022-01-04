from estimatePrice import estimated_price
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def tmp_theta0(learning_rate, x, y, theta0, theta1):
    return (learning_rate * sum([estimated_price(theta0, theta1, xs) - ys for xs , ys in zip(x,y)])) / len(x)
    

def tmp_theta1(learning_rate, x,y ,theta0, theta1):
    return (learning_rate * sum([(estimated_price(theta0, theta1, xs) - ys) * xs for xs , ys in zip(x,y)])) / len(x)

def gradient_dessent(x, y , iterations, learning_rate):
    t0 , t1 = 0 , 0
    for _ in range(iterations):
        t0 = t0 - tmp_theta0(learning_rate, x, y, t0 , t1)
        t1 = t1 - tmp_theta1(learning_rate, x, y, t0 , t1)
    return t0, t1



def normalize(x):
    return (x - x.min()) / (x.max() - x.min())

data = pd.read_csv('./data.csv')
print(data.head())
x = data["km"]
y = data["price"]
x_normalized = normalize(x)
y_normalized = normalize(y)


learning_rate = 0.1
iterations = 5000
t0 , t1 = gradient_dessent(x_normalized, y_normalized, iterations, learning_rate)
y_pred = estimated_price(t0, t1, x_normalized)

predict = 176000
predict = (predict - x.min()) / (x.max() - x.min())
new_yPred = estimated_price(t0, t1, predict)
plt.scatter(predict, new_yPred, c='r')
plt.plot(x_normalized,y_pred, '--')
plt.scatter(x_normalized,y_normalized, s=100, c='g')
plt.show()