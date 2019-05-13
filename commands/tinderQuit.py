
import command_system


def tinderQuit():
   message = 'Ну что, мой неугомонный друг, чем ты теперь хочешь заняться?'
   buttons = open("/home/jBloodless/mysite/defaultKeys.json", "r", encoding="UTF-8").read()
   return message, '', buttons

tinderQuit_command = command_system.Command()

tinderQuit_command.keys = ['В начало', 'Выйти', 'Respawn']
tinderQuit_command.description = 'tinder internal'
tinderQuit_command.process = tinderQuit