import dns.resolver
 
hosts = ["oreilly.com", "yahoo.com", "google.com", "microsoft.com", "cnn.com"]

for host in hosts:
    print(host)
    ip = dns.resolver.query(host, "A") # .query() method DEPRECATED -> use .resolve() instead
   # ip = dns.resolver.resolve(host, rdtype="A") # the new way to query
    for i in ip:
        print(i)
