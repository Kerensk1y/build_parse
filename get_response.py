import time
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def check_and_delete_urls():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

    cursor.execute("SELECT id, url FROM Avito")
    urls = cursor.fetchall()

    for uid, url in urls:
        print(url)
        driver.get(url)
        if driver.title == 'Ошибка 404. Страница не найдена':
            print(f"Error with {url}: {driver.title}, deleting...")
            cursor.execute("DELETE FROM Avito WHERE id=?", (uid,))
            conn.commit()
        time.sleep(30)
    conn.close()
    driver.close()

check_and_delete_urls()
