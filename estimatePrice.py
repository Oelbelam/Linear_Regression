import numpy as np
import os
import csv
import pandas as pd 

def read_theta_values (file_name):
    t0 , t1 = 0 , 0
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r') as csvfile:
        file_csv = csv.reader(csvfile, delimiter=',')
        for row in file_csv:
            t0 = float(row[0])
            t1 = float(row[1])
    return t0 , t1


def estimated_price(theta0, theta1, mileage):
    return (theta1* mileage) + theta0

if __name__ == "__main__":
    theta0 , theta1 = read_theta_values('thetas.csv')
    mileage = float(input("Enter mileage : "))
    price_pred= estimated_price(theta0, theta1, mileage)
    print(price_pred)
