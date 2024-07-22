#  Mindox задание.

## Описание проекта<a name="description"></a>
Структура репозитория:

**1. Папка geometry с заданием 1.**

**2. Папка tests c тестами для задания 1.**

**3. Папка pyspark с заданием 2.**


### Системные требования:<a name="stack"></a>

- Python 3.10
- Java 22

### Запуск скриптов <a name="local-install"></a>

1. **Копируем репозиторий:**

   ```bash
   git clone https://github.com/VitaliyDrozdov/Mbox_task

2. **Создаем и активируем виртуальное окружение:**

* Для Linux/macOS

    ```
    python3 -m venv env
    source env/bin/activate
    python3 -m pip install --upgrade pip
    ```

* Для windows

    ```
    python -m venv venv
    source venv/scripts/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```


3. **Подготавливаем переменные окружения к работе:**

*Редактируем*  .env файл и устанавливаем свои значения.

*Запускаем тесты ```python run_tests.py```*

*В папке pyspark запускаем ```python task_2.py```*

*Также в папке pyspark создан Jupyter файл: ```task_2.ipynb```*