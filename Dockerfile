FROM centos/python-38-centos7
WORKDIR /app
COPY . .
RUN pip3 install pipenv
RUN pipenv install
ENTRYPOINT [ "python3" ]
CMD ["app.py"]