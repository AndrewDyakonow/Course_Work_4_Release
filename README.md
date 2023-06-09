# course_work_4_release

___
## Курсовой проект по ООП “Парсер вакансий”

___
## Задачи
### Закрепить первоначальные знания по темам:
1. Концепция ООП;
2. Классы и объекты;
3. Инкапсуляция, наследование и полиморфизм;
4. Параметр self и метод "\__init__";
5. Classmethod и staticmethod;
6. Декораторы;
7. Магические методы;
8. Множественное наследование;
9. Исключения
___
## Установка

1. Откройте проект с помощью Get from VCS.
2. Введите ссылку на удалённый репозиторий. 
    ```
    git@github.com:AndrewDyakonow/Course_Work_4_Release.git
   ```
3. Создайте и активируйте виртуальное окружение.
    ```
    python3 -m venv venv
    source venv/bin/activate
   ```
4. Установите зависимости.
    ```
    pip install -r requirements.txt
   ```
___

## Описание

1. При запуске файла main.py необходимо выбрать ресурс для парсинга(Head Hunter или Superjob), в противном случае ничего не получится
2. Потом требуется набрать ключевое слово или фразу для поиска и нажать ENTER
3. Если по ключевому слову или фразе вакансий не будет найдено, то выведется соответствующее сообщение
4. После получения вакансий, их можно отсортировать по зарплате, от большей к меньшей
