import command_system
import vk

session = vk.Session()
api = vk.API(session, v=5.92)

def schedule():
   # Получаем пост с расписанием
   group_id = '-177456743'
   photo_id = '456239077'
   #photo_id = api.photos.get(owner_id=group_id, album_id='wall', photo_ids=456239017, access_token=s_token)['attachments']['photo']['id']
   attachment = 'photo' + str(group_id) + '_' + str(photo_id)
   message = 'Лови расписание!'
   buttons = open("/home/jBloodless/mysite/defaultKeys.json", "r", encoding="UTF-8").read()
   return message, attachment, buttons

schedule_command = command_system.Command()

schedule_command.keys = ['Хочу расписание!']
schedule_command.description = 'Пришлю расписание'
schedule_command.process = schedule