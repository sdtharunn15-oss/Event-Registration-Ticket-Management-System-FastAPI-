from fastapi_mail import FastMail, MessageSchema, ConnectionConfig


conf = ConnectionConfig(

    MAIL_USERNAME="your_email@gmail.com",

    MAIL_PASSWORD="your_password",

    MAIL_FROM="your_email@gmail.com",

    MAIL_PORT=587,

    MAIL_SERVER="smtp.gmail.com",

    MAIL_STARTTLS=True,

    MAIL_SSL_TLS=False
)



async def send_email(email):

    message = MessageSchema(

        subject="Event Registration Successful",

        recipients=[email],

        body="Your event registration is successful.",

        subtype="plain"

    )


    fm = FastMail(conf)

    await fm.send_message(message)