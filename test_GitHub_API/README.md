# GitHub API

1. Клонируйте репозиторий:
```
git clone https://git@github.com:DoraLoginova/test_tasks.git

```
2. Перейдите в директорию:
```
 cd test_GitHub_API
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
5. Необходимо настроить переменные окружения, примера указаны в файле .env.example

Создание токена для работы с GitHub:  

   В правом верхнем углу любой страницы щелкните фотографию своего профиля, затем нажмите Settings (Настройки).
   На левой боковой панели нажмите Developer settings (Настройки разработчика).
   На левой боковой панели щелкните Personal access tokens (Личные токены доступа).
   Щелкните Generate new token (Создать новый токен).

6. Запустите тестирование
```
python test_api.py

```