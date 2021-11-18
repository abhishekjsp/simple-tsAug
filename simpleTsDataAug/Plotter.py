import matplotlib.pyplot as plt


def plot(data):
    """generates a plot of time-series
    Parameters
    ----------
    data : list, numpy array
        array containing y values of a time-series
    Returns
    -------
    None
    Examples
    --------
    >>> plot([1,2,3])"""
    plt.plot(data)
    plt.show()


def plot_array(list_data, count=0):
    """generates a combined plot of multiple time-series, numner of plots limited by count parameter
    Parameters
    ----------
    list_data : 2D list, 2D numpy array
        array containing arrays of time-series data
    count: int, optional
        number of plots to be generated, 0 (the default) will plot all the given data
    Returns
    -------
    None
    Examples
    --------
    >>> plot([[1,2,3],
            [4,5,6]])
    >>> plot([[1,2,3],
            [4,5,6],
            [7,8,9]], count=2)"""
    for i, data in enumerate(list_data):
        plt.plot(data)
        if max and i+1 >= count:
            break
    plt.show()


def plot_labeled_data(list_data, count=0):
    """generates a combined plot of multiple time-series from a labeled dataset,
     numner of plots per class limited by count parameter
    Parameters
    ----------
    list_data : 2D list, 2D numpy array
        array containing arrays of labeled time-series data
    count: int, optional
        number of plots per class to be generated, 0 (the default) will plot all the given data
    Returns
    -------
    None
    Examples
    --------
    >>> plot([[1,2,3, 'class 1'],
            [4,5,6, 'class 2']])
    >>> plot([[1,2,3, 'class 1'],
            [4,5,6, 'class 1'],
            [7,8,9, 'class 2]], count=1)"""
    labels = {x[-1] for x in list_data}
    # print(labels)
    for label in labels:
        i = 0
        for data in list_data:
            if data[-1] != label:
                continue
            plt.plot(data[:-1], label=label)
            i+=1
            if count and i >= count:
                break
    plt.legend()
    plt.show()
