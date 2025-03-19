# GCP VM Auto-Scaling Setup using Python

## Overview
This repository contains a Python script that automates the creation of a VM instance on Google Cloud Platform (GCP) and configures auto-scaling policies based on CPU utilization. It also implements security measures such as IAM roles and firewall rules.

## Features
- **Automated VM creation** using Google Cloud API
- **Auto-scaling configuration** based on CPU usage
- **Security implementation** with IAM roles and firewall rules
- **Deployment scripts** for setting up and managing instances

## System Requirements
- **Python 3.6+**
- **Google Cloud SDK** (`pip install google-api-python-client`)
- **IAM permissions** to create and manage instances
- **A configured GCP project with billing enabled**

## Deployment Guide

### 1. Clone the Repository
```bash
git clone https://github.com/aishwarya0408/VCC_Assignment2.git
cd VCC_Assignment2
```

### 2. Run the Script
Execute the Python script to create a VM instance:
```bash
python3 vm_test.py
```

### 3. Monitor VM and Auto-Scaling
To check the status of your VM:
- **GCP Console:** Compute Engine → VM Instances
- **GCloud CLI:**
  ```bash
  gcloud compute instances list
  ```
- **Monitor auto-scaling:**
  ```bash
  gcloud compute instance-groups managed describe my-mig
  ```


## Expected Outcome
| Scenario | Expected Result |
|----------|----------------|
| VM created | Instance appears in GCP console |
| Auto-scaling enabled | New instances spawn based on CPU threshold |
| Security policies applied | Restricted access with IAM roles and firewall |
| VM deletion | Instance removed successfully |

## Troubleshooting

### 1. **Instance Creation Fails**
- Ensure GCP credentials are correct:
  ```bash
  gcloud auth list
  ```
- Check if project ID is set:
  ```bash
  gcloud config list
  ```

### 2. **Auto-Scaling Not Triggering**
- Verify auto-scaler policy:
  ```bash
  gcloud compute instance-groups managed describe my-mig
  ```
- Ensure CPU utilization metric is enabled in **Cloud Monitoring**.

### 3. **Firewall or Access Issues**
- List active firewall rules:
  ```bash
  gcloud compute firewall-rules list
  ```
- Modify firewall to allow required traffic:
  ```bash
  gcloud compute firewall-rules create allow-http --allow=tcp:80 --target-tags=http-server
  ```

## Repository Structure
```
/
├── vm_test.py   # Python script for VM creation
├── README.md      # Documentation and setup guide
└── .gitignore     # Ignore sensitive files
```

## License
MIT License

