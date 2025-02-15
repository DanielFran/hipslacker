"""
    Copyright 2018 the original author or authors from the Hipslacker project.

    This file is part of the JHipster project, see https://www.jhipster.tech/
    for more information.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# load environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
BOT_ID = os.getenv('BOT_ID', '')
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN', '')
JHIPSTER_ONLINE_USER = os.getenv('JHIPSTER_ONLINE_USER', '')
JHIPSTER_ONLINE_PWD = os.getenv('JHIPSTER_ONLINE_PWD', '')
LOGGER_FORMAT = os.getenv('LOGGER_FORMAT', '')
READ_WEBSOCKET_DELAY = int(os.getenv('READ_WEBSOCKET_DELAY', ''))
AT_BOT = os.getenv('AT_BOT', '')
