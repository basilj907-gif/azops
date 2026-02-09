from pipeline.run_pipeline import run_pipeline
import time
 
while True:
    result = run_pipeline("vm-101")
    print(result)
    time.sleep(300)