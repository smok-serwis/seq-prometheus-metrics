seq-prometheus-metrics
======================

This is a tool (and a [Docker container](https://hub.docker.com/repository/docker/smokserwis/seq-prometheus-metrics))
to grab metrics from your [Seq](https://datalust.co/seq)
instance and output them to Prometheus.

Environment variables you need to take care of:

* _SEQ_ADDRESS_ - address of the Seq server. Default is `http://localhost:80/`
* _SEQ_API_KEY_ - if authentication is enabled, this will be required access API key. Remember to assign it correct permissions!
* _BIND_ADDRESS_ - interface to bind the Prometheus metric server. Default is _0.0.0.0_
* _BIND_PORT_ - port number to bind. Default is _80_

**Please note that you will have to change either _SEQ_ADDRESS_ or _BIND_PORT_ since the program will happily try to read it's own Prometheus output.**
