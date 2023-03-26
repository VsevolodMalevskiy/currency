from django.contrib.auth.models import AbstractUser
from django.db import models
from django.templatetags.static import static


def avatar_path(instance, filename):
    return f"avatars/{instance.id}/{filename}"  # avatar сохрянется в дирректории static\avatars\id


class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.FileField(
        default=None,
        null=True,
        blank=True,
        upload_to=avatar_path
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property    # проверка наличия фото, при отсутствии вставка анонимного аватара (profile.html)
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url

        return static('anonymous-avatar.jpeg')
