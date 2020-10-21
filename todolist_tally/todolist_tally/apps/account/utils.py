from django.core.mail import send_mail
from todolist_tally.apps.account.models import User


class SendEmailMessage():
    def __init__(self, subject="你还有待办事项没有完成"):
        self.subject = subject
        self.user_message_dict = {}
        self.get_user_has_notdone_todo()

    def get_user_has_notdone_todo(self):
        all_user = User.objects.all()
        for user in all_user:
            all_todo = user.todo_set.all()
            for todo in all_todo:
                if todo.done is False:
                    try:
                        self.user_message_dict[user.username]
                    except Exception:
                        self.user_message_dict[user.username] = ""
                    self.user_message_dict[
                        user.username] += "\n" + todo.content

    def send(self):
        for username in self.user_message_dict:
            user = User.objects.get(username=username)
            send_mail(self.subject,
                      self.user_message_dict[username],
                      "zzsealy@qq.com", [user.email],
                      fail_silently=False)


def send_todo_email():
    s = SendEmailMessage()
    s.send()
