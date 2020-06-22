import os
from src import google_tts as tts

if os.environ['GOOGLE_APPLICATION_CREDENTIALS']:
    print("using credential: " + os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
else:
    print("No google cloud credential specified, cannot reach google api.")


def main():
    mp3file = tts.get_mp3(
        "白皮书说，党的十八大以来，中国的核安全事业进入安全高效发展的新时期。在核安全观引领下，中国逐步构建起法律规范、行政监管、行业自律、技术保障、人才支撑、文化引领、社会参与、国际合作等为主体的核安全治理体系，核安全防线更加牢固。",
        name="cmn-CN-Wavenet-B"
    )
    os.system("start " + mp3file)
    # tts.list_voices("zh-CN")


if __name__ == "__main__":
    main()
