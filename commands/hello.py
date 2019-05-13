
import command_system


def hello():
   message = 'Привет! Ты на Днях Физика, а это значит, что тебя ждёт нечто легендарное ☺ Я помогу тебе разобраться в происходящем и завести новых друзей. Жми на кнопки внизу!\nЯ клёвый, но немного ранимый. Поэтому со мной лучше общаться так:\n1. Не нажимай на одну и ту же кнопку несколько раз. Мне от этого больно. Потерпи немного и дай мне подумать.\n2. Чтобы начать со мной общаться, просто напиши "привет".'
   buttons = open("/home/jBloodless/mysite/defaultKeys.json", "r", encoding="UTF-8").read()
   return message, '', buttons

hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'привет!', 'хелоу', 'здравствуйте', 'дратути', 'дратути!', 'дороу', 'дороу!', 'Начать', 'Start']
hello_command.description = 'Поприветствую тебя'
hello_command.process = hello
