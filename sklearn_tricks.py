# detect prediction outliers
# Vincent Warmerdam: How to Constrain Artificial Stupidity

out = GaussianMixture(3).fit(X)
boundary = np.quantile(out.score_samples(X), 0.01)


