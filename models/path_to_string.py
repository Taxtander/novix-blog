from pathlib import Path
class FileConverter:
    def __init__(self, path:Path) :
        self.path = path
    def convert(self) -> str:
        with open(self.path, "a") as file:
            content = file.read()
            return content

