def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
    returns a sequence of same length with the averages.
    You can assume all items in sequence are numeric."""
    running_mean = []
    for i, _ in enumerate(sequence):
        running_mean.append(round(sum(sequence[: i + 1]) / (i + 1), ndigits=2))

    return running_mean
