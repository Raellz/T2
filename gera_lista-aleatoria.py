from random import Random
rng = Random()
values = [str(rng.randint(0, 1000)) for _ in range(1000)]
print(",".join(values))