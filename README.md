## Overview

## Setup
1. install docker
2. ensure nvidia container toolkit is installed (should be there already)

## Execute
1. Replace LOCAL_PATH_OF_YOUR_CONTENT_DIR in .env with your content directory
2. `docker-compose build`
3. `docker-compose up -d`
4. `docker-compose exec image_processor bash`
5. `python3 classify.py`
6. to leave the image, Run: `exit`