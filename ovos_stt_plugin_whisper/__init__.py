import speech_recognition as sr
from ovos_plugin_manager.templates.stt import STT
from whisper.tokenizer import LANGUAGES
import whisper


class WhisperSTT(STT):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = self.config.get("model", "base")
        self.recognizer = sr.Recognizer()
        self.load_model()

    def load_model(self):
        # will auto download if missing
        if not hasattr(self.recognizer, "whisper_model"):
            self.recognizer.whisper_model = {}
        self.recognizer.whisper_model[self.model] = whisper.load_model(self.model)

    def execute(self, audio, language=None):
        lang = language or self.lang
        lang = lang.split("-")[0]
        utt = self.recognizer.recognize_whisper(audio, language=lang,
                                                model=self.model)
        return utt

    def available_languages(self) -> set:
        return set(LANGUAGES.keys())


WhisperSTTConfig = {}
