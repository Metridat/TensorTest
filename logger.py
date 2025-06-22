import logging

# настройка логгера
logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)

# формат вывода
formatter = logging.Formatter('%(asctime)s — %(levelname)s — %(message)s')

# обработчик, который выводит логи в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# обработчик, который пишет логи в файл
file_handler = logging.FileHandler("test_log.log", encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# добавляем обработчики к логгеру
logger.addHandler(console_handler)
logger.addHandler(file_handler)
