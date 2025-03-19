import googleapiclient.discovery
import googleapiclient.errors
import time

def create_instance(compute, project, zone, name):
    """
    Creates a new VM instance on GCP.
    """
    config = {
        "name": name,
        "machineType": f"zones/{zone}/machineTypes/e2-medium",
        "disks": [
            {
                "boot": True,
                "autoDelete": True,
                "initializeParams": {
                    "sourceImage": "projects/debian-cloud/global/images/debian-11"
                },
            }
        ],
        "networkInterfaces": [
            {
                "network": "global/networks/default",
                "accessConfigs": [{"type": "ONE_TO_ONE_NAT", "name": "External NAT"}]
            }
        ],
        "metadata": {
            "items": [
                {
                    "key": "startup-script",
                    "value": "#!/bin/bash\napt-get update && apt-get install -y nginx"
                }
            ]
        }
    }
    try:
        operation = compute.instances().insert(project=project, zone=zone, body=config).execute()
        wait_for_operation(compute, project, zone, operation["name"])
        print(f"Instance {name} created successfully.")
    except googleapiclient.errors.HttpError as err:
        print(f"Error creating instance: {err}")

def delete_instance(compute, project, zone, name):
    """
    Deletes the specified VM instance from GCP.
    """
    try:
        operation = compute.instances().delete(project=project, zone=zone, instance=name).execute()
        wait_for_operation(compute, project, zone, operation["name"])
        print(f"Instance {name} deleted successfully.")
    except googleapiclient.errors.HttpError as err:
        print(f"Error deleting instance: {err}")

def wait_for_operation(compute, project, zone, operation):
    """
    Waits for an operation to complete before continuing.
    """
    print("Waiting for operation to complete...")
    while True:
        result = compute.zoneOperations().get(project=project, zone=zone, operation=operation).execute()
        if result["status"] == "DONE":
            if "error" in result:
                print(f"Error during operation: {result['error']}")
            return result
        time.sleep(5)

def main():
    project = "your-gcp-project-id"
    zone = "us-central1-a"
    instance_name = "vm-instance"
    compute = googleapiclient.discovery.build("compute", "v1")
    
    print("Creating instance...")
    create_instance(compute, project, zone, instance_name)
    
    # Uncomment the following lines if you want to delete the instance after some time
    # time.sleep(60)
    # print("Deleting instance...")
    # delete_instance(compute, project, zone, instance_name)

if __name__ == "__main__":
    main()
