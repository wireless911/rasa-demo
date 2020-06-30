FROM wireless911/jre-python:1.0
WORKDIR /code
RUN chmod 755 -R /code
COPY requirements.txt /code/
RUN pip install --upgrade pip \
    && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
COPY . /code/
ENTRYPOINT ["rasa", "run","-m " ,models","--enable-api","--log-file", out.log","--auth-token", thisismysecret"]
