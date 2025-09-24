from spatial_correlation import ALIASES


def get_spatial_correlation(method: str, **kwargs):
    method = method.lower()

    model = ALIASES[method]

    try:
        rho = model(**kwargs)

        return rho

    except TypeError:
        from spatial_correlation import select_func_args

        args = select_func_args(model)

        raise ValueError(
            f"Method: {method} requires the following arguments:",
            f"{args}"
        )

# Example 1
rho = get_spatial_correlation("jayarambaker09", T=3, h=20, vs30=1)
print("Correlation:", rho)


# Example 2
rho = get_spatial_correlation("markhvidaetal18", T1=0.1, T2=3, h=20)
print("Correlation:", rho)