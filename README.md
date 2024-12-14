# AI News Collector

A Python application that collects AI-related news from Twitter using Twitter API v2.

## Features

- Fetches AI-related tweets using configurable search criteria
- Filters for verified accounts and tweets with links
- Supports customizable result limits
- Built-in logging and error handling
- Environment-based configuration

## Prerequisites

- Python 3.8+
- Twitter API Bearer Token
- pip package manager

## Installation

1. Clone the repository:

```bash
git clone https://github.com/rajeshkanaka/AI-News-Collector.git
cd AI-News-Collector
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```env
TWITTER_BEARER_TOKEN=your_twitter_bearer_token
```

get token
https://developer.twitter.com/en/portal/dashboard

![alt text](<CleanShot 2024-12-14 at 16.41.59@2x.png>)

## Usage

Run the main script:

```bash
python grok_writer.py
```

## Project Structure

```
NewLetter/
├── grok_writer.py         # Main collector implementation
├── twitter_api_client.py  # Twitter API client
├── requirements.txt       # Project dependencies
├── .env                  # Environment variables (not in repo)
└── README.md             # Documentation
```

## Configuration

The application uses the following environment variables:

- `TWITTER_BEARER_TOKEN`: Twitter API Bearer Token for authentication

## Search Criteria

Default search parameters:

- Language: English
- Tweet type: Original tweets (no retweets)
- Account status: Verified accounts
- Content requirements: Must contain links
- Topics: AI, Machine Learning, Deep Learning

## Error Handling

- Logs errors using Python's logging module
- Graceful handling of API failures
- Environment variable validation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
