def file_gen():
    items = ["Асфальтоукладчик", "Каток дорожный", "Бульдозер", "Грейдер", "Экскаватор", "Погрузчик", "Автокран"]

    # Шаблон содержимого файла без строки "keys = "
    template = """[Avito]
    url = https://www.avito.ru/
    num_ads = 3
    freq = 1
    keys = {key}
    max_price = 100000
    min_price = 0
    geo = Москва
    """

    # Создание файлов
    for index, item in enumerate(items):
        filename = f"config_{index + 1}.ini"  # Даем каждому файлу уникальное имя
        with open(filename, 'w') as file:
            content = template.format(key=item)
            file.write(content)

        print(f"Файл {filename} успешно создан.")
