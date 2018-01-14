#A prometheus exporter for metrics Nvidia based GPUs
*For usage in a grafana + prometheus monitoring setup
*Tested on windows
*No multi GPUs yet tested

##Dependencies:
*pip install py3nvml
*pip install prometheus_client

##Supported metrics
*Temperature of GPU
*Fan Speed of GPU
*Memory usage
*Total Memory
*Graphics clock
*Memory clock
*Utilization of GPU
*Power draw

More can be added simply

##Usage
*Start it like python prom_nvmetrics.py
*It will listen on port 8000 per default, metrics available at http://localhost:8000/metrics
*Use you prometheus + grafana setup to add it and build a nice dashboard

