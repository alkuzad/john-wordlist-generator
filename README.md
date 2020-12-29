# Cracking prefix/suffix based passwords

1. Fill prefixes and suffixes sets in code with predicted strings, order matters (mostly used first)
2. Download jumbo version of John from <https://www.openwall.com/john/>
3. Generate wordlist using wordlist.py
4. For SSH, use `ssh2john.py ~/.ssh/key > ssh.hash` to convert private key to john's hash format
5. If hash file is generated with 2 lines, remove first one (some old scripts do that)
6. Start john from `run` folder - `.\john.exe --format=ssh --session=ssh -wordlist=C:\wordlist-generated.txt ssh.hash`