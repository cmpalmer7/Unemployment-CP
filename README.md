# Unemployment-CP

## Setup

Obtain an [API Key] (Obtain an [AlphaVantage API Key](https://www.alphavantage.co/support/#api-key). A normal key should be fine, but alternatively you can use one of the prof's "premium" keys.)

Create virtual environment:

```sh
conda create -n unemployemnt-env python=3.10
```

```sh
conda activate unemployemnt-env
```

Install third-party packages:

```sh
pip install -r requirements.txt
```


## Usage

Run the report:

```sh
python -m app.unemployment
```