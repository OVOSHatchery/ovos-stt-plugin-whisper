import speech_recognition as sr
from ovos_plugin_manager.templates.stt import STT
from whisper.tokenizer import LANGUAGES


class WhisperSTT(STT):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.recognizer = sr.Recognizer()

    def execute(self, audio, language=None):
        lang = language or self.lang
        lang = lang.split("-")[0]
        utt = self.recognizer.recognize_whisper(audio, language=lang)
        return utt

    def available_languages(self) -> set:
        return set(LANGUAGES.keys())


WhisperSTTConfig = {}
