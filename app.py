from flask import Flask, jsonify
from cost_client import query_vm_cost
 
app = Flask(__name__)
 
@app.route("/cost/vms", methods=["GET"])
def get_vm_cost():
    data = query_vm_cost(timeframe="MonthToDate")
 
    # Parse rows safely
    columns = [c["name"] for c in data["properties"]["columns"]]
    rows = data["properties"]["rows"]
 
    results = []
    for r in rows:
        row = dict(zip(columns, r))
        results.append({
            "vm_name": row.get("ResourceName"),
            "resource_type": row.get("ResourceType"),
            "cost": row.get("PreTaxCost"),
            "currency": row.get("Currency")
        })
 
    return jsonify(results)
 
if __name__ == "__main__":
    app.run(debug=True)