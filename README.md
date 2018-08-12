# Omniglot data set for one-shot learning  

This is a challenge submission for [fellowship.ai](fellowship.ai) cohort 13.

The challenge is to perform 1-shot learning on the [Omniglot dataset](https://github.com/brendenlake/omniglot).

## Omniglot  
- Omniglot dataset contains 1623 different handwritten characters from 50 different alphabets.
- Each character has 20 examples drawn by 20 different people online.
- The dataset also has information about stroke data, i.e. how it was drawn.
- It is split into "background" and "evaluation" sets of 30 and 20 alphabets respectively.
- Task is to do one-shot classification on the evaluation set after learning on the background set
- For our purposes, we use only the image data and ignore the stroke data.
- Some basic exploration, 1-NN experiment and demo run given in the dataset are in the [explore dataset](https://github.com/viraat/fellowshipai/blob/master/explore_dataset.ipynb) notebook.

## Existing solutions
- [Lake et. al](http://science.sciencemag.org/content/350/6266/1332) use Bayesian Program learning to achieve an error rate < 5% on the 20-way one-shot classification task. This method makes use of the stroke information. For a Siamese ConvNet they report an error of < 10%.
- We make use of Siamese networks as proposed by [Koch et. al](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf)
- They report an one-shot classification accuracy of 92% using Siamese ConvNets

## Solution
- Attempted to replicate the Siamese ConvNet as proposed by [Koch et. al](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf)
- The background set is split into a train and validation set in [train_test_split.ipynb](https://github.com/viraat/fellowshipai/blob/master/train_test_split.ipynb)
- Differences include using ADAM optimizer, and training for 100 epochs.
- Same network architecture is used.
- Main metric used to evaluate validation was the validation accuracy (20-way one-shot classification task for 161 batches)
- **A test set 20-way one-shot classification accuracy of 83.3% was achieved. Results are in the [kochnet_test.ipynb](https://github.com/viraat/fellowshipai/blob/master/kochnet_test.ipynb)**

## Possible improvements
- Attempted use of the [contrastive loss](http://yann.lecun.com/exdb/publis/pdf/hadsell-chopra-lecun-06.pdf) function which is in the [omniglot-contrastive.ipynb](https://github.com/viraat/fellowshipai/blob/master/omniglot-contrastive.ipynb)
- The training was slow to converge to a good solution. Likely due to the fact that the randomly generated positive and negative pairs were not contributing to the loss. Could improve this by using an online pair generation method.
- Training for a longer time with online pair generation will likely result in better performance. 
<!--
## Challenge goals
1. Problem solving ability - did you understand the problem correctly, and did you take logical steps to solve it?  
2. Machine learning skills - what sort of models did you use? How rigorous was your exploratory analysis of the data, your choice and fine tuning of models, and your assessment of results.  
3. Communication skills - is your solution readable and well explained? Messiness and raw code with no explanation does not reflect well on your potential for working well with our business partners during the fellowship.

## Mistakes to avoid
- Skipping exploratory analysis and feature engineering  
Do not jump straight into fitting models without demonstrating to us, in your Jupyter notebook, that you have understood and thought about the dataset.

- Choosing models with no explanation  
Please use the notebook to explain your thought process. We care about this as much as we care about your results.

- Unreadable notebooks  
Make sure to run your notebook before sharing so that we can see the results. We won't be running your code on our machines. On the flip side, please do not print out the entire dataset or endless rounds of epochs.

- Overly simplistic final results  
Your final results should consist of more than a single number or percentage printout. Explain why you chose the success metrics you chose, and analyze what your output means.


## Questions to Consider
Ask yourself why would they have selected this problem for the challenge? What are some gotchas in this domain I should know about?  
What is the highest level of accuracy that others have achieved with this dataset or similar problems / datasets ?  
What types of visualizations will help me grasp the nature of the problem / data?  
What feature engineering might help improve the signal?  
Which modeling techniques are good at capturing the types of relationships I see in this data?  
Now that I have a model, how can I be sure that I didn't introduce a bug in the code? If results are too good to be true, they probably are!  
What are some of the weaknesses of the model and and how can the model be improved with additional work? -->
