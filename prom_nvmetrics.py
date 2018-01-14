from prometheus_client import start_http_server, Summary, Gauge
import random
import time
import xml.etree.ElementTree as ET
import py3nvml.nvidia_smi as smi

gTemperature = Gauge('GPU_Temperature', 'Description of gauge')
gfan_speed = Gauge('GPU_fan_speed', 'Fan Speed of GPU: ')
gfb_memory_usage = Gauge('GPU_memory_usage', 'Memory usage of GPU: ')

# Create a metric to track time spent and requests made.
#REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
#@REQUEST_TIME.time()
def execute_and_read_from_SMI(t):
    """A dummy function that takes some time."""
    #time.sleep(t)
    #si = subprocess.STARTUPINFO()
    #si.dwFlags =  subprocess.SW_HIDE
    #out = subprocess.Popen(['C:\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe', '-q', '-x'  ], stdout=subprocess.PIPE, shell=False, startupinfo=si).communicate()[0]
    out = smi.XmlDeviceQuery()
    root = ET.fromstring(out)
    print(out)
    for gpu in root.getiterator('gpu'):
        gpuName =(gpu.find('product_name').text)
        print(gpuName)
        #gTemperature
        temperature=[float(gpu.find('temperature/gpu_temp').text.split()[0])]
        print(temperature[0])
        gTemperature.set(temperature[0])

        fan_speed = values=[float(gpu.find('fan_speed').text.split()[0])]
        gfan_speed.set(fan_speed[0])

        #       vl.dispatch(type='memory', type_instance='used',
        fb_memory_usage = values=[1e6 * float(gpu.find('fb_memory_usage/used').text.split()[0])]
        gfb_memory_usage.set(fb_memory_usage[0])
        
        #        vl.dispatch(type='memory', type_instance='total',
        fb_memory_total = values=[1e6 * float(gpu.find('fb_memory_usage/total').text.split()[0])]

        #        vl.dispatch(type='percent', type_instance='gpu_util',
        gpu_util = values=[float(gpu.find('utilization/gpu_util').text.split()[0])]
        #       vl.dispatch(type='power', type_instance='draw',
        power_draw = values=[float(gpu.find('power_readings/power_draw').text.split()[0])]


        #        vl.dispatch(type='cpufreq', type_instance='graphics_clock',
        graphics_clock = values=[float(gpu.find('clocks/graphics_clock').text.split()[0])]

        #vl.dispatch(type='cpufreq', type_instance='sm_clock',
        sm_clock = values=[float(gpu.find('clocks/sm_clock').text.split()[0])]

        #vl.dispatch(type='cpufreq', type_instance='mem_clock',
        mem_clock = values=[float(gpu.find('clocks/mem_clock').text.split()[0])]





if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        time.sleep(2)
        execute_and_read_from_SMI(random.random())
        
