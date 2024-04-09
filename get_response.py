import time
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def check_and_delete_urls():
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT id, url FROM Avito")
    urls = cursor.fetchall()
    conn.close()
    for uid, url in urls:
        print(url)
        driver.get(url)
        if driver.title == 'Ошибка 404. Страница не найдена':
            print(f"Error with {url}: {driver.title}, deleting...")
            cursor.execute("DELETE FROM Avito WHERE id=?", (uid,))
            conn.commit()
        time.sleep(15)
    driver.close()

check_and_delete_urls()
