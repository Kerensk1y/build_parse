#!/bin/bash

n=$(ls /config/ | wc -l)

# Проверяем, что директория найдена
if [ -n "$n" ]; then
    while true; do
        for i in $(seq 1 $n); do
	    echo $i
            # Запуск python скрипта в фоне и сохранение его PID
            python3 parser_cls.py &
            python_pid=$!

            # Ждем 250 секунд
            sleep 250

            # Проверяем, запущен ли еще процесс и если да, то убиваем его
            if kill -0 $python_pid > /dev/null 2>&1; then
                echo "Killing process with PID $python_pid"
                kill $python_pid
            else
                echo "Process python3 parser_cls.py is not running"
            fi

            # Копирование содержимого конфигурационного файла в settings.ini
            cat "/config/$i.txt" > "settings.ini"
        done
    done
else
    echo "Directory '/config' is empty!"
fi
