import os
from src import tts

print("using credential: " + os.environ['GOOGLE_APPLICATION_CREDENTIALS'])


def main():
    mp3file = tts.get_mp3("所以才想着来找你问问")
    os.system("start " + mp3file)


if __name__ == "__main__":
    main()
