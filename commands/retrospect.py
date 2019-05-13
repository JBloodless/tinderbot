import command_system
import vkapi
import vk
from settings import s_token

session = vk.Session()
api = vk.API(session, v=5.92)

def retrospect():
   # Получаем случайную картинку из паблика
   attachment = vkapi.get_random_old_picture()
   message = 'В прошлом году было как-то так. А как будет в этом - зависит от тебя!\n'+api.photos.getAlbums(owner_id = '-177456743', album_ids = '264789751', access_token=s_token)['items'][0]['title']
   buttons = open("/home/jBloodless/mysite/defaultKeys.json", "r", encoding="UTF-8").read()
   return message, attachment, buttons

retrospect_command = command_system.Command()

retrospect_command.keys = ['Как это было?']
retrospect_command.description = 'ретроспектива'
retrospect_command.process = retrospect