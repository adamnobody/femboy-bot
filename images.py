from io import TextIOWrapper
from typing import List, TextIO, Union

import urllib


class ImagesLoader:
    def __init__(self, filename: str = 'urls.txt'):
        """Class for work with images - load to base, create a list of images."""
        self.filename = filename

    def openFile(self, setting: str = 'r') -> Union[TextIO, TextIOWrapper]:
        """Open file with given mode."""
        file = open(self.filename, setting)

        return file

    def closeFile(self, fileObj: Union[TextIO, TextIOWrapper]) -> None:
        """Close given file object."""
        fileObj.close()

    def addPhoto(self, url: str) -> None:
        file = self.openFile('a')
        file.write(url)
        self.closeFile(file)

    def createList(self) -> List[str]:
        """Creates a list of urls for creating images later."""
        file = self.openFile()
        urls = file.read().split('\n')
        urls = [url for url in urls if url]
        
        return urls

    def loadImages(self) -> None:
        """Creates images using list of urls."""
        urls = self.createList()

        for url in urls:
            try:
                image = open(f'{urls.index(url)}.jpg', 'wb')
                image.write(urllib.request.urlopen(url).read())
                image.close()
            except: pass
            else: continue

    def getCountOfImages(self) -> int:
        """Returns number of pictures."""
        urls = self.createList()

        return len(urls)