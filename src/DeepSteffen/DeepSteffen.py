from textgenrnn import textgenrnn
from typing import List

from src.DeepSteffen.allow_gpu_growth import allow_gpu_growth


class DeepSteffen:

    textgen = None

    def __init__(self):
        self.textgen = textgenrnn("Generator/telegram_weights.hdf5")

    def generate_samples(self):
        self.textgen.generate_samples()

    def generate(self, prefix=None, temperature=None) -> List[str]:
        """
        Generates sentences from a textgenrnn weights file.

        :param prefix: Optionally hard-code the start of the sentence to generate.
        :param temperature: How "creative" the sentence should be. 0.5 is average.
        :return: The generated sentence.
        """

        if prefix and temperature:
            print("both")
            return self.textgen.generate(return_as_list=True, max_gen_length=100, temperature=temperature, prefix=prefix)
        elif prefix:
            print("prefix")
            return self.textgen.generate(return_as_list=True, max_gen_length=100, prefix=prefix)
        elif temperature:
            print("temp")
            return self.textgen.generate(return_as_list=True, max_gen_length=100, temperature=temperature)
        else:
            print("neither")
            return self.textgen.generate(return_as_list=True, max_gen_length=100)


if __name__ == '__main__':
    allow_gpu_growth()
    DeepSteffen().generate_samples()
