from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from project.account.tasks import send_email


@receiver(post_save, sender=CustomUser)
def send_email(sender, instance, created, **kwargs):
    if created:
        send_email.delay(
            'Welcome To Good-Reads Clone!',
            f"Hi {instance.username} welcome to Good-Reads Cone , we are glad to see you here in the world's best library . "
            f"Enjoy reading millions of books and do not forget to leave your reviews about them . Have a good journey and "
            f"see you in the library . ",
            [instance.email]
        )

