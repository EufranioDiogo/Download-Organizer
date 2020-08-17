# Download Organizer

Languages: [English](##English), [Português](##Português)

## English

### Introductation
At majority of the time when we are navigating through Internet we download a lot of stuff and consequently we fill up our Download folder with a lot of things like music, pictures, videos and so on. Because of it I decided to put the hands on it and try to give a solution to this huge problem that I also have. 

### Script propose
Track the Downloads folder and put every files that appear right there at the right folder, music goes to music folder, videos goes to video folder and so on.

### What Do I need to get It?
1. You need to have a python3.x installed at your computer, if you are using Linux or Mac OS I guess that you already have python3.x installed, to be sure of that type this command: `python3 --version`. If the result is something like "Python 3.8.2" it means that you already have one version of python3 installed at your computer else go to official python web site and download the last stable relaese of it, [click here to go there](https://www.python.org/downloads/)

### How Install it at your computer?
- **Linux**
  1. Download the repository.
  2. Unpack the repository.
  3. Open the Terminal, typing Terminal at your apps menu or press those keys: **<kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>t</kbd>**
  4. Navitage to **Download Organizer** folder and after enter at **Linux** folder.
  5. After you're already at the Linux folder type those commands bellow:
        ```
        chmod +x install.sh
        sudo ./install.sh
        ```
  6. You'll be asked if do you want agree with the license and with the changes that will happen at your computer, to accept type: Y, y. If you don't agree type: n or any other letter.


### How Uninstall it at your computer?
- **Linux**
  1. Open the Terminal, typing Terminal at your apps menu or press those keys: **<kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>t</kbd>**
  2. Navitage to **Download Organizer** folder and after enter at **Linux** folder.
  3. After you're already at the Linux folder type those commands bellow:
        ```
        chmod +x uninstall.sh
        sudo ./uninstall.sh
        ```
        **Note:** If you don't have the Download Organizer folder that you downloaded first you can also go to /opt/download_organizer/ folder and type the command above.

### How Can I stop the script while it's already running?
- **Linux**
  1. Open the Terminal, typing Terminal at your apps menu or press those keys: **<kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>t</kbd>**
  2. Type: `sudo download_organizer stop`

### How Can I run the script while it's stopped?
- **Linux**
  1. Open the Terminal, typing Terminal at your apps menu or press those keys: **<kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>t</kbd>**
  2. Type: `sudo download_organizer start`

### Questions
  1. If I just want run the script one time what can I do?<br>
  R: It's really can happen, just stop the script with: `sudo download_organizer stop` after run the command this command type `download_organizer` and after the work done type `sudo download_organizer stop`

- Mac Os <br>
    I don't know if I'll do it, I don't promisse anything.

- Windows <br>
    I'm still studying, about the services and how work with filesystem. 
<hr>

## Português

### Introdução
Na maior parte do tempo navegando pela Internet nos fizemos o download the várias coisas e consequentemente nos enchemos o nossa pasta de Downloads com muitas coisas como músicas, imagens, vídeos e entre outros. Por causa disso decidi colocar as minhas mãos nisso e tentar dar uma solução para este problema que eu também tenho.

### Propósito do Script
Controlar o directório Downloads(Transferência) e colocar todos os ficheiros que aparecem lá no seu devido directório, músicas vão para o directório musicas, vídeos vão para o directório vídeos e assim sucessivamente.

### O que eu preciso para ter isto?
1. Você precisa ter o python3.x instalado no seu computador, se você está usando Linux ou Mac OS acho que que você já tem ele instalado, para confirmar digite o comando: `python3 --version`. Se o resultado for algo como "Python 3.8.2" isso significa que você já tem uma versão do python3 instalada no seu computador senão vá para o site oficial do python e faça o download da última versão estavel, [clique aqui para ir para lá](https://www.python.org/downloads/)

### Como instalar isso no teu computador?
- **Linux**
  1. Baixe o repositório.
  2. Desempacote o repositório.
  3. Abra o Terminal, digitando Terminal no menu de aplicações ou pressione as teclas: **<kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>t</kbd>**
  4. Navegue para o directório **Download Organizer** e depois entre no directório **Linux**.
  5. Depois de estar no directório Linux digite os seguintes comandos abaixo:
        ```
        chmod +x install.sh
        sudo ./install.sh
        ```
  6. Você será questionado se aceita com a licensa e com as alterações que irão acontecer no seu computador, para aceitar digite: Y, y. Se você não concorda digite: n or qualquer outra letra.

### Como desinstalar isso do seu computador?
- **Linux**
  1. Abra o Terminal, digitando Terminal no menu de aplicações ou pressione as teclas: **<kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>t</kbd>**
  2. Navegue para o directório **Download Organizer** e depois entre no directório **Linux**.
  3. Depois de estar no directório Linux digite os seguintes comandos abaixo:
        ```
        chmod +x uninstall.sh
        sudo ./uninstall.sh
        ```
        **Nota:** Se você já não tem a pasta Download Organizer que você baixou primeiro você pode ir até a pasta /opt/download_organizer/ e digitar os comandos a cima.

### Como posso para o script enquanto ele está rodando?
- **Linux**
  1. Abra o Terminal, digitando Terminal no menu de aplicações ou pressione as teclas: **<kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>t</kbd>**
  2. Digite: `sudo download_organizer stop`

### Como posso colocar a funcionar o script enquanto está parado?
- **Linux**
  1. Abra o Terminal, digitando Terminal no menu de aplicações ou pressione as teclas: **<kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>t</kbd>**
  2. Digite: `sudo download_organizer start`

### Questões
  1. Se eu só quero executar o script uma vez o que eu posso fazer?<br>
  R: Isso pode sim acontecer, apenas para o script com: `sudo download_organizer stop` depois digite o comando  `download_organizer` depois do trabalho executado digite `sudo download_organizer stop`

- Mac Os <br>
    Eu não sei se farei isso, não prometo nada.

- Windows <br>
    Ainda estou estudando, sobre serviços e como trabalhar com o sistema de arquivos.