import numpy as np


def slice_me(
    family: list,
    start: int,
    end: int
) -> list:
    """
    slice_me(family: list, start: int, end: int)
                                                -> list:
This function takes as parameters a 2D array, prints its shape,
and returns a
truncated version of the array based on the provided start and
end arguments."""
    try:
        assert isinstance(family, list), "family must be list"
        lengths = set(len(row) for row in family)
        if len(lengths) > 1:
            raise ValueError(
                "Toutes les listes internes doivent avoir la même taille.")
        np_family = np.array(family)

        print(np_family.shape)
        np_family_split = np_family[start:end]
        print(np_family_split.shape)
        return np_family.tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}")
