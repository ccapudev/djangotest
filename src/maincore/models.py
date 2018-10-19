from django.db import models
from django.core.validators import ValidationError
from maincore import create_model

class App(models.Model):
    name = models.CharField(max_length=255)
    module = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Model(models.Model):
    app = models.ForeignKey(
        App, related_name='models', on_delete=models.DO_NOTHING
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_django_model(self):
        "Returns a functional Django model based on current data"
        # Get all associated fields into a list ready for dict()
        fields = [(f.name, f.get_django_field()) for f in self.fields.all()]

        # Use the create_model function defined above
        return create_model(self.name, dict(fields), self.app.name, self.app.module)

    class Meta:
        unique_together = (('app', 'name'),)

def is_valid_field(self, field_data, all_data):
    if hasattr(models, field_data) and issubclass(getattr(models, field_data), models.Field):
        # It exists and is a proper field type
        return
    raise ValidationError("This is not a valid field type.")

class Field(models.Model):
    model = models.ForeignKey(Model, related_name='fields', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, validators=[is_valid_field])

    def get_django_field(self):
        "Returns the correct field type, instantiated with applicable settings"
        # Get all associated settings into a list ready for dict()
        settings = [(s.name, s.value) for s in self.settings.all()]

        # Instantiate the field with the settings as **kwargs
        return getattr(models, self.type)(**dict(settings))

    class Meta:
        unique_together = (('model', 'name'),)

class Setting(models.Model):
    field = models.ForeignKey(Field, related_name='settings', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = (('field', 'name'),)


'''
from maincore import create_model, create_install_model
model = create_install_model('Empty', app_label='dynamic')
from maincore.models import Model
model = Model.objects.get(app__name='fake_project', name='FakeModel')
'''