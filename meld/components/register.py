from flask_meld import Component
from forms import RegistrationForm


class Register(Component):
    form_class = RegistrationForm
    registrations = []

    def updated(self, field):
        self.validate(field)
