import time

def zaman_begir(kar):
    def anjam_dahande(n):
        start = time.perf_counter()
        result = kar(n)
        end = time.perf_counter()
        zaman = end - start
        print(f" zamane ejra: {zaman:.8f} sanie")
        return result
    return anjam_dahande

@zaman_begir
def list_besaz(n):
    return list(range(1, n + 1))

n = int(input("adad n ra vared konid: "))
lst = list_besaz(n)
print(f" tedad list ha: {lst}")
