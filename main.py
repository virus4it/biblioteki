import requests
import pandas as pd
import matplotlib.pyplot as plt


url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
if response.status_code == 200:
    print("Успешно получили данные с сайта:")
    print(response.json()[:3])
else:
    print(f"Ошибка при запросе данных: {response.status_code}")


data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [24, 27, 22, 32],
    "Salary": [70000, 80000, 65000, 90000]
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)


print("\nСредний возраст:", df["Age"].mean())
print("Максимальная зарплата:", df["Salary"].max())


print("\nDataFrame с добавленным столбцом:")
df["Tax"] = df["Salary"] * 0.2
print(df)


ages = df["Age"]
salaries = df["Salary"]
plt.figure(figsize=(8, 5))
plt.bar(ages, salaries, color='blue', alpha=0.7)
plt.title("Зависимость зарплаты от возраста")
plt.xlabel("Возраст")
plt.ylabel("Зарплата")
plt.show()
