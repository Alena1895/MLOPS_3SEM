import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class EDA:
    def __init__(self, filename):
        self.__filename = filename
        self.__data = pd.read_csv(self.__filename)

    @property
    def data(self):
        return self.__data

    def missing_data(self):
        """Функция выводит пропущенные значения"""
        return self.__data.isnull().sum()

    def show_pairplot(self):
        """Функция строит диаграмму попарного распределения"""
        sns.pairplot(self.__data, diag_kind="kde", hue="Default")
        plt.show()

    def show_corr_matrix(self):
        """Функция строит и выводит матрицу корреляции"""
        corr_matrix = self.__data.corr()

        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Корреляционная матрица")
        plt.show()

    def show_class_distribution(self):
        """Функция строит и выводит распределение классов"""
        class_counts = self.__data["Default"].value_counts()
        print(class_counts)

        class_counts.plot(kind="bar", color=["skyblue", "salmon"])
        plt.title("Распределение классов Default")
        plt.xlabel("Класс")
        plt.ylabel("Количество")
        plt.xticks(ticks=[0, 1], labels=["Non-Default", "Default"], rotation=0)
        plt.show()
