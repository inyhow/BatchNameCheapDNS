import csv
import requests
import xml.etree.ElementTree as ET

# Namecheap API 配置
api_user = 'acount_name'
api_key = '111111592c47a091fb837c934e4382'
client_ip = '103.84.217.36' #modify your network ip
base_url = 'https://api.namecheap.com/xml.response'

def print_api_response(response, action):
    print(f"\n--- {action} API Response ---")
    print(f"Status Code: {response.status_code}")
    print("Response Content:")
    print(response.text)
    print("--- End of Response ---\n")


def clear_all_dns_records(domain):
    sld, tld = domain.split('.')[-2:]
    url = f"{base_url}?ApiUser={api_user}&ApiKey={api_key}&UserName={api_user}&ClientIp={client_ip}&Command=namecheap.domains.dns.setHosts&SLD={sld}&TLD={tld}"

    # 发送一个空的DNS记录集来清除所有记录
    response = requests.get(url)
    print_api_response(response, "Clear DNS Records")

    if response.status_code == 200:
        root = ET.fromstring(response.content)
        if root.attrib['Status'] == 'OK':
            print(f"Successfully cleared all DNS records for {domain}")
        else:
            print(f"Failed to clear DNS records for {domain}")
    else:
        print(f"Failed to clear DNS records for {domain}: HTTP {response.status_code}")


def add_a_record(domain, a_record_value):
    sld, tld = domain.split('.')[-2:]
    get_hosts_url = f"{base_url}?ApiUser={api_user}&ApiKey={api_key}&UserName={api_user}&ClientIp={client_ip}&Command=namecheap.domains.dns.getHosts&SLD={sld}&TLD={tld}"

    response = requests.get(get_hosts_url)
    print_api_response(response, "Get Hosts")

    if response.status_code == 200:
        root = ET.fromstring(response.content)
        if root.attrib['Status'] == 'OK':
            set_hosts_url = f"{base_url}?ApiUser={api_user}&ApiKey={api_key}&UserName={api_user}&ClientIp={client_ip}&Command=namecheap.domains.dns.setHosts&SLD={sld}&TLD={tld}"
            new_host_entries = (
                f'&HostName1=@&RecordType1=A&Address1={a_record_value}&TTL1=300'
                f'&HostName2=*&RecordType2=A&Address2={a_record_value}&TTL2=300'
            )
            set_hosts_url += new_host_entries

            update_response = requests.get(set_hosts_url)
            print_api_response(update_response, "Set Hosts")

            if update_response.status_code == 200:
                update_root = ET.fromstring(update_response.content)
                if update_root.attrib['Status'] == 'OK':
                    print(f"Successfully added A record and wildcard A record for {domain}")
                else:
                    print(f"Failed to update DNS for {domain}")
            else:
                print(f"Failed to update DNS for {domain}: HTTP {update_response.status_code}")
        else:
            print(f"Failed to get DNS records for {domain}")
    else:
        print(f"Failed to get DNS records for {domain}: HTTP {response.status_code}")


# 读取 CSV 文件
with open('domains.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        domain = row['domain']
        ip_address = row['ip']

        print(f"\nProcessing domain: {domain}")

        # 首先清除所有DNS记录
        clear_all_dns_records(domain)

        # 然后添加新的A记录
        add_a_record(domain, ip_address)
