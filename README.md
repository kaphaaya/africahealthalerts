# 🌍 Africa Health Alert: Resilient Cloud Monitoring System

### **The Mission**
A cloud-native, automated health monitoring system designed to track disease alerts (e.g., Meningitis in Nigeria). The goal was to build a system that is **Resilient**, **Secure**, and **Self-Healing**.

### **The Technical Win**
* **Self-Healing Logic:** Implemented a `try/except` block with `create_table()` to ensure the database auto-provisions if it is ever manually deleted.
* **Cloud Persistence:** Engineered a direct handshake between **Azure Functions** and **Azure Table Storage** (`africahealthdevab60`).
* **Security First:** Managed all connection strings via **Environment Variables** (`os.getenv`) to ensure zero-leak of sensitive keys to public repositories.

---

### **Tech Stack & Tools**
* **Language:** Python 3.x
* **Cloud Provider:** Microsoft Azure
* **Compute:** Azure Functions (Timer-Triggered every 5 minutes)
* **Database:** Azure Table Storage (NoSQL)
* **Deployment:** Azure Functions Core Tools (CLI)
* **Version Control:** Git & GitHub

---

### **System Architecture**
1.  **Trigger:** A CRON expression `0 */5 * * * *` fires the function every 5 minutes.
2.  **Logic:** The Python script checks for a connection to the Azure Storage Account.
3.  **Resilience:** If the `HealthAlerts` table doesn't exist, the code creates it on the fly.
4.  **Output:** A JSON payload containing the Country, Disease, and Timestamp is securely stored.

---

### **How to Deploy Locally**
1.  **Clone the repo:** `git clone https://github.com/kaphaaya/africahealthalerts.git`
2.  **Set up Environment:** ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
3.  **Configure Secrets:** Add your `AzureWebJobsStorage` connection string to `local.settings.json`.
4.  **Launch:** `func start`

