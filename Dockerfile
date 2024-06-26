FROM pytorch/pytorch:2.3.1-cuda12.1-cudnn8-devel

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    git-lfs \
    && rm -rf /var/lib/apt/lists/*
RUN pip install flash-attn --no-build-isolation

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
    
COPY . /app