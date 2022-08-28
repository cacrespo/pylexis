"""Common functionality for inputs."""


def check_range_grid(start, end, input):
    """Validates that the input value are between the maximum and minimum
    possible."""
    if start <= input <= end:
        return
    else:
        message = f"""Invalid Data
            Range of allowed grid values: {start} to {end}
            Value: {input}"""
        raise ValueError(message)
