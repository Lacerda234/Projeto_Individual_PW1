## PET'S LOVERS

A ideia principal do projeto é criar um sistema que facilite a adoção de animais, onde quem quiser fazer uma adoção poderá entrar no site, realizar seu cadastro e escolher algum dos animais que estejam disponíveis para adoção. Será realizada uma análise do cadastro para decidir se a pessoa realmente poderá adotar o animal desejado.

# Como rodar o projeto

- Clone o projeto, para isso você pode simplesmente baixar o arquivo ou usar o git, para clonar diretamente do repositório remoto :
```
git clone https://github.com/ifpb-cz-ads/pw1-2021-2-ai-Lacerda234.git
```

- Dentro do repositório, agora local, você precisa criar um novo ambiente virtual. Seja ele qual for, o próximo passo é acessa-lo e partir para a próxima etapa.

- Para ativar o ambiente virtual, se estiver usando linux ou Mac,use o seguinte comando :
```
source venv/bin/activate
```
- Se estiver usando windows use:
```
./venv/Scripts/Activate.ps1
```

- Após ativado, instalar todas as bibliotecas necessárias :
```
python -m pip install -r requirements.txt
```

- Não esqueça de rodas as migrations :
```
python manage.py makemigrations
```

- E então :
```
python manage.py migrate
```

- Feito isso, você pode iniciar a qualquer momento com :
```
python manage.py runserver
```

Por fim, acesse o site neste link : [http://localhost:8000/](http://localhost:8000/)
