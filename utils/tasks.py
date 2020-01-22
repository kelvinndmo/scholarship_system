
# Create your tasks here
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

"""A handy class to send emails."""

# this will help cleanup email sending


def send_email_notification(body):
    """
    Handles sending of notifications to the user via email
    Arguments:
        body: {
            subject: "",
            recipient: ["test1@t.c","test2@t.c"], # an array or emails
            text_body: "", # Sample text email template
            html_body: "", # Sample html email template
            context: {} # A dict to be used as the template’s context for
                          rendering.
        }
    :param body:
    :return: Null
    """
    text_body = body['context']
    html_body = body['context']

    msg = EmailMultiAlternatives(subject=body['subject'],
                                 from_email="noreply@scholarships.com",
                                 to=body['recipient'],
                                 body=text_body)
    msg.attach_alternative(html_body, "text/html")
    msg.send()
