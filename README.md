## Overview

## Setup
1. install docker
2. install nvidia container toolkit
3. Run `docker build -t image_processor`

## Execute
1. `CONTENT_DRIVE=/path/to/your_base_folder_to_classify docker-compose up -d`
2. `docker-compose exec image_processor bash`
3. python3 classify.py