from abc import ABC, abstractmethod

# Target interface
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, filename: str) -> str:
        pass

# Adaptee (old interface)
class AdvancedMediaPlayer(ABC):
    @abstractmethod
    def play_vlc(self, filename: str) -> str:
        pass

    @abstractmethod
    def play_mp4(self, filename: str) -> str:
        pass

# Concrete Adaptees
class VLCPlayer(AdvancedMediaPlayer):
    def play_vlc(self, filename: str) -> str:
        return f"Playing VLC file: {filename}"

    def play_mp4(self, filename: str) -> str:
        return ""

class MP4Player(AdvancedMediaPlayer):
    def play_vlc(self, filename: str) -> str:
        return ""

    def play_mp4(self, filename: str) -> str:
        return f"Playing MP4 file: {filename}"

# Adapter
class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type: str):
        if audio_type == "vlc":
            self._advanced_player = VLCPlayer()
        elif audio_type == "mp4":
            self._advanced_player = MP4Player()
        else:
            self._advanced_player = None

    def play(self, filename: str) -> str:
        if isinstance(self._advanced_player, VLCPlayer):
            return self._advanced_player.play_vlc(filename)
        elif isinstance(self._advanced_player, MP4Player):
            return self._advanced_player.play_mp4(filename)
        return ""

# Concrete implementation using adapter
class AudioPlayer:
    def play(self, audio_type: str, filename: str) -> str:
        if audio_type == "mp3":
            return f"Playing MP3 file: {filename}"
        elif audio_type in ("vlc", "mp4"):
            adapter = MediaAdapter(audio_type)
            return adapter.play(filename)
        return f"Invalid media type: {audio_type}"


if __name__ == "__main__":
    player = AudioPlayer()
    print(player.play("mp3", "song.mp3"))
    print(player.play("vlc", "movie.vlc"))
    print(player.play("mp4", "video.mp4"))
