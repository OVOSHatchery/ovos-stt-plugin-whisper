## Description

A stt plugin for ovos using [whisper](https://github.com/openai/whisper)

## Install

`pip install ovos-stt-plugin-whisper`


## Configuration

By default the global language used by mycroft-core will be used

```json
  "stt": {
    "module": "ovos-stt-plugin-whisper",
    "ovos-stt-plugin-whisper": {"model": "base"}
  }
 
```