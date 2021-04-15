import sys

from .lib.main import authorize, bot, get_bot
from .lib.warns import BotNotFound, Unauthorized

def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "bot":
            if len(sys.argv) > 2:
                print(get_bot(sys.argv[2]))
            else:
                print("USAGE: python -m blackerz_wrapper bot [id]")
    else:
        print("-get bot information from id\npython -m blackerz_wrapper bot [id]")

if __name__ == "__main__":
    main()