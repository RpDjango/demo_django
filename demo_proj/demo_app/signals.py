from django.db.models.signals import post_save, pre_delete, post_delete, pre_save
from django.dispatch import receiver
from demo_app.models import Product

@receiver(post_save, sender=Product)
def my_handler(sender, **kwargs):
    print(f"Product created! {kwargs}")

@receiver(pre_delete, sender=Product)
def mymodel_pre_delete(sender, instance, **kwargs):
    # do something before MyModel instance is deleted
    print("Pre delete called!")

@receiver(post_delete, sender=Product)
def mymodel_post_delete(sender, instance, **kwargs):
    # do something after MyModel instance is deleted
    print("Post delete called!")

@receiver(pre_save, sender=Product)
def mymodel_pre_save(sender, instance, **kwargs):
    # do something before MyModel instance is saved
    print(f"Pre save the product {instance} {kwargs}!")