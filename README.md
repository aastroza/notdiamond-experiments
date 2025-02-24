# NotDiamond Experiments

A simple test using the NotDiamond Python SDK. Can an LLM Router help reduce racial bias? This experiment explores that question using a small-scale "toy problem" approach.

## Installation

### Windows

```bash
uv venv --python 3.12
uv pip install -r requirements.txt
```

## Dataset

We use a small dataset from the [MBIB](https://huggingface.co/datasets/mediabiasgroup/mbib-base) (Media Bias Identification Benchmark). It consists of 40 training examples and 10 test examples, all from the `racial_bias` category, with a balanced distribution.

## Training Steps

1. [Prepare the dataset](/00_prepare_dataset_for_training.ipynb)
2. [Train a NotDiamond customer router](/01_train_notdiamond.ipynb)
3. [Evaluate the model](/02_eval_notdiamond.ipynb)

## Results

Here are the evaluation results for the raw responses from different models:

| Provider                               | Train | Train Accuracy (%) | Test | Test Accuracy (%) |
|----------------------------------------|-------|--------------------|------|-------------------|
| google/gemini-1.5-pro-latest           | 19    | 47.50              | 5    | 50.00             |
| mistral/mistral-large-2407             | 16    | 40.00              | 6    | 60.00             |
| openai/gpt-4o-2024-08-06               | 19    | 47.50              | 7    | 70.00             |
| openai/gpt-4o-mini-2024-07-18          | 16    | 40.00              | 6    | 60.00             |
| perplexity/sonar                        | 15    | 37.50              | 6    | 60.00             |
| togetherai/DeepSeek-R1                 | 18    | 45.00              | 6    | 60.00   

The models perform far from perfectly on the training dataset but achieve reasonable accuracy on the test set.

Both the NotDiamond base router and our trained custom router ended up routing all requests to the `gpt-4o-2024-08-06` model. While this was an interesting experiment, we need a more extensive dataset and a more detailed evaluation to draw meaningful conclusions.