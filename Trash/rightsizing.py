import math


def recommend_rightsizing(cpu_p95, current_vcpu, target_util=0.6):
    """
    Decide required vCPU based on P95 usage
    """
    required_vcpu = math.ceil(
        (cpu_p95 / 100) * current_vcpu / target_util
    )
 
    if required_vcpu < current_vcpu:
        action = "DOWNSIZE"
    elif required_vcpu > current_vcpu:
        action = "UPSCALE"
    else:
        action = "NO_CHANGE"
 
    return {
        "current_vcpu": current_vcpu,
        "required_vcpu": required_vcpu,
        "action": action
    }

if __name__ == "__main__":
    result = recommend_rightsizing(cpu_p95=42, current_vcpu=8)
    print(result)