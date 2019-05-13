import command_system
import vk

session = vk.Session()
api = vk.API(session, v=5.92)

def tinderGender():
    message = 'Сейчас мы тебе кого-нибудь подберем😉Ты только скажи, с кем тебя знакомить.'
    buttons = open("/home/jBloodless/mysite/tinderGender.json", "r", encoding="UTF-8").read()
    return message, '', buttons

tinderGender_command = command_system.Command()

tinderGender_command.keys = ['Хочу знакомиться!', 'Оставить', 'Искать новые знакомства!']
tinderGender_command.description = 'internal tinder message'
tinderGender_command.process = tinderGender