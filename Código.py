from abc import ABC, abstractmethod
from datetime import datetime

#MENSAGENS

class Mensagem(ABC):
    def __init__(self, mensagem: str, data_envio: datetime = None):
        self._mensagem = mensagem
        self._data_envio = data_envio or datetime.now()

    @abstractmethod
    def exibir(self):
        pass

class MensagemTexto(Mensagem):
    def exibir(self):
        return f"[Texto] {self._mensagem} - Enviado em {self._data_envio}"

class MensagemVideo(Mensagem):
    def __init__(self, mensagem, arquivo, formato, duracao):
        super().__init__(mensagem)
        self._arquivo = arquivo
        self._formato = formato
        self._duracao = duracao

    def exibir(self):
        return f"[Vídeo] {self._mensagem} ({self._arquivo}.{self._formato}, {self._duracao}s) - Enviado em {self._data_envio}"

class MensagemFoto(Mensagem):
    def __init__(self, mensagem, arquivo, formato):
        super().__init__(mensagem)
        self._arquivo = arquivo
        self._formato = formato

    def exibir(self):
        return f"[Foto] {self._mensagem} ({self._arquivo}.{self._formato}) - Enviado em {self._data_envio}"

class MensagemArquivo(Mensagem):
    def __init__(self, mensagem, arquivo, formato):
        super().__init__(mensagem)
        self._arquivo = arquivo
        self._formato = formato

    def exibir(self):
        return f"[Arquivo] {self._mensagem} ({self._arquivo}.{self._formato}) - Enviado em {self._data_envio}"


#CANAIS

class Canal(ABC):
    def __init__(self, identificador: str):
        self._identificador = identificador

    @abstractmethod
    def enviar(self, mensagem: Mensagem):
        pass

class WhatsApp(Canal):
    def enviar(self, mensagem: Mensagem):
        print(f"Enviando via WhatsApp para {self._identificador}: {mensagem.exibir()}")

class Telegram(Canal):
    def enviar(self, mensagem: Mensagem):
        print(f"Enviando via Telegram para {self._identificador}: {mensagem.exibir()}")

class Facebook(Canal):
    def enviar(self, mensagem: Mensagem):
        print(f"Enviando via Facebook para {self._identificador}: {mensagem.exibir()}")

class Instagram(Canal):
    def enviar(self, mensagem: Mensagem):
        print(f"Enviando via Instagram para {self._identificador}: {mensagem.exibir()}")


#EXEMPLO

if __name__ == "__main__":
    # Criar mensagen
    msg_texto = MensagemTexto("Olá, tudo bem?")
    msg_video = MensagemVideo("Veja o vídeo", "video_apresentacao", "mp4", 120)
    msg_foto = MensagemFoto("Confira a imagem", "foto_paisagem", "jpg")
    msg_arquivo = MensagemArquivo("Segue o relatório", "relatorio_final", "pdf")

    # Criar canais
    whatsapp = WhatsApp("+551199999999")
    telegram_tel = Telegram("+551198888888")
    telegram_user = Telegram("usuario_telegram")
    facebook = Facebook("usuario_facebook")
    instagram = Instagram("usuario_insta")

    # Enviar mensagem
    whatsapp.enviar(msg_texto)
    telegram_tel.enviar(msg_video)
    telegram_user.enviar(msg_foto)
    facebook.enviar(msg_arquivo)
    instagram.enviar(msg_texto)
