from scipy.stats import poisson

# Expected number of rainy days in 30 days
lam = 10

# 1. Probability of observing 12 or more rainy days
p_12_or_more = poisson.sf(11, lam)

# 2. Probability of observing between 12 and 18 rainy days (inclusive)
p_12_to_18 = poisson.cdf(18, lam) - poisson.cdf(11, lam)

# Display results
print("Probability of 12 or more rainy days:", p_12_or_more)
print("Percentage:", p_12_or_more * 100, "%")

print("\nProbability of between 12 and 18 rainy days:", p_12_to_18)
print("Percentage:", p_12_to_18 * 100, "%")