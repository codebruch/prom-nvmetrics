from prometheus_client import start_http_server, Summary, Gauge
import random
import time
import xml.etree.ElementTree as ET
import py3nvml.nvidia_smi as smi

#initialize GPUs to get dynamic name assignment for metric description
def initialize_gpus():
       smi.nvmlInit()
       print ("Driver Version: ", smi.nvmlSystemGetDriverVersion())
       out = smi.XmlDeviceQuery()
       root = ET.fromstring(out)
       for gpu in root.getiterator('gpu'):
           gpuName =(gpu.find('product_name').text)
           print('Found: ' + gpuName)
           gTemperature = Gauge('GPU_Temperature', 'Temperature of GPU: ' + gpuName, labelnames=['card'])
           gfan_speed = Gauge('GPU_fan_speed', 'Fan Speed of GPU: '+ gpuName, labelnames=['card'])
           gfb_memory_usage = Gauge('GPU_memory_usage', 'Memory usage of GPU: ' + gpuName, labelnames=['card'])
           gfb_memory_total = Gauge('GPU_memory_total', 'Total Memory usage of GPU: ' + gpuName, labelnames=['card'])
           ggraphics_clock = Gauge('GPU_graphics_clock', 'Graphics clock of GPU: ' + gpuName, labelnames=['card'])
           gmem_clock = Gauge('GPU_memory_clock', 'Memory clock of GPU: ' + gpuName, labelnames=['card'])
           gpower_draw = Gauge('GPU_power_draw', 'Power draw of GPU: ' + gpuName, labelnames=['card'])
           ggpu_util = Gauge('GPU_util', 'Utilization of GPU: ' + gpuName, labelnames=['card'])
       return  {'gTemperature': gTemperature, 'gfan_speed': gfan_speed,'gfb_memory_usage': gfb_memory_usage,
                'ggraphics_clock': ggraphics_clock, 'gpower_draw': gpower_draw, 'ggpu_util': ggpu_util,
                'gfb_memory_total': gfb_memory_total,'gmem_clock': gmem_clock}


def execute_and_read_from_SMI(metrics):
    """A dummy function that takes some time."""

    gTemperature = metrics.get('gTemperature', 'default')
    gfan_speed = metrics.get('gfan_speed', 'default')
    gfb_memory_usage = metrics.get('gfb_memory_usage', 'default')
    gfb_memory_total = metrics.get('gfb_memory_total', 'default')
    ggraphics_clock = metrics.get('ggraphics_clock', 'default')
    gpower_draw = metrics.get('gpower_draw', 'default')
    ggpu_util = metrics.get('ggpu_util', 'default')
    gmem_clock = metrics.get('gmem_clock', 'default')

    out = smi.XmlDeviceQuery()
    root = ET.fromstring(out)
    #print(out)
    for gpu in root.getiterator('gpu'):
        gpuName =(gpu.find('product_name').text)                  
        temperature=[float(gpu.find('temperature/gpu_temp').text.split()[0])]
        #print(temperature[0])
        gTemperature.labels(gpuName).set(temperature[0])

        fan_speed = [float(gpu.find('fan_speed').text.split()[0])]
        gfan_speed.labels(gpuName).set(fan_speed[0])

        
        fb_memory_usage = [1e6 * float(gpu.find('fb_memory_usage/used').text.split()[0])]
        gfb_memory_usage.labels(gpuName).set(fb_memory_usage[0])
        
        
        fb_memory_total = [1e6 * float(gpu.find('fb_memory_usage/total').text.split()[0])]
        gfb_memory_total.labels(gpuName).set(fb_memory_total[0])
        
       
        gpu_util = [float(gpu.find('utilization/gpu_util').text.split()[0])]
        ggpu_util.labels(gpuName).set(gpu_util[0])
     
        power_draw = [float(gpu.find('power_readings/power_draw').text.split()[0])]
        #print(power_draw)
        gpower_draw.labels(gpuName).set(power_draw[0])

        
        graphics_clock = [float(gpu.find('clocks/graphics_clock').text.split()[0])]
        ggraphics_clock.labels(gpuName).set(graphics_clock[0])
        

        mem_clock = [float(gpu.find('clocks/mem_clock').text.split()[0])]
        gmem_clock.labels(gpuName).set(mem_clock[0])




if __name__ == '__main__':
    #initialize the metrics from GPU
    metrics = initialize_gpus()
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        print('sleep')
        time.sleep(0.3)
        print('update metrics')
        execute_and_read_from_SMI(metrics)
        
        
