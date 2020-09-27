#!/usr/bin/env python3
import os
import pyttsx3
import PyPDF2
import urllib.request
from google_speech import Speech


class Reader:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 130)
        self.engine.setProperty("volume", 2.0)
        # Changing Voice
        self.engine.setProperty("voice", "en-german-5")

    def contentReader(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def isOnline(self):
        host = "https://google.com"
        try:
            urllib.request.urlopen(host)  # Python 3.x
            return True
        except:
            return False

    def bookText(self, bookPath):
        if os.path.exists(bookPath):
            with open(bookPath, "rb") as file:
                pdf = PyPDF2.PdfFileReader(file)
                totalPages = pdf.getNumPages()
                pg = int(input(f"Enter page no. to read (1-{totalPages}): "))
                text = pdf.getPage(pg - 1).extractText()
                # print(text)
                if self.isOnline():
                    tts = Speech(text, "en")
                    tts.play()
                else:
                    print("Go Online for a better audio experience")
                    self.contentReader(text)
        else:
            print(f"Sorry no file found at {bookPath}")


def main():
    reader = Reader()
    pathToPdf = input("Enter the full path to the PDF: ")
    reader.bookText(pathToPdf)


if __name__ == "__main__":
    main()
