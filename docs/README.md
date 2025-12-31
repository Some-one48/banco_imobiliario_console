# Banco Imobiliário para Console
Uma versão simples de Banco Imobiliário ainda em desenvolvimento, que pode ser rodada localmente através do terminal

## Instalação
#### Pré-requisitos: 
* Ter instalado o Python versão 3.14.0
* Ter instalado o VS Code, ou outro editor de código que seja compatível com Python

#### Passo a Passo:
1. Vá em "Code" na pasta do repositório no GitHub e clique em "Download ZIP"
2. Após baixar o arquivo ZIP do projeto, vá em seu Gerenciador de Arquivos e extraia "banco_imobiliario_console.zip"
3. Com o arquivo extraído, clique sobre ele com o botão direito e selecione "Abrir com Code" (ou "Abrir com..." outro editor de código que você tenha)
4. Abra o arquivo [main.py](main.py)
5. Dê Ctrl + S
6. Dê Ctrl + Alt + N ou clique no simbolo de Play (triângulo) no canto superior direito da tela
7. Divirta-se!

Obs.: É necessário que você tenha um editor de código, como o VS Code, instalado para isso.

### Estrutura do Projeto
    banco_imobiliario_console/  
    ├── docs/
    │   ├── LICENSE
    │   └── README.md
    ├── main.py  
    └── terrenos.csv  
    
## Como jogar?
### Definições iniciais
Para compreender melhor, daremos um exemplo prático onde três amigos - Jonas, Mariana e Miguel - estarão jogando o jogo.

Ao iniciar o programa com o comando Ctrl+Alt+N, será impresso na tela

    ----------------------------------------------
            BEM-VINDO AO BANCO IMOBILIÁRIO
    ----------------------------------------------
    Digite a quantidade de jogadores: 
    
Agora, você deverá inserir a quantidade de jogadores no terminal, variando de 2 a 4 pessoas.
Seguindo o nosso exemplo, o grupo digitará "3".

![imagem de exemplo 1](/docs/img/img1.png)

Em seguida, será requisitado o nome dos jogadores, para definir os turnos.

        Digite o nome do jogador X: 
        
A ordem que for inserida será a ordem de jogada.
Obs.: Não esqueça de dar Enter após digitar o nome, caso contrário, o programa não seguirá para o próximo jogador.

Então será impressa a ordem de jogada:

    --------------------------------
            ORDEM DE JOGADA:
    --------------------------------
    1. Mariana
    2. Miguel
    3. Jonas
    
Não é necessário que os jogadores façam nada. Após 2 segundos o terminal será limpo.

### O Jogo

## Licença
Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.  
