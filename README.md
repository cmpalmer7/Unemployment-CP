# Unemployment-CP

## Setup

Obtain an [API Key] (Obtain an [AlphaVantage API Key](https://www.alphavantage.co/support/#api-key). A normal key should be fine, but alternatively you can use one of the prof's "premium" keys.)

Add your API key to an .env file and place your key inside like:

```sh
ALPHAVANTAGE_API_KEY="API KEY HERE"
```

Create virtual environment:

```sh
conda create -n unemployment-env python=3.10
```

```sh
conda activate unemployment-env
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

Run the report:

```sh
python -m app.tweets
```

Run the web apps:
```sh
FLASK_APP=web_app flask run
```

## Testing


```sh
pytest
```

## [Deployment Guide](/DEPLOYING.md)