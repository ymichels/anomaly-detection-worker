# CloudTrail Anomaly Detection Worker

## Overview
This Python script implements a worker for processing CloudTrail events from an SQS queue with the purpose of detecting anomalies. Anomalies in CloudTrail events could indicate potentially malicious activity or misconfigurations within an AWS environment.

The worker ensures that each event is processed only once to prevent duplication and provides a simple architecture for scalability.

## Prerequisites
- AWS IAM user with permissions to access the SQS queue and read messages.
- Python 3 installed on your system.
- Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration
1. Set up your AWS credentials and region by modifying the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_REGION` variables in the script.
2. Replace the value of `YOUR_QUEUE_URL` with the URL of your SQS queue.

## Usage
1. Clone this repository or copy the script `cloudtrail_anomaly_worker.py` to your project directory.
2. Run the script using Python:
    ```bash
    python app.py
    ```
This will start the worker which will process CloudTrail events from the SQS queue.

## Important Notes
- Ensure that the IAM user credentials used by the worker have the necessary permissions to read messages from the SQS queue and perform other required actions.
- Customize the `process_message` function to implement your anomaly detection logic based on CloudTrail events.
- Be cautious with scaling the number of worker threads. Consider the performance impact on your system and the rate at which events are generated in your AWS environment.

