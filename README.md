## Overview

## Setup
1. install docker
2. install nvidia container toolkit
3. Run `docker build -t image_processor`

## Execute
1. Replace /path/to/content/folder in docker-compose.yml
2. Run `docker-compose up -d`
2. Run `docker-compose exec image_processor bash`
3. Run `python3 classify.py`
4. to leave the image, Run: `exit`