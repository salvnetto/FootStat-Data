from datetime import datetime


URL_FBREF = 'https://fbref.com'
FORMAT = '.csv'
SUPPORTED_FILES = ['standings', 'match_history', 'squads']

now = datetime.now()

SEASONS = {
    'full_year': [str(year) for year in range(2019, now.year+1)],
    'split_years': (
        [f"{year}-{year+1}" for year in range(2019, now.year) if now.month < 7] +
        [f"{year}-{year+1}" for year in range(2019, now.year + 1) if now.month >= 7]
    )
}

ACTIVE_SEASON = {
    'full_year': str(now.year),
    'split_years': f"{now.year-1}-{now.year}" if now.month < 7 else f"{now.year}-{now.year+1}"
}


NAME_CHANGES = {
    "Ath Paranaense": "Athletico Paranaense",
    "Atl Goianiense": "Atlético Goianiense"
}