# lango-tune
An API for reproducing songs in other languages than the original. `lango-tune` translates song lyrics which it queries through Google's search API and reproduces the song via pitch-adjusted text-to-speech.

## Setup

- **Development**: `python setup.py develop`
- **Production**: `python setup.py install`

Add packages/dependencies to `requirements.txt` as necessary to ensure the app builds.

__NOTE__: All project modules and code *must* go into the `src` directory, or else setup will not detect them.

`lango-tune` requires an install of [FFmpeg](https://www.ffmpeg.org/download.html) for its audio manipulation backend.

## API

Send an HTTP GET query to `/api` with the following parameters:

- `name`: song title
- `lang`: language you wish to translate song to
- `path`: url of an audio file (`.wav` format) matching the song title you wish to translate

The API will return a JSON of the following format:
- `song`: song title
- `lang`: language of translated song
- `path`: input audio URL
- `raw_output`: raw binary of converted audio song
- `filetype`: extension to decode raw output