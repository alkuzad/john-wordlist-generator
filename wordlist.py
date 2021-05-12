from itertools import product

# Fill with common prefixes, starting both with upcase and downcase
prefixes = {}

# Fill with all common prefixes like !
suffixes = {}

pro_pre_suf = []

for repeat in range(1, 5):
    print(f"Repeat: {repeat}")
    pro_mix = {''.join(x) for x in product(prefixes, repeat=repeat)}
    for suf_repeat in range(1,5):
        print(f"Suf Repeat: {suf_repeat}")
        suff_mix = {''.join(x) for x in product(suffixes, repeat=suf_repeat)}
        for pro in pro_mix:
            for suf in suff_mix:
                pro_pre_suf.append(f"{pro}{suf}")
                if(len(pro_pre_suf) == 300000):
                    with open('wordlist-generated.txt', 'a', encoding="utf-8", newline="\n") as wordlist:
                        stro = "\n".join(set(pro_pre_suf))
                        wordlist.write(stro)
                        print("Wrote batch")
                    pro_pre_suf = []

if pro_pre_suf:
    with open('wordlist-generated.txt', 'a', encoding="utf-8", newline="\n") as wordlist:
        stro = "\n".join(set(pro_pre_suf))
        wordlist.write(stro)
        print("Wrote remaining batch")
