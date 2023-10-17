def get_float(num_check):
    """checks the string passed it for leading float number and gets the float number of any length
    from 1-5

    Args:
        num_check (string): should be the string with float at the beginning (example, '4.01 HERITAGE ASSET NOTE')

    Returns:
        float: returns the float number that was at the beginning of the string passed in to argument
    """
    try:
        return float(num_check[:5])
    except ValueError:
        try:
            return float(num_check[:4])
        except ValueError:
            try:
                return float(num_check[:3])
            except ValueError:
                try:
                    return float(num_check[:2])
                except ValueError:
                    try:
                        return float(num_check[:1])
                    except Exception as ex:
                        print(ex)

my_strings = ["3.01 HERITAGE ASSET NOTES",
              "10.21 HERITAGE ASSET NOTES AGAIN"]

for s in my_strings:
    print(get_float(s))