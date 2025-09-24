from correlation import ALIASES


def get_correlation(method: str, **kwargs):
    method = method.lower()

    model = ALIASES[method]

    return model(**kwargs)


rho = get_correlation("BakErjayaram08", T1=10, T2=0.5)
print("Correlation:", rho)
