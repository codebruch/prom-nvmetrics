# A prometheus exporter for metrics NVIDIA based GPUs
* Inofficial no affiliation with NVIDIA
* For usage in a grafana https://grafana.com/ + prometheus https://prometheus.io/ monitoring setup
* Uses py3nvml https://github.com/fbcotter/py3nvml
* Tested on windows
* No multi GPUs yet tested

## Dependencies:
* python 3.x ( tested on 3.5 )
* pip install py3nvml
* pip install prometheus_client

## Supported metrics
* Temperature of GPU
* Fan Speed of GPU
* Memory usage
* Total Memory
* Graphics clock
* Memory clock
* Utilization of GPU
* Power draw

More can be added simply

## Usage
* Start it like python prom_nvmetrics.py
* It will listen on port 8000 per default, metrics available at http://localhost:8000/metrics
* Use you prometheus + grafana setup to add it and build a nice dashboard

