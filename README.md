
# Проект  TakeText

---------------------------------------------------------

## Description

Copies all text from a text file.


## Зависимости Requirements

![Python version](https://img.shields.io/badge/python-3.12%2B-blue?logo=python&logoColor=ffdd54)
> Требуется Python 3.12+

Установка зависимостей:
```sh
pip3 install -r requirements.txt
```
Используется
```pyperclip```


## Конфигурирование Configuration

`Take_text.py`

```python
# CONFIGURATION
ALLOWED_TYPES = ('.txt', '.md', '.svg', '.html', '.css', '.js', '.py', '.ini', '.cmd', '.bat')
```
``ALLOWED_TYPES`` : Extensions of allowed file types  


## Usage

### Запуск

```bash
python Take_text.py <file>
```
- аргумент `file` передаётся путь к текстовому файлу.


____

## License

![License](https://img.shields.io/badge/license-MIT-green)  

/*******************************************************
 * Copyright 2026 Vintets <programmer@vintets.ru> - All Rights Reserved
 * Written by Vintets <programmer@vintets.ru>, June 2026
*******************************************************/  
