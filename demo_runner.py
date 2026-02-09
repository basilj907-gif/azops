import pandas as pd
from pipeline import run_pipeline   # adjust if pipeline file name differs

CONFIG_PATH = "Data/vm_config.xlsx"

def run_all_vms():

    # Load VM list from config
    config_df = pd.read_excel(CONFIG_PATH)

    vm_ids = config_df["vm_id"].tolist()

    all_results = []

    for vm in vm_ids:
        try:
            result = run_pipeline(vm)
            all_results.append(result)

            print("\n----------------------------")
            print(f"VM: {vm}")
            print(result)

        except Exception as e:
            print(f"Error processing {vm}: {e}")

    return all_results


if __name__ == "__main__":
    results = run_all_vms()

    print("\n============================")
    print("FINAL AGGREGATED RESULTS")
    print("============================")
    print(results)
