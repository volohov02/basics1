В задании 20 проделана следующая работа:

1. Улучшена работа парсера. Разделены в разные классы методы отвечающие за получение данных от сайта и методы отвечающие за мапинг. С сайта получена одна (первая) страница вакансий Python developer, реализована возможность перехода по ссылке в каждую отдельную вакансию, и получение на этой странице требований к сотруднику в виде списка.
2. Поскольку цель данного занятия работа с Django, убран реализованный ранее механизм получения всех страниц с этой вакансией.
3. На Django реализованы модели со списком вакансий и со списком требуемых для скиллов для этих вакансий.
4. Реализовано заполнение этих таблиц списком вакансий и списком уникальных скиллов.
5. В колонке descriptions таблицы вакансий записан номер вакансии по порядку (ну не придумал другого описания), В колонке descriptions таблицы скиллов счетчик нахождения скиллов в списке вакансий.
6. Между таблицами вакансий и скиллов реализована связь много-много, без создания промежуточного класса. (Об этом, собственно и был вопрос на который мне не ответили)