from abc import ABC, abstractmethod

# Subject interface
class Image(ABC):
    @abstractmethod
    def display(self) -> str:
        pass

# Real Subject
class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._load_from_disk()

    def _load_from_disk(self):
        print(f"Loading image from disk: {self.filename}")

    def display(self) -> str:
        return f"Displaying image: {self.filename}"

# Proxy
class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._real_image: RealImage = None

    def display(self) -> str:
        if self._real_image is None:
            self._real_image = RealImage(self.filename)
        return self._real_image.display()


if __name__ == "__main__":
    # Images are loaded only when displayed
    image1 = ProxyImage("photo1.jpg")
    image2 = ProxyImage("photo2.jpg")

    print("\nFirst display call:")
    print(image1.display())

    print("\nSecond display call (cached):")
    print(image1.display())

    print("\nDisplay another image:")
    print(image2.display())
