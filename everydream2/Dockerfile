# Based off https://www.runpod.io/blog/diy-deep-learning-docker-container
FROM nvidia/cuda:11.6.2-cudnn8-devel-ubuntu20.04 

# Use bash shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV DEBIAN_FRONTEND noninteractive\
    SHELL=/bin/bash

# Install base utilities and Python 3.10
RUN apt-get update && apt-get upgrade -y && apt install software-properties-common -y && add-apt-repository ppa:deadsnakes/ppa && \
    apt-get install -y wget git python3.10-dev python3.10-venv curl zip unzip git-lfs tmux vim kbd openssh-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen

# Install runpodctl 
RUN wget https://github.com/runpod/runpodctl/releases/download/v1.9.0/runpodctl-linux-amd -O runpodctl && \
    chmod a+x runpodctl && \
    mv runpodctl /usr/local/bin

# Install pip for Python 3.10
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 0

# Install Pytorch 1.21.1 for CUDA 1.16
RUN pip install --no-cache-dir torch==1.12.1+cu116 torchvision==0.13.1+cu116 --extra-index-url https://download.pytorch.org/whl/cu116 

# Install required python modules,
# Install transformers and upgrade requests
# Install jupyter lab,
# Install xformers (shouldn't take too long since ninja is installed)
ADD requirements.txt .
RUN python3 --version && pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir transformers -i https://pypi.python.org/simple && \
    pip install --no-cache-dir requests --upgrade && \
    pip install --no-cache-dir jupyterlab && \
    pip install --no-cache-dir ipywidgets && \
    export FORCE_CUDA=1 && export TORCH_CUDA_ARCH_LIST=8.6 && CUDA_VISIBLE_DEVICES=0 && \
    pip install --no-cache-dir git+https://github.com/facebookresearch/xformers.git#egg=xformers

# Precache .cache with huggingface files
#RUN mkdir -p /root/.cache/huggingface/
#ADD cache/huggingface/* /root/.cache/huggingface/

# Add EveryDream repo, add damian0815 fork, assign a default user.email for quickfix merging
WORKDIR /
RUN git clone https://github.com/victorchall/EveryDream2trainer everydream2 && \
    cd everydream2 && \
    python3 utils/get_yamls.py && \
    git remote add damian0815 https://github.com/damian0815/EveryDream2trainer && \
    git config --global user.email "nobody@nowhere.no"

# Add welcome banner
ADD welcome-banner.txt /root/welcome-banner.txt
RUN echo "cat ~/welcome-banner.txt" >> ~/.bashrc

ADD start.sh /

RUN chmod +x /start.sh

CMD [ "/start.sh" ]
