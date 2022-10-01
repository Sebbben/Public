function get10001Prime(r) {
  let primes = [2];
  let i = 2;
  while (primes.length < r) {
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
    i++;
  }
  return primes[primes.length - 1];
}
