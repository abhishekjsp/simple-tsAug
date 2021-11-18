from simpleTsDataAug import Std_signals, Plotter, STsDA


if __name__ == '__main__':
    print('started sample execution')
    # generate a labeled time-series data of two different classes for testing
    my_data = Std_signals.two_class_labeled_signals()
    # print number of samples per class
    print('samples before augmentation: ', STsDA.get_event_count(my_data))
    # visualise the generated test data
    Plotter.plot_labeled_data(my_data, count=5)

    # augment the original data having 1 sample per class to generate data with 100 samples per class
    aug_data = STsDA.generate_balanced_augmented_data(my_data, aug_event_limit=100)
    # print number of samples per class
    print('samples after augmentation: ', STsDA.get_event_count(aug_data))
    # visualise the generated augmented data, first 5 plots per class
    Plotter.plot_labeled_data(aug_data, count=5)
