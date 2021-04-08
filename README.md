# Описание выполненных работ и проектов

## Базовые операции
 1. 

-Получите из [данных](https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv) фрейм

-По этому фрейму вычислите среднее значение вызовов пожарных машин в месяц в одном округе Москвы, округлив до целых

Решение:
**[Numpy,pandas](https://github.com/Armada000/Portfolio/blob/main/%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B5%20%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8/1Numpy%2Cpandas.py)**

2.

-Получите [данные по безработице в Москве](https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv)

-Объедините эти данные индексами с [данными вызовов пожарных](https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv)

-Найдите значение поля 'UnemployedMen' в том месяце, когда было меньше всего вызовов в Центральном административном округе

Решение:
**[Index,Frames](https://github.com/Armada000/Portfolio/blob/main/%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B5%20%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8/1Index%2CFrames.py)**

3.

-Получите данные по [безработице в Москве](https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv)

-Найдите, с какого года процент людей с ограниченными возможностями среди всех безработных стал меньше 2%

Решение:
**[Filter,labmda](https://github.com/Armada000/Portfolio/blob/main/%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B5%20%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8/1Filter%2Clabmda.py)**

4.

-Возьмите [данные по безработице в городе Москва](https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv)

-Сгруппируйте данные по годам

-Постройте модель линейной регрессии по годам среднего значения отношения UnemployedDisabled к UnemployedTotal за месяц

-Какое ожидается значение процента безработных инвалидов в 2020 году при сохранении текущей политики города Москвы,ответ округлите до сотых

Решение:
**[Regression](https://github.com/Armada000/Portfolio/blob/main/%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B5%20%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8/Regression.py)**

## Парсинг

5. 

-Получите ключ API в кабинете разработчика [API Геокодера Яндекса](https://yandex.ru/dev/maps/geocoder/doc/desc/concepts/input_params.html)

-Выполните запрос к API и узнайте долготу точки на карте для города Самара

Решение:
**[API,SOAP,Geocode](https://github.com/Armada000/Portfolio/blob/main/%D0%9F%D0%B0%D1%80%D1%81%D0%B8%D0%BD%D0%B3/API%2CSOAP%2CGeocode.py)**

6. 

-Получите [данные по котировкам акций](https://mfd.ru/marketdata/?id=5&group=16&mode=3&sortHeader=name&sortOrder=1&selectedDate=01.11.2019)

-Найдите, по какому тикеру был максимальный рост числа сделок (в процентах) за 1 ноября 2019 года

Решение:
**[Parsing](https://github.com/Armada000/Portfolio/blob/main/%D0%9F%D0%B0%D1%80%D1%81%D0%B8%D0%BD%D0%B3/Parsing.py)**

7. 

-Используя парсинг [данных](https://video.ittensive.com/data/018-python-advanced/beru.ru/) найдите, на сколько литров отличается общий объем холодильников Саратов 263 и Саратов 452

Решение:
**[Fridge_volume](https://github.com/Armada000/Portfolio/blob/main/%D0%9F%D0%B0%D1%80%D1%81%D0%B8%D0%BD%D0%B3/Fridge_volume.py)**

8. 

-Соберите [данные о моделях холодильников Саратов](https://video.ittensive.com/data/018-python-advanced/beru.ru/): URL, название, цена, размеры, общий объем, объем холодильной камеры

-Создайте соответствующие таблицы в SQLite базе данных и загрузите полученные данные в таблицу beru_goods

Решение:
**[ParsInSql](https://github.com/Armada000/Portfolio/blob/main/%D0%9F%D0%B0%D1%80%D1%81%D0%B8%D0%BD%D0%B3/ParsInSql.py)**

## Визуализация

9. 

-Загрузите [данные по ЕГЭ за последние годы](https://video.ittensive.com/python-advanced/data-9722-2019-10-14.utf.csv)

-Выберите данные за 2018-2019 учебный год

-Выберите тип диаграммы и постройте ее для районов Северо-Западного административного округа Москвы для количества школьников, написавших ЕГЭ на 220 баллов и выше

Решение:
**[VisualType](https://github.com/Armada000/Portfolio/blob/main/%D0%92%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F/VisualType.py)**

10. 

-Загрузите [данные по итогам марафона](https://video.ittensive.com/python-advanced/marathon-data.csv)

-Приведите время половины и полной дистанции к секундам

-Найдите, данные каких серии коррелируют

-Найдите коэффициент корреляции этих серий данных

-Постройте график jointplot для коррелирующих данных

Решение:
**[MarathonData](https://github.com/Armada000/Portfolio/blob/main/%D0%92%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F/MarathonData.py)**

11. 

-Используя [данные индекса РТС за последние годы](https://video.ittensive.com/python-advanced/rts-index.csv) постройте отдельные графики закрытия индекса по дням за 2017, 2018, 2019 годы в единой оси X

-Добавьте на график экспоненциальное среднее за 20 дней для значения 'Max' за 2017 год

-Найдите последнюю дату, когда экспоненциальное среднее максимального дневного значения 'Max' в 2017 году было больше, чем соответствующее значение 'Close' в 2019 году 

Решение:
**[VisualCandle](https://github.com/Armada000/Portfolio/blob/main/%D0%92%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F/VisualCandle.py)**

12. 

-Постройте фоновую картограмму по [количеству объектов в каждом регионе России](https://video.ittensive.com/python-advanced/data-44-structure-4.csv.gz), используя [гео-данные](https://video.ittensive.com/python-advanced/russia.json)

-Выведите для каждого региона количество объектов в нем

-Посчитайте число объектов культурного наследия в Татарстане

Решение:
**[GeoData](https://github.com/Armada000/Portfolio/blob/main/%D0%92%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F/GeoData.py)**

## Отчеты и автоматизация

13. 



14. g
15. gsag
16. s
17. as
18. g
