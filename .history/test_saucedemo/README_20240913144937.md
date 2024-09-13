# E2E тестирование для saucedemo.com

## Предварительные условия
- Python 3.
- Google Chrome браузер

## Установка
1. Клонируйте репозиторий:
```
git clone https://github.com/your-username/test-saucedemo.git

```
2. Перейдите в директорию:
```
 cd test_saucedemo
```
3. Создайте виртуальное окружение:

```
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

```
 
4. Установите зависимости:
 
```
pip install -r requirements.txt
```

5. Запустите тестирование
```
python test_saucedemo.py

```