# BombCrypto Bot

- [en-us] For change to english Readme version click [here](https://github.com/guimatheus92/Bot_BombCrypto/blob/main/README.md "here").
- [pt-br] Para alterar para a versão Readme em português, clique [aqui](https://github.com/guimatheus92/Bot_BombCrypto/blob/main/README.pt.md "aqui").

------------

Este é uma automação (bot) para jogar o jogo BombCrypto, esse bot automaticamente loga no jogo, coloca os heróis para trabalhar, atualiza o jogo para não cair por tempo de resposta, checa novos maps, etc.

Se você achou que esse bot foi uma ajuda para você, por favor faça uma doação com as opções abaixo, assim podemos continuar a melhorar o grande trabalho que gastei e por tantas horas gastas 🤯.

![Donation](https://github.com/guimatheus92/Bot_BombCrypto/blob/main/static/img/readme/qr_code.png)

**Donations options:**

- **BUSD/BCOIN/ETH/BNB (BEP20):** 0xf1e43519fca44d9308f889baf99531ed0de903fc
- **PayPal:** https://www.paypal.com/donate/?hosted_button_id=82CABN6CYVG6U
- **Pix:** 42a762ed-e6ec-4059-a88e-f168b9fbc63f (chave aleatória)

## Project structure
    .
    └── Bot_BombCrypto
        ├── main.py                    # inicia nosso app
        ├── bot.py                     # todos os movimentos e mecânicas para o bot
        ├── controllers.py             # todos os controles para ajudar o bot a rodar
        ├── config.yaml                # todas as configurações para ajudar o bot a rodar
        └── logs                       # todos os arquivos log são salvos aqui
        └── static
            ├── img
                ├── game               # todas as imagens relacionadas ao jogo estarão aqui
                ├── readme             # todas as imagens relacionadas ao repositório

## Tutorial

O tutorial para instalar e usar esse bot pode ser encontrado aqui [GitHub Wiki](https://github.com/guimatheus92/Bot_BombCrypto/wiki/How-to-execute-BombCrypto-bot "GitHub Wiki").

#### Algumas configurações podem ser alteradas no arquivo config.yaml. Caso mude, não se esqueça de reiniciar o bot para que as novas configurações sejam ativadas.

## Atualizações

- **19/01/2022**: Lançado a primeira versão sem multiplas contas

## Requisitos

Versão do Windows:
- `Windows 10`

- `Windows 11`

Versão do Python:
```python
Python 3.9.9
```

Os requisitos também podem ser encontrados no arquivo `requirements.txt`.
Este projeto utiliza os seguintes requisitos:

    APScheduler==3.6.3
    numpy==1.21.4
    PyAutoGUI==0.9.53
    python-telegram-bot==13.9
    pywin32==303
    pywinauto==0.6.8
    PyYAML==6.0
    requests==2.26.0
    tzlocal==4.1

Escala do monitor: `100%`

## Observações

- Verifique o tópico de [Requisitos](https://github.com/guimatheus92/Bot_BombCrypto/blob/main/README.pt.md#requisitos "Requisitos") para ter certeza em qual ambiente e versões nós sabemos que funciona.
- Todas as images foram tiradas do jogo de uma tela Full HD e a escala selecionada em 100%. Caso seu bot não esteja funcionando, certifique-se que a escala do seu monitor também esteja em 100%. Após isso, salve todas as imagens novamente e salve elas com o formato `.png`.

## Funcionalidades

- Agende a atualização de heróis no jogo em um período de tempo
- Agende o envio de heróis para trabalhar em um período de tempo
- Exclua arquivos e pastas antigos se desejar automaticamente
- Conecta na carteira
- Conecte-se, faça login e desbloqueie o Metamask
- Modo de jogo Caça ao Tesouro
- Verifique se há novo mapa disponível
- Faça captura de tela de erros e novos mapas
- Envia mensages para o bot do seu Telegram
- Atualização de herói apenas (caso você esteja jogando sozinho)

###### *Atualizar heróis explicados: Bot apenas atualizará o jogo voltando ao menu e depois voltando ao modo Caça ao Tesouro*

## Conclusão

1. Quer o meu código? [Pegue aqui](https://github.com/guimatheus92/Bot_BombCrypto "Grab it here") 📎
2. Quer o tutorial de como usa-lo? [Vá para o Wiki](https://github.com/guimatheus92/Bot_BombCrypto/wiki/How-to-execute-BombCrypto-bot "Go to here") ✔️
3. Novas ideias para este app? Me ajuda a melhora-lo ❤️
4. Quer algo mais adicionado neste tutorial? Crie uma Issu no repositório ⚠️
