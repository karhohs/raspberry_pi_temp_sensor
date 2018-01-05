FROM gpio_base:latest  

RUN mkdir -p /root/data

ADD ./data_logging_test.py ./data_logging_test.py

CMD ["python", "data_logging_test.py"]