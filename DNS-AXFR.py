#!/usr/bin/env python3

# Dependencies:
# python3-dnspython

# Used Modules:
import dns.zone as dz
import dns.query as dq
import dns.resolver as dr
import argparse

# Initialize Resolver-Class from dns.resolver as "NS"
NS = dr.Resolver()

# Target domain
Domain = 'inlanefreight.com'

# Set the nameservers that will be used
NS.nameservers = ['ns1.inlanefreight.com', 'ns2.inlanefreight.com']

# List of found subdomains
Subdomains = []

# Define the AXFR Function
def AXFR(domain, nameserver):

        # Try zone transfer for given domain and namerserver
		# Perform the zone transfer
        # If zone transfer was successful
        # Add found subdomains to global 'Subdomain' list
        # If zone transfer fails

# Main
if __name__=="__main__":

        # For each nameserver
        # Try AXFR
        # Print the results
        # Print each subdomain
