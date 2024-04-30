import gspread
from oauth2client.service_account import ServiceAccountCredentials

def authenticate_service_account(credentials_file):
    """
    Аутентификация сервисного аккаунта и получение клиента для работы с Google Sheets API.
    Параметры:
    - credentials_file: путь к файлу с учетными данными сервисного аккаунта
    Возвращает объект клиента.
    """
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(credentials)
    return client

def open_sheet(client, file_id, sheet_name=None):
    """
    Открытие Google Sheets файла по его идентификатору и получение листа по его имени.
    Параметры:
    - client: объект клиента Google Sheets API
    - file_id: идентификатор файла на Google Диске
    - sheet_name (опционально): имя листа, если не указано, будет открыт первый лист
    Возвращает объект листа.
    """
    spreadsheet = client.open_by_key(file_id)
    if sheet_name:
        sheet = spreadsheet.worksheet(sheet_name)
    else:
        sheet = spreadsheet.sheet1
    return sheet

def append_data_to_sheet(sheet, data):
    """
    Добавление данных в конец Google Sheets файла.
    Параметры:
    - sheet: объект листа Google Sheets
    - data: список с данными для добавления
    """
    sheet.append_row(data)

# Пример использования
def main(new_data, objName):
    # Аутентификация сервисного аккаунта и получение клиента'
    credentials_file = 'own_cred.json'
    client = authenticate_service_account(credentials_file)

    # Идентификатор файла Google Sheets на Google Диске
    file_id = '1_Ar3Fm0IcDe0YPBbCURP27uSV1xIfziMa2fxDmJ7edU'

    # Открытие файла и получение листа
    sheet = open_sheet(client, file_id, sheet_name=objName)

    # Добавление данных в конец файла
    append_data_to_sheet(sheet, new_data)

    print("Данные успешно добавлены в Google Sheets файл.")