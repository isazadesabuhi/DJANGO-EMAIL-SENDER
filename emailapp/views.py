from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def sendemail(request):
    if request.method == "POST":
        subject_email = request.POST.get('subject')
        content = request.POST.get('content')

        # Loop to handle dynamic email inputs
        index = 1
        while True:
            email_key = f'toemail{index}'
            to_email = request.POST.get(email_key)

            # Break if there's no more email input with the current index
            if not to_email:
                break

            send_mail(
                subject_email,
                content,
                settings.EMAIL_HOST_USER,
                [to_email]
            )

            # Increment the index to process the next email input
            index += 1

        return render(
            request,
            'email.html',
            {
                'title': 'send an email'
            }
        )
    else:
        return render(
            request,
            'email.html',
            {
                'title': 'send an email'
            }
        )
