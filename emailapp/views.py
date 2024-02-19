# Django imports
# For rendering templates.
from django.shortcuts import render
# Function to facilitate email sending.
from django.core.mail import send_mail

# For accessing project settings, in this case, the email configuration.
from django.conf import settings


def sendemail(request):
    # Check if the HTTP method is POST, which typically indicates data submission.
    if request.method == "POST":
        # Fetch the email subject from the submitted form.
        subject_email = request.POST.get('subject')

        # Fetch the email content/body from the submitted form.
        content = request.POST.get('content')

        # Initialize an index for looping through dynamic email inputs.
        index = 1
        # Initialize a counter to track successfully sent emails
        emails_sent = 0  

        # Loop to handle multiple email recipients with dynamic input names (like toemail1, toemail2,...).
        while True:
            # Construct the name of the form input dynamically.
            email_key = f'toemail{index}'

            # Fetch the email address using the dynamic input name.
            to_email = request.POST.get(email_key)

            # If there's no more email input for the current index, break out of the loop.
            if not to_email:
                break

            # Use Django's send_mail function to send the email.
            send_mail(
                subject_email,            # Subject of the email.
                content,                  # Content or body of the email.
                # Sender's email address, fetched from Django's settings.
                settings.EMAIL_HOST_USER,
                # List of recipients. In this case, just one recipient.
                [to_email]
            )

            # Move on to the next possible email input.
            index += 1
            
            emails_sent +=1
            
            # Check if at least one email was sent successfully
        email_sent_status = "Your email has been sent!" if emails_sent > 0 else "Failed to send email."

        # After sending all emails, render the email template with a title.
        return render(
            request,
            'email.html',
            {
                'title': 'send an email',
                'email_sent_status': email_sent_status  # Pass the email sent status to the template
            }
        )
    else:
        # If the request method isn't POST (e.g., it's a GET request), just render the email template.
        return render(
            request,
            'email.html',
            {
                'title': 'send an email',
            }
        )
