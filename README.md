parser.py домогается к главной странице сайта garant-don.ru (так как именно на ней есть новости). Находит и выводит в консоль заголовки новостей и их количество, ссылки и их общее количество, количество относительных ссылок, количество абсолютных ссылок и нашел битую ссылку.
В lesson_16 этот же механизм парсера с помощью flask смонтирован в сайт (4 страницы), который позволяет выбрать тип информации - "новости" или "ссылки" из выпадающего меню и на странице "Результаты" посмотреть список новостей или ссылок и их количество. В случае если запрос с сайта не отправлялся, на странице "результаты" будет надпись "Нет данных"
В занятии 17 добавлена запись новостей и ссылок в заранее созданную базу данных SQLite, результат в той же папке lesson_16.
В lesson_18 находится домашнее задание занятия 18 - это тот же парсер + Flask, который записывает новости и ссылки в базу данных, предварительно ее создав. Файл query_data.py реализует обращение с условием к созданной базе данных.
