import dns.resolver

hosts = ["oreilly.com", "yahoo.com", "google.com", "microsoft.com", "cnn.com"]

for host in hosts:
    print(f"""
###################
#  {host}{(14 - len(host)) * ' '} #
###################
""")
    ip = dns.resolver.resolve(host, "A")
    for i in ip:
        print(f"IP: {i}")
