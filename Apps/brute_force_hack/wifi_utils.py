import pywifi

def get_wifi_networks():
    wifi = pywifi.PyWiFi()
    # Get the Wi-Fi interface (usually the first one)
    iface = wifi.interfaces()[0]
    # Scan for available Wi-Fi networks
    iface.scan()
    # Get the scan results (a list of scanned Wi-Fi networks)
    scan_results = iface.scan_results()
    ret = {}
    # Print the details of each available network
    for result in scan_results:
        ret[result.ssid] = result
        # print(f"SSID: {result.ssid}, Signal Strength: {result.signal}, BSSID: {result.bssid}")
    return ret
