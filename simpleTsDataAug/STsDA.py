import random
import numpy as np


def get_event_count(dataset):
    event_tags = np.array(dataset)[:, -1]
    et, count = np.unique(event_tags, return_counts=True)

    # for ev, ev_count in zip(et, count):
    #     print(ev, ' : ', ev_count)

    return dict(zip(et, count))


def shift_list(l, shift, empty=None):
    src_index = max(-shift, 0)
    dst_index = max(shift, 0)
    # src_index = -shift
    # dst_index = shift
    length = max(len(l) - abs(shift), 0)
    new_l = [empty] * len(l)
    new_l[dst_index:dst_index + length] = l[src_index:src_index + length]
    return new_l


def generate_augmented_signal(signal):
    X_aug = [signal]

    for i in range(3):
        rs = random.randint(0, int(len(signal)*0.05))
        m = max(signal)/10
        p = signal[0]+random.random()*m
        X_aug.append(shift_list([d + random.random()*m for d in signal], rs))

    return X_aug


def generate_augmented_data(dataset):
    X_aug = []

    for row in dataset:
        x = row[:30]
        label = row[-1]
        X_aug.append(row)
        for i in range(9):
            rs = random.randint(0, 2)
            m = max(x)/100
            p = x[0]+random.random()*m if x[0] else 0
            X_aug.append(shift_list([d + random.random()*m if d else d for d in x], rs, p)+[label])

    return X_aug


def generate_balanced_augmented_data(dataset, aug_event_limit=10):
    count_dict = get_event_count(dataset)
    data_dict = {}

    for data in dataset:
        if data[-1] not in data_dict:
            data_dict[data[-1]] = [data]
        else:
            data_dict[data[-1]].append(data)

    X_aug = []

    for tag, count in count_dict.items():
        if count >= aug_event_limit:
            continue
        X_aug += data_dict[tag]
        max_i = len(data_dict[tag]) - 1
        for i in range(aug_event_limit - count):
            ri = random.randint(0, max_i)
            row = data_dict[tag][ri]
            # breakpoint()
            x = row[:-1]
            label = row[-1]
            rs = random.randint(0, 2)
            m = max(x) / 10
            p = x[0] + random.random() * m if x[0] else 0
            X_aug.append(shift_list([d + random.random() * m if d else d for d in x], rs) + [label])

    return X_aug