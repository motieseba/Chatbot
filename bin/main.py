from src.chatbot import *
from src.cli_handler import *
from src.command_handler import *
from src.csvdata_handler import *

def main():
    args = parse_arguments()
    chatbot = Chatbot(args.data_file,args)
    chatbot.run_chatbot()

if __name__ == "__main__":
    main()