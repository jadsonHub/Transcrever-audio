import subprocess
import ctypes
ctypes.CDLL("C:\\Windows\\System32\\msvcrt.dll")  # Forçando um caminho manual
import whisper

# Caminho do FFmpeg
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

def transcrever_com_whisper(audio_path):
    """Transcreve um arquivo de áudio usando Whisper da OpenAI."""
    model = whisper.load_model("large")  # Use "large" para maior precisão
    result = model.transcribe(audio_path, language="portuguese")
    return result["text"]

# Defina os caminhos dos arquivos
ogg_file = r"C:\Users\jadso\Downloads\WhatsApp Ptt 2025-05-10 at 08.05.01.ogg"
wav_file = r"C:\Users\jadso\Downloads\saida.wav"

# Converter OGG para WAV
converter_ogg_para_wav(ogg_file, wav_file)

# Transcrever áudio com Whisper
texto_transcrito = transcrever_com_whisper(wav_file)
print("Transcrição aprimorada:\n", texto_transcrito)