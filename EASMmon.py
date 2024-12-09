import os
domain=input("Give the Domain:")
url = f"https://{domain}"
#runs final recon
os.system(f"python3 finalrecon.py --headers --sslinfo --whois --crawl --dns --sub --dir --wayback --ps --full -r -s {url}")
#runs Sws-recon
os.system(f"python3 SWS-Recon.py -d {domain} -o -A --whois -D --spoof -a --dork -s -p --subtake --ssl -jl -t -c -b -w --hunt -r --email")


