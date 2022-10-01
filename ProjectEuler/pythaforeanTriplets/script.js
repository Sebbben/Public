function pythagoreanTriplets(r, target) {
  for (i = 1; i < r; i++) {
    for (j = 1; j < i; j++) {
      c = i ** 2 + j ** 2;
      c = Math.sqrt(c);
      if (c % 1 != 0) continue;
      if (i + j + c == target) {
        return i, j, c, i * j * c;
      }
    }
  }
}
