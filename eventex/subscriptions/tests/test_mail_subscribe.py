from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Fabricio Gatto", cpf="79797979797",
                    email="fa_gatto7@yahoo.com.br", phone="21-97979-7979")
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'fa_gatto7@yahoo.com.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Fabricio Gatto',
            '79797979797',
            'fa_gatto7@yahoo.com.br',
            '21-97979-7979'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)