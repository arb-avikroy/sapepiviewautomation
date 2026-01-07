# SAP Enterprise Portal iView Creation Automation
iView creation automation using Python and XML - XML Content and Actions

This project automates the mass creation of **SAP Portal URL iViews** . It uses Python to transform data from an Excel sheet into SAP's proprietary `GenericCreator` XML format.

## 🌟 Features
- **Mass Creation:** Generate 100+ iViews in matter of few minutes (Complete Workflow)
- **Optimized UI:** Configured to open in a separate window without Portal overhead (Headerless).
- **Audit Ready:** By default, iViews are tracked by SAP Portal Activity Reportsu (PAR) if they are active in the system. They can be configured and tracked in custom PARs.
- **Robust Parsing:** Automatically handles XML reserved characters (like `&` in URLs).

---

## 🛠️ 1. Environment Setup

### Install Python
1. Download and install Python from [Python.org](https://www.python.org/).
2. During installation, ensure you check the box **"Add Python to PATH"**.
Also, Add Python from Microsoft Store (in Windows)

### Setup Visual Studio Code (VS Code)
1. Open VS Code.
2. Install the **Python Extension** (by Microsoft) from the Extensions Marketplace.
3. Open the project folder.

### Check Python version
Open the VS Code terminal (`Ctrl + ` `) and run:
Check version
```bash
python --version
```
### Check Python version

### Install Required Libraries
Open the VS Code terminal (`Ctrl + ` `) and run:
```bash
pip install pandas openpyxl
```
### 2. Excel Data Structure 
Prepare an Excel file named PortalXML.xlsx (any name, need to modify in the python code before running) in the root folder with the following columns:
ID -> Title -> URL  

### 3. Python Script
In git

### 4. Execution & Upload
-- Run Script: In VS Code, run python generate_portal.py.
-- Locate File: A file named portal_upload.xml will appear in your folder.
-- Login to SAP Portal: Go to System Administration > Transport > XML Content and Actions.
-- Import:
-- Click the Browse button.
-- Select portal_upload.xml.
-- Click Upload.
-- Verify: Check the log for "Status: Success" and find your new iViews in the Portal Content Studio.

### Important Notes
-- Closing Excel: The script will fail with a Permission Denied error if the Excel file is open while running the script.
-- PCD Permissions: After creation, ensure you assign End-User Permissions to the folder in Portal Content Studio so users can see the links.
-- HTTPS: Ensure all URLs start with https:// to avoid browser security blocks (Mixed Content).


### Files:
Excel example as Source 
Python script to create XML from Excel Sheet
Example XML as Output Created to be uploaded in XML Content and Actions
