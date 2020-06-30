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