from correlation import ALIASES


def get_correlation(method: str, **kwargs):
    method = method.lower()

    model = ALIASES[method]

    try:
        rho = model(**kwargs)

        return rho

    except TypeError:
        from correlation import select_func_args

        args = select_func_args(model)

        raise ValueError(
            f"Method: {method} requires the following arguments:",
            f"{args}"
        )


rho = get_correlation("bakerbradley17", T1=3, T2=0.5)
print("Correlation:", rho)
