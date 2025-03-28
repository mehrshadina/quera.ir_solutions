def my_first_function(s1: str, s2: str) -> list[int]:
    """
    This function modifies two input strings, s1 and s2, and returns a list containing their lengths after the following operations:

        1.Append "HELLO" to s2 and assign the result to s1.
        2.Replace s2 with s1 repeated 12 times.
    """
    s1 = s2 + "HELLO"
    s2 = s1 * 12

    return [len(s1), len(s2)]