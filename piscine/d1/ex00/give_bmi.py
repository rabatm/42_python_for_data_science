import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
give_bmi(height: list[int | float], weight: list[int | float])
                                            -> list[int | float
Return an list of bmi."""

    try:
        np_height = np.array(height)
        np_weight = np.array(weight)
        assert isinstance(height, list), "Height must be lists"
        assert isinstance(weight, list), "Weight must be lists"
        assert np_height.dtype in [np.float64, np.int64], \
            "Height array must be a number"
        assert np_weight.dtype in [np.float64, np.int64], \
            "Weight array must be number"
        assert np_height.dtype in [np.float32, np.int32], \
            "Height array must be a number"
        assert np_weight.dtype in [np.float32, np.int32], \
            "Weight array must be number"

        print(np_height.dtype)
        bmi = np_height / (np_weight ** 2)
        squared_height = np.multiply(height, height)
        bmi = np.divide(weight, squared_height)
        return bmi.tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}")


def apply_limit(bmi: list[float | int], limit: int) -> list[bool]:
    # Gérer le cas où un élément est None
    if any(x is None for x in bmi):
        raise ValueError("bmi contains None values")

    # Gérer les strings convertibles en nombre
    try:
        return [float(x) > limit for x in bmi]
    except (ValueError, TypeError):
        raise TypeError("All elements in bmi must be numeric")
