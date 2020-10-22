from textgenrnn import textgenrnn
import json

from src.DeepSteffen.allow_gpu_growth import allow_gpu_growth


class TelegramWeightsGenerator:
    """
    Generates textgenrnn weights based on a Telegram chat export.

    Running this with GPU support requires some extra steps.
    """

    TELEGRAM_JSON_EXPORT = "C:\\Users\\Dylan\\Downloads\\Telegram Desktop\\ChatExport_2020-10-22\\result.json"
    USER = "Dylan Jenkins"

    def __init__(self):

        allow_gpu_growth()

        with open(self.TELEGRAM_JSON_EXPORT, encoding='utf-8') as json_export:
            data = json.load(json_export)

        messages = data['messages']

        chosen_messages = []

        for message in messages:
            if message['type'] == 'message' \
                    and message['text'] \
                    and type(message['text']) == str \
                    and message['from'] == self.USER \
                    and 'forwarded_from' not in message:
                chosen_messages.append(message['text'])

        textgen = textgenrnn(name="telegram")

        textgen.train_on_texts(chosen_messages,
                               # Total number of iterations. More isn't always better! Deep Steffen used 150~
                               num_epochs=100,
                               # Uncomment this if you're using a GPU to speed things up considerably.
                               # batch_size=1024,
                               # How many epochs between each preview.
                               gen_epochs=10,
                               # How many epochs between saving out weights.
                               save_epochs=10,
                               # Max length of output sentences.
                               max_gen_length=100
                               )


if __name__ == '__main__':
    TelegramWeightsGenerator()
