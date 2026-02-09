import math
 
def recommend_rightsizing(cpu_p95, current_vcpu, target_util=0.6):
    required_vcpu = math.ceil((cpu_p95/100)*current_vcpu/target_util)
 
    if required_vcpu < current_vcpu:
        action = "DOWNSIZE"
    elif required_vcpu > current_vcpu:
        action = "UPSCALE"
    else:
        action = "NO_CHANGE"
 
    return {"required_vcpu": required_vcpu, "action": action}