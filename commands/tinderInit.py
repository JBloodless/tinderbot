import command_system
import vk

session = vk.Session()
api = vk.API(session, v=5.92)

def tinderInit():
    message = 'Обратить на себя внимание можно красивым лицом и метким словцом. Кинь нам свою фотку и расскажи немного о себе, а обо всем остальном я позабочусь.\nСначала отправь фотографию с описанием, через обычную кнопку с самолетиком. При этом клавиатура бота свернется - после отправки ее надо открыть и обязательно нажать Загрузить.  Ничего не перепутай!'
    buttons = open("/home/jBloodless/mysite/tinderInit.json", "r", encoding="UTF-8").read()
    return message, '', buttons

tinderInit_command = command_system.Command()

tinderInit_command.keys = ['Загрузить новые']
tinderInit_command.description = 'internal tinder message'
tinderInit_command.process = tinderInit