from flask_meld import Component
from forms import RegistrationForm


class Register(Component):
    form = RegistrationForm()

    def updated(self, field):
        self.validate(field)
