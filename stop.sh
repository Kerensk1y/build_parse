#!/bin/bash

# Поиск директории parser_avito и её сохранение в переменную directory
directory=$(find ~/ -type d -name "build_parse" | head -n 1 | tr -d '\n')

# Получение PID процессов
scr_pid=$(ps aux | grep "/bin/bash ./loop.sh"| grep -v grep| awk '{print $2}')
g_pid=$(ps aux | grep "/google/chrome/chrome" | grep -v 'grep' | awk '{print $2}')
py_pid=$(ps aux | grep "python3 $directory/parser_cls.py" | grep -v 'grep' | awk '{print $2}')
sel_pid=$(ps aux | grep "/selenium" | grep -v 'grep' | awk '{print $2}')
sleep_pid=$(ps aux | grep "sleep" | grep -v 'grep' | awk '{print $2}')

# Остановка процессов
if [ -n "$scr_pid" ]; then
    kill $scr_pid
else
    echo "Process /bin/bash ./loop.sh is not running"
fi

if [ -n "$sleep_pid" ]; then
    kill $sleep_pid
else
    echo "Process sleep 250 is not running"
fi

if [ -n "$sel_pid" ]; then
    kill $sel_pid
else
    echo "Process /selenium/chromedriver/ is not running"
fi

if [ -n "$py_pid" ]; then
    kill $py_pid
else
    echo "Process python3 /home/kirill/Desktop/build_parse/parser_cls.py is not running"
fi

if [ -n "$g_pid" ]; then
    kill $g_pid
else
    echo "Process /opt/google/chrome/chrome is not running"
fi
