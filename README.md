# Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure as instâncias com .env.
6. Execute os testes.

```
console
git clone git@github.com:fabricio-2Uu/eventex.git wttd
cd wttd
python -m venv .wttd
call .wttd/Scripts/activate.bat
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no HEROKU.
2. Envie as configurações para o HEROKU.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o heroku.

```Console
heroku create minhainstancia
heroku config:push
heroku congif:set SECRET_KEY='python contrib/secret_gen.py'
heroku confir:set DEBUG=False
#configuro o email
git push heroku master --force
```