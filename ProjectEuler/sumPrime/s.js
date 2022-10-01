function sumPrime(r) {
  primes = [2];
  for (i = 2; i < r; i++) {
    if (i % 2 != 0) {
      devided = false;
      for (prime of primes) {
        if (i % prime == 0) {
          devided = true;
        }
      }
      if (!devided) {
        primes.push(i);
      }
    }
  }
  let tot = 0;
  for (prime of primes) {
    tot += prime;
  }
  return tot;
}
