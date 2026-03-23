import logging
import azure.functions as func
from azure.data.tables import TableClient
import os
import datetime

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False) 
def HealthMonitor(myTimer: func.TimerRequest) -> None:
    connection_string = os.getenv("AzureWebJobsStorage")
    
    # Connect to the table
    table_client = TableClient.from_connection_string(conn_str=connection_string, table_name="HealthAlerts")

    # --- THE SAFETY NET LINE ---
    try:
        table_client.create_table()
        logging.info("Table 'HealthAlerts' was missing, so I created it.")
    except Exception:
        # If table already exists, it will throw an error, we just ignore it
        pass

    # Create the alert
    new_alert = {
        "PartitionKey": "Nigeria",
        "RowKey": str(datetime.datetime.now().timestamp()),
        "Disease": "Meningitis",
        "Status": "Alert",
        "Message": "Live Cloud Test: Successful Connection."
    }

    table_client.create_entity(entity=new_alert)
    logging.info("Health Alert successfully uploaded to the Cloud!")