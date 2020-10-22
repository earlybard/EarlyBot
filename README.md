# EarlyBot

Telegram bot for generating [textgenrnn](https://github.com/minimaxir/textgenrnn) text snippets from a given dataset.

## Setup
 - Install python3
 - pip install -r requirements.txt
 - OPTIONAL for GPU support
    - Install these: https://www.tensorflow.org/install/gpu
        - CUDA Toolkit
            - https://developer.nvidia.com/cuda-toolkit-archive
            - CUDA Toolkit 10.1 
            - Direct link: https://developer.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.105_418.96_win10.exe
        - CuDNN
            - https://developer.nvidia.com/cudnn
            - "Download cuDNN v7.6.5 (November 5th, 2019), for CUDA 10.1"
            - "cuDNN Library for Windows 10" 
        - Add CuDNN to your path
            - Start
            - Edit the system environment variables
            - Environment Variables...
            - Double click "Path"
            - New
            - Add wherever you extracted CuDNN
                - "C:\Users\Dylan\Downloads\cudnn-10.1-windows10-x64-v7.6.5.32\cuda\bin"

## Run
 - Create a Telegram bot: https://core.telegram.org/bots#6-botfather 
 - Insert your bot's key into main.py
 - python3 main.py <your-bot-key>
