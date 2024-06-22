## Overview

## Setup
1. install docker
2. install nvidia container toolkit

## Execute
1. Replace /path/to/content/folder in docker-compose.yml
2. `docker-compose build`
3. `docker-compose up -d`
4. `docker-compose exec image_processor bash`
5. `python3 classify.py`
6. to leave the image, Run: `exit`