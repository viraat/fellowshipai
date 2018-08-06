import os
import torch
import pandas as pd
import random
import numpy as np
import hashlib
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from torch.utils.data.sampler import BatchSampler

# adapted from https://github.com/fangpin/siamese-network
class SiameseTrainData(Dataset):
    '''
    Train: For each sample creates randomly a positive or a negative pairs
    '''

    def __init__(self, dataset):
        self.dataset = dataset

    def __getitem__(self, index):

        target = np.random.randint(0, 2)
        img1, label1 = self.dataset[index]
        if target == 1:
            while True:
                siamese_index, (_, label2) = random.choice(list(enumerate(self.dataset._flat_character_images)))
                if label1 == label2:
                    break
        else:
            label2 = label1
            while label2 == label1:
                siamese_index, (_, label2) = random.choice(list(enumerate(self.dataset._flat_character_images)))

        img2, label2 = self.dataset[siamese_index]

        target = torch.from_numpy(np.array([target], dtype=np.float32))
        return (img1, img2, target)

    def __len__(self):
        return len(self.dataset)

# adapted from https://github.com/fangpin/siamese-network
class SiameseTestData(Dataset):

    def __init__(self, dataset, times=200, way=20, seed=0):
        self.dataset = dataset
        self.times = times
        self.way = way
        self.seed = seed

    def __len__(self):
        return self.times * self.way

    def __getitem__(self, index):
        self.rng = random.Random(self.seed + index)

        idx = index % self.way
        label = None

        # image frm same class
        if idx == 0:
            self.img1, self.label1 = self.dataset[index]
            while True:
                siamese_index, (_, label2) = self.rng.choice(list(enumerate(self.dataset._flat_character_images)))
                if self.label1 == label2:
                    break
        # image from different class
        else:
            label2 = self.label1
            while label2 == self.label1:
                siamese_index, (_, label2) = self.rng.choice(list(enumerate(self.dataset._flat_character_images)))

        img2, label2 = self.dataset[siamese_index]

        return self.img1, img2
