import command_system
import vk
import random

session = vk.Session()
api = vk.API(session, v=5.92)

def tinderStart():
    messages = ('Тебя уже заждались! Жми кнопку внизу, чтобы начать общаться!', 'Мне звонили из рая и сказали, что у них пропал самый красивый ангел. Это случайно не ты? Нажми на кнопку и срази всех наповал!', 'Твои родители случайно не пираты? Тогда откуда у них такое сокровище? Скорее жми на кнопку, чтобы начать знакомиться!', 'Крокодил Гена нашел Чебурашку с помощью объявления на стенде. Ты можешь пообщаться прямо сейчас, просто нажав кнопку! Дерзай!', 'Иван-царевич нашел свою невесту, пустив стрелу в случайном направлении. Попытай и ты свою удачу! Жми на кнопку, чтобы начать.')
    message = random.choice(messages)
    buttons = open("/home/jBloodless/mysite/tinderStartKey.json", "r", encoding="UTF-8").read()
    return message, '', buttons

tinderStart_command = command_system.Command()

tinderStart_command.keys = ['Тиндер']
tinderStart_command.description = 'тиндер, хех'
tinderStart_command.process = tinderStart