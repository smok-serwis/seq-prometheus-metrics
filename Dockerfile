FROM python:3.8

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache

WORKDIR /app
ADD seq_prometheus_metrics /app/seq_prometheus_metrics

ENV SEQ_ADDRESS="http://localhost:80"
ENV BIND_ADDRESS="0.0.0.0"
ENV BIND_PORT="80"

CMD ["python", "-m", "seq_prometheus_metrics.run"]