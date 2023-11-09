from django.core.mail.backends.smtp import EmailBackend

class CustomEmailBackend(EmailBackend):
    def __init__(self, sender):
        super().__init__()
        self.sender = sender

    def send_messages(self, email_messages):
        # Set email settings based on the sender
        self.host = self.sender.EMAIL_BACKEND
        self.host = self.sender.EMAIL_HOST
        self.port = self.sender.EMAIL_PORT
        self.username = self.sender.EMAIL_HOST_USER
        self.password = self.sender.EMAIL_HOST_PASSWORD
        self.use_tls = self.sender.EMAIL_USE_TLS

        return super().send_messages(email_messages)
