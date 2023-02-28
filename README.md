# python

## Создаём виртуальное окружение
```
python3 -m venv venv
```

Если видим ошибку:
Невозможно загрузить файл .../venv/Scripts/Activate.ps1, так как выполнение сценариев отключено в этой системе. Для получения дополнительных сведений см. about_Execution_Policies по адресу http://go.microsoft.com/fwlink/?LinkID=135170
то открываем терминал от админа.
Пишем и запускаем:
```
PS C:\WINDOWS\system32> Set-ExecutionPolicy RemoteSigned
```
На вопрос отвечаем: A (Да для всех)
Если всё хорошо, то промпт выглядит так:
```
(venv) PS C:\python\PhoneBookPy>
```
После этого скритп можно выполнить вручную
```
(venv) PS C:\python\venv\scripts> .\Activate
```
зайдя в папку 
После создания venv в истории консоли встретилась команда:
```
python.exe -m pip install -U autopep8
```
надо бы разобраться зачем она

В консоли пишем:
```
pip list
```
получаем
```
Package     Version
----------- -------
autopep8    2.0.1  
pip         22.3.1 
pycodestyle 2.10.0 
setuptools  65.5.0 
tomli       2.0.1  

[notice] A new release of pip available: 22.3.1 -> 23.0.1       
[notice] To update, run: python.exe -m pip install --upgrade pip
```
Обновляем pip (package installer for Python)
```
python.exe -m pip install --upgrade pip
```
# Допы 2-го семинара

https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=3&id_topic=35&id_problem=223

https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=5&id_topic=113&id_problem=695

https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=5&id_topic=114&id_problem=703

https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=5&id_topic=114&id_problem=702

Доп 5-го семинара

https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=5&id_topic=114&id_problem=704

