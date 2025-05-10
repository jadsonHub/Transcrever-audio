import os
import subprocess
import speech_recognition as sr

# Caminho do FFmpeg (substitua pelo seu caminho correto)
FFMPEG_PATH = r"C:\ffmpeg-7.1.1\bin\ffmpeg.exe"

def converter_ogg_para_wav(ogg_path, wav_path):
    """Converte um arquivo OGG para WAV usando FFmpeg."""
    try:
        subprocess.run([FFMPEG_PATH, "-i", ogg_path, "-ac", "1", "-ar", "16000", wav_path], check=True)
        print(f"Conversão concluída: {wav_path}")
    except FileNotFoundError:
        print("Erro: FFmpeg não encontrado. Verifique o caminho do executável.")
    except subprocess.CalledProcessError:
        print("Erro ao converter o arquivo. Verifique o caminho do áudio.")

def transcrever_audio(audio_path):
    """Transcreve um arquivo de áudio para texto."""
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            texto = recognizer.recognize_google(audio, language="pt-BR")
            return texto
    except sr.UnknownValueError:
        return "Não foi possível entender o áudio."
    except sr.RequestError:
        return "Erro na requisição ao serviço de reconhecimento."

# Defina os caminhos dos arquivos
ogg_file = r"C:\Users\jadso\Downloads\WhatsApp Ptt 2025-05-10 at 08.05.01.ogg"
wav_file = r"C:\Users\jadso\Downloads\saida.wav"

# Converter OGG para WAV
converter_ogg_para_wav(ogg_file, wav_file)

# Transcrever áudio
texto_transcrito = transcrever_audio(wav_file)
print("Transcrição:\n", texto_transcrito)