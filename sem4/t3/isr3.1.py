class Post():
    def __init__(self, user_id, text):
        self.id = user_id
        self.text = text

    def __str__(self):
      return f"Author: {self.id}\n Text: {self.text}"

class Comment(Post):
    def __init__(self, user_id, reply_to, text):
        Post.__init__(self, user_id, text)
        self.text = text
        self.reply_to = reply_to

    def __str__(self):
      return f"Author: {self.id}\n Reply to: {self.reply_to}\n Comment: {self.text}"

post = Post(user_id='aaa', text='post')
print('Post:\n\n', post)
comment = Comment(user_id='bittle', reply_to='pau', text='text')
print('\nComment:\n\n', comment)
