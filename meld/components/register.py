from flask_meld.component import Component
from forms import RegistrationForm


class Register(Component):
    form_class = RegistrationForm
    registrations = []

    def updated(self, field):
        self.validate(field)

    def register(self):
        print(self.validate)
        if self.validate():
            print("fucking validated")
            self.registrations.append(self.email)

        # print(self.email.data)
        # print(self.form.password)
        # print(self.form.password_confirm)
        # self.registrations.append(self.form.email)
