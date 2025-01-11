import math

def sieve_of_eratosthenes(limit):
    """
    Génère une liste de nombres premiers jusqu'à la limite spécifiée en utilisant le crible d'Ératosthène.
    """
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 et 1 ne sont pas des nombres premiers

    for start in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[start]:
            for multiple in range(start*start, limit + 1, start):
                is_prime[multiple] = False

    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

def find_large_primes(count):
    """
    Trouve les premiers 'count' nombres premiers.
    """
    # Estimation de la limite supérieure à utiliser dans le crible d'Ératosthène
    # Utilisation de la fonction d'approximation de la distribution des nombres premiers
    # pi(x) ~ x / ln(x) donne une estimation de la limite supérieure pour trouver 'count' nombres premiers
    limit = int(count * math.log(count) * 1.15)
    primes = sieve_of_eratosthenes(limit)
    
    # Assurez-vous d'avoir exactement 'count' nombres premiers
    while len(primes) < count:
        limit = int(limit * 1.1)
        primes = sieve_of_eratosthenes(limit)
    
    return primes[:count]

# Exemple d'utilisation: trouver les 100 000 000 premiers nombres premiers
count = 100_000
primes = find_large_primes(count)

print(f"Les {count} premiers nombres premiers ont été trouvés.")
# Affichage des 10 premiers nombres premiers pour vérification
print(primes[:100])