# 📜 transcript-youtube-video

---

<img src="assets/code.png" alt="O código Python que salva as transcrições">

## 📑 Sumário

* [📜 O que é](#-o-que-é-)
* [🧰 Pré-requisitos](#-pré-requisitos)
* [🚀 Como utilizar](#-como-utilizar-)
* [📂 Estrutura do Projeto](#-estrutura-do-projeto)
* [📄 Exemplo de saída](#-exemplo-de-saída)
* [⚠️ Aviso](#️-aviso-)
* [🐛 Como relatar um problema](#-como-relatar-um-problema)

---

## 📜 O que é? 🤷🏻

**`transcript-youtube-video`** é um bot em Python que coleta automaticamente a **transcrição de vídeos do YouTube** e salva o conteúdo em um arquivo `.txt`.

Ele utiliza o navegador automatizado **Playwright** para abrir o vídeo, localizar a transcrição e exportá-la — tudo isso com apenas **um comando**.

---

## 🧰 Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados no seu sistema:

* [Python 3.8+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)
* [Playwright](https://playwright.dev/python/)

---

## 🚀 Como utilizar

### 1. Verifique se o Git está instalado

```bash
git -v
```

Se a saída for algo como `"git version 2.x.x"`, você está pronto para continuar.

---

### 2. Clone o repositório

```bash
git clone https://github.com/flameastro/transcript-youtube-video.git
```

---

### 3. Instale as dependências

```bash
pip install playwright
playwright install
```

---

### 4. Execute o bot

Dentro da pasta do projeto, rode:

```bash
python main.py
```

O programa pedirá um **link do vídeo do YouTube**:

```
Insira a URL do vídeo do YouTube: https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Após inserir, uma nova janela do navegador **Chromium** será aberta automaticamente.
Basta **aguardar alguns segundos** enquanto o bot coleta a transcrição.

Se tudo correr bem ✅, a transcrição será salva no arquivo `transcript.txt`.

---

## 📂 Estrutura do Projeto

```
transcript-youtube-video/
├─ assets/
│  ├─ code.png
│  └─ output.png
├─ main.py
└─ transcript.txt   # gerado automaticamente após a execução
```

---

## 📄 Exemplo de saída

<img src="assets/output.png" alt="Um exemplo de transcrição de saída">

Exemplo de como o terminal se comporta:

```bash
$ python main.py
Insira a URL do vídeo do YouTube: https://www.youtube.com/watch?v=dQw4w9WgXcQ

✅ Transcrição salva com sucesso em transcript.txt
```

---

## ⚠️ Aviso

* Alguns vídeos **não possuem transcrição**, principalmente quando:

  * São **músicas** ou clipes
  * Possuem **pouco ou nenhum áudio**
  * O autor desativou as **legendas automáticas**

Nesses casos, o arquivo `transcript.txt` pode ficar vazio.

---

## 🐛 Como relatar um problema

Se encontrar algum bug ou comportamento inesperado, você pode:

1. Abrir uma **issue** neste repositório.
2. Usar um **título descritivo** e explicar claramente o problema.
3. Se possível, inclua **imagens, logs ou passos para reproduzir** o erro.

---

💡 **Contribuições são bem-vindas!** Sinta-se livre para enviar *pull requests* e melhorar o projeto.
