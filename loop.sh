#!/bin/bash

# Проверяем, существует ли уже строка в crontab
if ! crontab -l | grep "0 0 * * 7 /home/kirill/Desktop/build_parse/cron.sh" > /dev/null; then
  # Если строки нет, добавляем ее в crontab
  (crontab -l 2>/dev/null; echo "0 0 * * 7 /home/kirill/Desktop/build_parse/cron.sh") | crontab -
fi

nohup python3 config/tgbot.py &

while true; do
    for file in $(ls -t config/*.ini); do
        # Запуск python скрипта в фоне и сохранение его PID
        echo $file
        nohup python3 parser_cls.py &
        python_pid=$!

        # Ждем 250 секунд
        sleep 430

        # Проверяем, запущен ли еще процесс и если да, то убиваем его
        if kill -0 $python_pid > /dev/null 2>&1; then
            echo "Killing process with PID $python_pid"
            kill $python_pid
        else
            echo "Process python3 parser_cls.py is not running"
        fi

        # Копирование содержимого конфигурационного файла в settings.ini
        cat "$file.ini" > "settings.ini"
    done
done
