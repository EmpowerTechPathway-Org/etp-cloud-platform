# Fictional IT ticket classifier example

def classify_ticket(text):

    text = text.lower()

    if "vpn" in text or "wifi" in text or "network" in text:
        return "Network Issue"

    if "password" in text or "login" in text:
        return "Access Request"

    if "error" in text or "crash" in text:
        return "Application Error"

    if "printer" in text or "laptop" in text:
        return "Device Problem"

    return "General Support"


tickets = [
    "VPN connection failing for remote user",
    "Doctor cannot login to scheduling system",
    "Clinic printer not responding",
    "Application crashes when opening"
]

for t in tickets:
    print(t, "->", classify_ticket(t))
