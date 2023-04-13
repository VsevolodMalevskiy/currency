from rest_framework import serializers

from currency.models import Rate, Source, ContactUs, RequestResponseLog


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'created',
            'source',
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'source_url',
            'name',
            'code_name',
        )


class ContactusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id',
            'created',
            'name',
            'email',
            'subject',
            'message',
        )

    # отправка email, изменение функции создания объекта
    def create(self, validated_data):
        from django.core.mail import send_mail
        data_email = ContactUs(**validated_data)
        subject = 'User ContactUs'
        recipient = 'support@rambler.ru'
        sender = 'User@gmail.com'
        message = f'''
                    Request from: {data_email.name}
                    Reply to email: {data_email.email}
                    Subject: {data_email.subject}
                    Body: {data_email.message}
                '''
        send_mail(
            subject,
            message,
            sender,
            [recipient, sender],
            fail_silently=False,
        )
        return ContactUs.objects.create(**validated_data)


class RequestResponseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestResponseLog
        fields = (
            'id',
            'path',
            'request_method',
            'time',
        )
