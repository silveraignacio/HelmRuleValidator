# **HelmRuleValidator**  

**HelmRuleValidator** is a command-line tool designed to validate Prometheus rules defined in Helm chart templates. It ensures that alerting rules are correctly formatted, free of duplicates, and compatible with `promtool`. This helps maintain consistency and prevent issues in Kubernetes monitoring setups.  

## **Features**  

- ✅ **Converts** Prometheus rules from Helm chart templates into a `promtool`-compatible format.  
- ✅ **Processes multiple files** separately to maintain modularity.  
- ✅ **Removes duplicate rules** to prevent inconsistencies.  
- ✅ **Easily integrates** into CI/CD pipelines like GitLab CI.  

## **Installation**  

### **Requirements**  

- Python **3.8+**  
- `pyyaml` (for YAML file processing)  
- `promtool` (included in [Prometheus](https://prometheus.io/download/))  

### **Install dependencies**  

```sh
pip install pyyaml
```

To ensure `promtool` is installed, run:  

```sh
promtool --version
```

If it's not installed, download Prometheus from [here](https://prometheus.io/download/).  

## **Usage**  

Before using HelmRuleValidator, ensure your Helm chart has already been rendered with values applied. **This tool does not process raw Helm templates; it works with fully rendered YAML files.**  

### **Step 1: Generate Prometheus rule files**  

Run the script with one or more input files:  

```sh
python helm_rule_validator.py file1.yaml file2.yaml
```

This generates output files:  

```sh
file1-promtool.yaml  
file2-promtool.yaml  
```

Each output file is formatted for `promtool` validation.  

### **Step 2: Validate with promtool**  

```sh
promtool check rules file1-promtool.yaml
```

If any issues are found, `promtool` will report them.  

## **Contributing**  

Contributions are welcome! Open an issue or submit a pull request to improve **HelmRuleValidator**.  

---  
