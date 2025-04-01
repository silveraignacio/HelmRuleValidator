import sys
import yaml
import os

def process_prometheus_rules(input_file):
    # Remove the file extension
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}-promtool.yaml"

    with open(input_file, 'r') as f:
        documents = list(yaml.safe_load_all(f))

    prometheus_rules = []

    for doc in documents:
        if isinstance(doc, dict) and doc.get("kind") == "PrometheusRule":
            prometheus_rules.append(doc)

    if not prometheus_rules:
        print(f"No valid PrometheusRule found in {input_file}. Skipping...")
        return

    output_data = {"groups": []}

    for rule in prometheus_rules:
        output_data["groups"].extend(rule.get("spec", {}).get("groups", []))

    with open(output_file, 'w') as f:
        yaml.dump(output_data, f, default_flow_style=False)

    print(f"Processed {input_file} -> {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: helmrulevalidator.py <file1> <file2> ...")
        sys.exit(1)

    for file in sys.argv[1:]:
        if os.path.exists(file):
            process_prometheus_rules(file)
        else:
            print(f"File not found: {file}")