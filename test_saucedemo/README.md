# E2E тестирование для saucedemo.com


- Python 3.X
- Google Chrome браузер

1. Клонируйте репозиторий:
```
git clone https://git@github.com:DoraLoginova/test_tasks.git

```
2. Перейдите в директорию:
```
 cd test_saucedemo
```
3. Создайте виртуальное окружение:

```
python3 -m venv venv
source venv/bin/activate  

```
 
4. Установите зависимости:
 
```
pip install -r requirements.txt
```

5. Запустите тестирование
```
python test_saucedemo.py

```