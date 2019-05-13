import vkapi
import os
import importlib
from command_system import command_list
import vk
from settings import s_token
import random

session = vk.Session()
api = vk.API(session, v=5.92)


def damerau_levenshtein_distance(s1, s2):
   d = {}
   lenstr1 = len(s1)
   lenstr2 = len(s2)
   for i in range(-1, lenstr1 + 1):
       d[(i, -1)] = i + 1
   for j in range(-1, lenstr2 + 1):
       d[(-1, j)] = j + 1
   for i in range(lenstr1):
       for j in range(lenstr2):
           if s1[i] == s2[j]:
               cost = 0
           else:
               cost = 1
           d[(i, j)] = min(
               d[(i - 1, j)] + 1,  # deletion
               d[(i, j - 1)] + 1,  # insertion
               d[(i - 1, j - 1)] + cost,  # substitution
           )
           if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
               d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition
   return d[lenstr1 - 1, lenstr2 - 1]


def load_modules():
   files = os.listdir("mysite/commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])


def get_answer(extract_id, body):

   distance = len(body)
   command = None
   key = ''
   for c in command_list:
       for k in c.keys:
           d = damerau_levenshtein_distance(body, k)
           if d < distance:
               distance = d
               command = c
               key = k
               if distance == 0:
                   message, attachment, buttons = c.process()
                   return message, attachment, buttons
   if distance < len(body)*0.4:
       message, attachment, buttons = command.process()
       #message = 'Я понял ваш запрос как "%s"\n\n' % key + message
       """
   else:
       hist=api.messages.getHistory(offset=0, count=1, user_id=extract_id, group_id=177456743, access_token = token)   #testbot
       id=hist['items'][0]['id']
       rnd_seed = random.randint(0, 2147483647)
       api.messages.send(random_id=rnd_seed, domain = 'golodyayeva', forward_messages = str(id), group_id = 177456743, access_token = token)   #testbot
       message = 'Привет! Тебе скоро ответят.'
       attachment = ''
       buttons = None
       """
   try:
        return message, attachment, buttons
   except UnboundLocalError:
        pass

def create_answer(data, token):
   load_modules()
   print(data)
   user_id = data['user_id'] #у групп поле "user_id", у встреч from_id
   try:
       message, attachment, buttons = get_answer(extract_id=user_id, body=data['body'].lower())    #у групп поле "body", у встреч - "text"
   except TypeError:
       pass
   try:
        vkapi.send_message(user_id, token, message, buttons, attachment)
   except UnboundLocalError:
        pass
