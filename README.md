# Crawlers

Este programa retorna os *trending threads* dos subreddits do [Reddit](#reddit) passados como parâmetro. Ele pode ser chamado de dois modos, descritos mais abaixo: **modo terminal** e **modo _bot_** (ou **modo crawler**), integrado com o [Telegram](#telegram).


### Reddit

O [Reddit](https://www.reddit.com) é quase como um fórum com milhares de categorias diferentes. Com a sua conta, você pode navegar por assuntos técnicos, ver fotos de gatinhos, discutir questões de filosofia, aprender alguns life hacks e ficar por dentro das notícias do mundo todo!

Subreddits são como fóruns dentro do Reddit e as postagens são chamadas *threads*.

Para quem gosta de gatos, há o subreddit ["/r/cats"](https://www.reddit.com/r/cats) com *threads* contendo fotos de gatos fofinhos.
Para *threads* sobre o Brasil, vale a pena visitar ["/r/brazil"](https://www.reddit.com/r/brazil) ou ainda ["/r/worldnews"](https://www.reddit.com/r/worldnews/).
Um dos maiores subreddits é o ["/r/AskReddit"](https://www.reddit.com/r/AskReddit).

Cada *thread* possui uma pontuação que, simplificando, aumenta com "up votes" (tipo um like) e é reduzida com "down votes".

### Telegram

O [Telegram](http://telegram.org) é um serviço de mensagens OpenSource (licença GNU GPL) que funciona baseado na Nuvem e possui criptografia de alto nível. Ele possui uma API para que desenvolvedores implementem códigos ou interfaces que façam uso de seus serviços.

*Bot* é um tipo de conta do Telegram usado para rodar programas e scripts dentro dos clientes Telegram (aplicativos, extensões de navegadores, etc). Por exemplo, [YTranslateBot](https://telegram.me/YTranslateBot) é um *Bot* que permite a tradução de textos entre várias línguas dentro do próprio Telegram.


## Sobre o programa

### Arquivos

* `readReddit.py`: arquivo com a função readReddit() usada para ler as informações do servidor do Reddit.
* `RedditTerm.py`: arquivo executável para rodar no terminal (modo Terminal).
* `RedditBot.py`: arquivo executável para rodar o *Bot* no Telegram (modo *Bot*).


### Requisitos de instalação

* Python 2.7.* (não testado no Python 3.*)
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
* [requests](https://github.com/requests/requests)

### Entrada

O parâmetro de entrada para ambos os modos é uma lista com os nomes dos subreddits separados por ponto-e-vírgula (`;`). Ver abaixo como chamar o executável para os modos [teminal](#modo-terminal) e [bot](#modo-bot).

### Saída

A saída é a impressão das informações abaixo de todos os *threads* de cada subreddit de entrada que:

1. tenham mais de 5000 up votes; e
2. estejam entre os 25 primeiros classificados como *hot* pelo Reddit.

As informações são impressas na seguinte ordem: Título do *thread*; número de up votes; URL do subreddit; URL; e URL dos comentários no Reddit.



## Modo Terminal

O modo terminal é chamado dentro diretório onde o código `RedditTerm.py` através do seguinte comando:

```
python RedditTerm.py "*lista*"
```

ou

```
./RedditTerm.py "*lista*"
```

onde `*lista*` é o [parâmetro de entrada](#entrada). Observe que o parâmetro deve ser colocado entre aspas.

### Status

Este modo retorna um código padrão de status para o sistema:

* 0: caso o processamento tenha sido efetuado com sucesso.
* 1: caso tenha havido algum erro.



## Modo Bot

O *bot* [RedditBot](https://telegram.me/DanBedBot) é utilizado para requisições ao código Python `RedditBot.py`, que se comunica com o Telegram através da Nuvem.

Para que o *bot* funcione, é necessário que o código `RedditBot.py` seja rodado em algum computador local ou servidor. Para isso, abra um terminal dentro deste diretório onde se encontra e digite o seguinte comando:

```
python ./RedditBot.py &
```

ou

```
./RedditBot.py &
```

O caractere `&` faz o código ser rodado em segundo plano e, portanto, permite que o mesmo não seja interrompido com o fechamento do terminal.


### Comandos do RedditBot

No link do [RedditBot](https://telegram.me/DanBedBot) clique em *Send Message* para convidar o *bot* para seu Telegram.

Apenas dois comandos são permitidos para o RedditBot:

* `/start`
  Imprime a funcionalidade do *bot* e explica como rodá-lo.

* `/NadaPraFazer *lista*`
  Manda o comando para a Nuvem passando o parâmetro[parâmetro de entrada](#entrada) de `*lista*`.


## Autor

Daniel Bednarski Ramos

[https://www.astro.iag.usp.br/~bednarski](https://www.astro.iag.usp.br/~bednarski)

daniel.bednarski.ramos@gmail.com


## Licença

GNU GPLv3
