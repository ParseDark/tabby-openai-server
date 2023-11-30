# tabby-openai-server

tabby-openai-server is the openai backend implementation of [Tabby](https://github.com/TabbyML/tabby), using the latest
gpt-4 to complete code.

## usage

### Server

```bash
# install requirements
python3 -m pip install -r requirements.txt

# run
base_url="https://xxxx.us/v1" api_key="sk-xxxx" python3 ./main.py
```

### Docker
```bash

# build local image 
docker build -t tabby-openai-server:latest .

# run local image 
docker run -d --name tabby-openai -p 8080:8080 -e base_url="https://xxx.com/v1" -e api_key="sk-xxxx"  tabby-openai-server:latest
```

### IDE Extensions

see https://tabby.tabbyml.com/docs/extensions
