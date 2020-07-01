# rasa-demo
rasa项目链接到rasa-x的实例

# 训练
rasa train


# docker 构建镜像
```
docker build -t rasa/rasa-demo:v1 .
```

# docker 启动容器
```
docker run --name rasa-demo -d rasa/rasa-demo:v1
```


# docker 构建actions镜像
```
docker build . -t <account_username>/<repository_name>:<custom_image_tag>
eg:
docker build . --no-cache -t wireless911/rasa-demo:v1.0 
```
# docker 启动actions容器
```
docker run --name rasa-demo --privileged=true  -p 5055:5055 -v ./actions:/app/actions -d wireless911/rasa-demo:v1.0 
```

# docker 容器中训练模型
```
docker run -v $(pwd):/app rasa/rasa:1.10.3-full train --domain domain.yml --data data --out models

```