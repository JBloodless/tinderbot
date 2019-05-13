import command_system


def info():
    message = 'Ребята, не стоит вскрывать эту команду. Вы молодые, шутливые, вам все легко. Это не то. Это не Сберкот и даже не бот из анимешного паблика. Сюда лучше не лезть. Серьезно, любой из вас будет жалеть. Лучше выйди на главную и забудь, что тут писалось. Я вполне понимаю, что данным сообщением вызову дополнительный интерес, но хочу сразу предостеречь пытливых - стоп. Остальные просто не найдут. Но раз ты такой умный, то вот тебе список команд.\n\n'
    for c in command_system.command_list:
        message += c.keys[0] + ' - ' + c.description + '\n'
    buttons = open("/home/jBloodless/mysite/tinderHelp.json", "r", encoding="UTF-8").read()
    attachment = 'photo-177456743_456239045'
    return message, attachment, buttons


info_command = command_system.Command()

info_command.keys = ['/help']
info_command.description = 'Покажу список команд'
info_command.process = info