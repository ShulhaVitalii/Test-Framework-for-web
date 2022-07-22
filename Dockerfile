FROM joyzoursky/python-chromedriver:3.9-selenium

ENV INSIDE_DOCKER True

WORKDIR /web_tests/

COPY docker_setup.sh .

RUN bash docker_setup.sh

COPY requirements.txt .

RUN pip3 install -r requirements.txt

CMD python -m pytest -s --alluredir=test_result/ /web_tests/tests
