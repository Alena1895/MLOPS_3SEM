В процессе выполнения задания произведен разведочный анализ данных (EDA) на датасете Credit Default,
а также создан CI/CD pipeline для автоматизации тестирования и развертывания.
EDA был проведен в Jypiter Notebook eda.ipynb, вспомогательный код размещен в файле eda.py.
Результаты EDA опубликованы на GitLab Pages.
В процессе выполнени CI/CD pipeline:

код проверяется на соответствие стандартам,
собирается и публикуется в GitLab Docker Registry образ проекта,
собирается и публикуется в GitLab PyPI Registry Python-пакет,
с помощью Quarto на основании файла eda.ipynb формируется и публикуется на GitLab Pages документация в формате HTML.
