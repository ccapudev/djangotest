from django.db import models
from django.core.validators import ValidationError
from . import create_model, install
from uuid import uuid4
from maincore.utils import get_valid_fields, choice_fields


class App(models.Model):
    uid = models.UUIDField(default=uuid4)
    name = models.CharField(max_length=255)
    module = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Model(models.Model):
    uid = models.UUIDField(default=uuid4)
    app = models.ForeignKey(
        App, related_name='models', on_delete=models.DO_NOTHING
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}_{}'.format(
            self.app.module,
            self.name,
        )

    @classmethod
    def create_table(cls):
        install(cls)

    def get_django_model(self):
        "Returns a functional Django model based on current data"
        # Get all associated fields into a list ready for dict()
        fields = [(f.name, f.get_django_field()) for f in self.fields.all()]

        # Use the create_model function defined above
        return create_model(
            self.name, dict(fields), self.app.name, self.app.module,
            admin_opts=[]
        )

    class Meta:
        unique_together = (('app', 'name'),)

def is_valid_field(field_data, *args, **kwargs):
    if hasattr(models, field_data) and issubclass(getattr(models, field_data), models.Field):
        # It exists and is a proper field type
        return
    raise ValidationError("%s no es un tipo de campo válido" % field_data)




class Field(models.Model):
    uid = models.UUIDField(default=uuid4)
    model = models.ForeignKey(Model, related_name='fields', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=255,
        validators=[is_valid_field], choices=choice_fields)

    def save(self, *args, **kwargs):
        from django.template.defaultfilters import slugify
        self.name = slugify(self.name).replace('-', '_')
        super().save(*args, **kwargs)

    def get_django_field(self):
        "Returns the correct field type, instantiated with applicable settings"
        # Get all associated settings into a list ready for dict()
        settings = [(s.name, s.value) for s in self.settings.all()]

        # Instantiate the field with the settings as **kwargs
        return getattr(models, self.type)(**dict(settings))

    class Meta:
        unique_together = (('model', 'name'),)

class Setting(models.Model):
    uid = models.UUIDField(default=uuid4)
    field = models.ForeignKey(Field, related_name='settings', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = (('field', 'name'),)


'''
from maincore import create_model, create_install_model
model = create_install_model('weblog', app_label='dynamic')
from maincore.models import Model
model = Model.objects.get(app__name='fake_project', name='FakeModel')
'''