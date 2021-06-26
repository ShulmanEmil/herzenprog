class Post():
    def __init__(self, user_id, text):
      self.__verify_text(user_id)
      self.__verify_text(text)
      self.__user_id = user_id
      self.__user_text = text


    @property
    def id_user(self):
      return self.__user_id

    @id_user.setter
    def id_user(self, user_id):
      try:
        self.__verify_text(user_id)
      except ValueError as e:
        print(e)
      else:
        self.__user_id = user_id

    @property
    def text_post(self):
      return self.__user_text

    @text_post.setter
    def text_post(self, text):
      try:
        self.__verify_text(text)
      except ValueError as e:
        print(e)
      else:
        self.__user_text = text

    def __verify_text(self, text,field='text'):
      if len(text) == 0:
        raise ValueError(f'Поле {field} обязательное поле')

    def __str__(self):
      return f"Author: {self.id_user}\n Text: {self.text_post}"

class Comment(Post):
    def __init__(self, user_id, reply_to, text):
        Post.__init__(self, user_id, text)
        self.text = text
        self.reply_to = reply_to

    def __str__(self):
      return f"Author: {self.id_user}\n Reply to: {self.reply_to}\n Comment: {self.text}"

post = Post(user_id='aaa', text='post')
print('Post:\n\n', post)
comment = Comment(user_id='bittle', reply_to='pau', text='text')
print('\nComment:\n\n', comment)
