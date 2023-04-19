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

1. При запуске файла main.py происходит отрисовка формы
![alt text](https://github.com/AndrewDyakonow/Course_Work_4_Release/blob/main/image_for_readme/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202023-04-18%2018-27-26.png)
2. Далее необходимо выбрать ресурс для парсинга(Head Hunter или superjob), в противном случае ничего не получится
![alt text](https://github.com/AndrewDyakonow/Course_Work_4_Release/blob/main/image_for_readme/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202023-04-19%2013-30-31.png)
3. Потом требуется набрать ключевое слово или фразу для поиска и нажать кнопку "Запрос"
![alt text](https://github.com/AndrewDyakonow/Course_Work_4_Release/blob/main/image_for_readme/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202023-04-19%2013-32-29.png)
4. Если по ключевому слову или фразе вакансий не будет найдено, то выведется соответствующее сообщение
![alt text](https://github.com/AndrewDyakonow/Course_Work_4_Release/blob/main/image_for_readme/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202023-04-19%2013-34-11.png)
5. После получения вакансий, их можно отсортировать по зарплате, от большей к меньшей
![alt text](https://github.com/AndrewDyakonow/Course_Work_4_Release/blob/main/image_for_readme/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202023-04-19%2013-34-51.png)
