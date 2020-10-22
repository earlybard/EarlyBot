from textgenrnn import textgenrnn
import json
import tensorflow as tf


class TelegramWeightsGenerator:
    """
    Generates textgenrnn weights based on a Telegram chat export.

    Running this with GPU support requires some extra steps.
    """

    TELEGRAM_JSON_EXPORT = "C:\\Users\\Dylan\\Downloads\\Telegram Desktop\\ChatExport_2020-09-28\\result.json"
    USER = "Dylan Jenkins"

    def __init__(self):

        with open(self.TELEGRAM_JSON_EXPORT, encoding='utf-8') as json_export:
            data = json.load(json_export)

        gpus = tf.config.experimental.list_physical_devices('GPU')
        if gpus:
            try:
                for gpu in gpus:
                    # I need more VRAM to not use this.
                    tf.config.experimental.set_memory_growth(gpu, True)
            except RuntimeError as e:
                print(e)

        messages = data['messages']

        chosen_messages = []

        for message in messages:
            if message['type'] == 'message' \
                    and message['text'] \
                    and type(message['text']) == str \
                    and message['from'] == self.USER \
                    and 'forwarded_from' not in message:
                chosen_messages.append(message['text'])

        textgen = textgenrnn(name="my-generated-weights")

        textgen.train_on_texts(chosen_messages,
                               # Total number of iterations. More isn't always better!
                               num_epochs=100,
                               # Might need to reduce this on a worse GPU.
                               batch_size=1024,
                               # How many epochs between each preview.
                               gen_epochs=10,
                               # Max length of output sentences.
                               max_gen_length=100,
                               # How many epochs between saving out weights.
                               save_epochs=10)


if __name__ == '__main__':
    TelegramWeightsGenerator()
