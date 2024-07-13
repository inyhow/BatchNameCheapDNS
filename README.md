# BatchNameCheapDNS
#Introduction
This project aims to provide a solution for batch modifying DNS records of NameCheap domains. It allows you to update multiple DNS records simultaneously, saving you time and effort.
#Prerequisites
Before using this script, make sure you have the following:
Python 3.x installed on your machine.
The namecheap library installed. You can install it using pip:

  pip install namecheap
#Usage
Clone or download this repository to your local machine.
Open the terminal or command prompt and navigate to the project directory.
Create a configuration file named config.ini and provide the necessary details. The file should have the following structure:

   [namecheap]
```python
   api_user = YOUR_API_USER
   api_key = YOUR_API_KEY
   username = YOUR_NAMECHEAP_USERNAME
   client_ip = YOUR_CLIENT_IP
```
   records_file = PATH_TO_RECORDS_FILE
Replace YOUR_API_USER, YOUR_API_KEY, YOUR_NAMECHEAP_USERNAME, YOUR_CLIENT_IP, and PATH_TO_RECORDS_FILE with your actual NameCheap API credentials, NameCheap username, client IP address, and the path to the file containing the DNS records to be modified.
Prepare a file containing the DNS records to be modified. Each record should be in the following format:

  ```bash
 domain.com A 192.168.0.1
```
   subdomain.domain.com CNAME anotherdomain.com
The file can contain multiple records, each on a new line.
Run the script using the following command:

```bash
   python dns_modifier.py
```

The script will read the DNS records from csv file, connect to the NameCheap API, and modify the DNS records accordingly.
##Notes
Make sure to review and verify the DNS records in the file before running the script to avoid unintended modifications.
This script uses the NameCheap API to modify DNS records. Ensure that you have the correct API credentials and permissions.
It is recommended to test the script on a small number of DNS records before applying it to a large number of records.
#License
This project is licensed under the MIT License.
For more information, please refer to the NameCheap API documentation.
Note: Remember to replace the placeholders (YOUR_API_USER, YOUR_API_KEY, YOUR_NAMECHEAP_USERNAME, YOUR_CLIENT_IP, PATH_TO_RECORDS_FILE) in the config.ini file and provide accurate instructions and details in the README.md file based on your specific project requirements.
