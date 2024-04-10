class Contact:
    def __init__(self,name,phone_number,email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self) -> str:
        return f"Name: {self.name}\nPhone_number: {self.phone_number}\nEmail: {self.email}"



contact1 = Contact("Johan doe","12345678","johan@hmail.com")
print(contact1)
