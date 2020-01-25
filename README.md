# [Deploy Django Heroku Windows](https://github.com/murilothink/)


### Clone o repositorio com o comando:

git clone https://github.com/murilothink/django_deploy_heroku.git

Esses arquivos precisa fazer parte do seu projeto, todos os .js, CSS e imagens tem que ser colocada dentro do deploy_heroku\static
ou configurre 

Caso queira colocar seus arquivos HTML adicione em deploy_heroku\templates

Observação, caso queira usar nosso settings e preciso configurar o INSTALLED_APP

### Requirements:

suba sua virtual env 

$ \exemplo_caminho\da_sua_enve\scripts\activate 

## Em seu projeto digite

$ (enve) \exemplo_caminho\ pip install -r requirements.txt

$ (enve) \exemplo_caminho\ pip freeze > requirements.txt


### Comandos Heroku e git

heroku login

git init
git add .
git commit -m "First deploy"
heroku config:set DISABLE_COLLECTSTATIC=1
heroku create
git push heroku master








