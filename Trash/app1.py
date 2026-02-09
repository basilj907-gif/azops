from flask import Flask, jsonify
from Trash.cost_client import fetch_vm_cost
 
app = Flask(__name__)
 
@app.route("/cost/vms", methods=["GET"])
def get_vm_cost():
    data = fetch_vm_cost()
 
    columns = [c["name"] for c in data["properties"]["columns"]]
    rows = data["properties"]["rows"]
 
    results = []
 
    print("\n===== PARSED VM COST OUTPUT =====")
    for row in rows:
        record = dict(zip(columns, row))
        vm_cost = {
            "vm_name": record.get("ResourceName"),
            "resource_type": record.get("ResourceType"),
            "cost": record.get("PreTaxCost"),
            "currency": record.get("Currency")
        }
 
        # 🔹 PRINT EACH VM COST
        print(vm_cost)
 
        results.append(vm_cost)
 
    return jsonify(results)
 
if __name__ == "__main__":
    app.run(debug=True)