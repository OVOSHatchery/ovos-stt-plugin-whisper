import speech_recognition as sr
from ovos_plugin_manager.templates.stt import STT


class WhisperSTT(STT):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.recognizer = sr.Recognizer()

    def execute(self, audio, language=None):
        lang = language or self.lang
        l1, l2 = lang.split("-")
        lang = f"{l1.lower()}-{l2.upper()}"
        utt = self.recognizer.recognize_whisper(audio, language=lang)
        return utt


WhisperSTTConfig = {}
