from google.oauth2 import service_account
from googleapiclient.discovery import build

# Загрузите учетные данные сервисного аккаунта из JSON-файла ключа
credentials = service_account.Credentials.from_service_account_file(
    'own_cred.json',
    scopes=['https://www.googleapis.com/auth/drive']
)

# Создайте экземпляр клиента Google Drive API
drive_service = build('drive', 'v3', credentials=credentials)

# Идентификатор файла .xlsx, для которого нужно настроить права доступа
file_id = '1_Ar3Fm0IcDe0YPBbCURP27uSV1xIfziMa2fxDmJ7edU'

# Настройка прав доступа для файла
body = {
    'role': 'writer',  # Роль пользователя (например, writer, reader)
    'type': 'user',    # Тип пользователя (например, user, group, domain)
    'emailAddress': 'keyslash123@gmail.com'  # Адрес электронной почты пользователя
}

# Создание нового правила доступа
permission = drive_service.permissions().create(fileId=file_id, body=body).execute()

# Проверка успешности создания правила доступа
if permission:
    print("Права доступа успешно настроены.")
else:
    print("Не удалось настроить права доступа.")