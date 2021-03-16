def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """

artist_id = 0
album_id = 1
year_id = 2
genre_id = 3
time_id = 4

albums = [
            ["Pink Floyd", "The Dark Side Of The Moon", "1973", "progressive rock", "43:00"],
            ["Britney Spears", "Baby One More Time", "1999", "pop", "42:20"],
            ["The Beatles", "Revolver", "1966", "rock", "34:43"],
            ["Deep Purple", "Machine Head", "1972", "hard rock", "37:25"],
            ["Old Timers", "Old Time", "966", "ancient", "123:45"],
            ["Pink Floyd", "Wish You Were Here", "1975", "progressive rock", "44:28"],
            ["Boston", "Boston", "1976", "hard rock", "37:41"],
            ["Monika Brodka", "Granada", "2010", "pop", "37:42"],
            ["David Bowie", "Low", "1977", "rock", "38:26"],
            ["rock", "rock", "966", "pop", "13:37"],
            ["Massive Attack", "Blue Lines", "1991", "hip hop", "45:02"]
        ]



def get_genre_stats(albums):
    """
    Get albums' statistics showing how many albums are in each genre
    Example: { 'pop': 2, 'hard rock': 3, 'folk': 20, 'rock': 42 }

    :param list albums: albums' data
    :returns: genre stats
    :rtype: dict
    """
    genre_stats = {}
    for album in albums:
        if not album[genre_id] in genre_stats:
            genre_stats[album[genre_id]] = 1
        else:
            genre_stats[album[genre_id]] = genre_stats[album[genre_id]] + 1

    return genre_stats


def genres_with_biggest_number_of_albums(stats) -> dict:
    biggest_number_of_albums = 0 #stats[list(stats.keys())[0]]
    for genre in stats.keys():
        if stats[genre] > biggest_number_of_albums:
            biggest_number_of_albums = stats[genre]

    for genre in stats.keys():
        if stats[genre] == biggest_number_of_albums:
            print(genre)

genres_with_biggest_number_of_albums(get_genre_stats(albums))

def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """


def get_last_oldest(albums):
    """
    Get last album with earliest release year.
    If there is more than one album with earliest release year return the last
    one of them (by original list's order)

    :param list albums: albums' data
    :returns: last oldest album
    :rtype: list
    """


def get_last_oldest_of_genre(albums, genre):
    """
    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: last oldest album in genre
    :rtype: list
    """


def to_time(time:str) -> int:
    """
    converts time in format "minutes:seconds" (string) to seconds (int)
    """
    minutes, seconds = time.split(":")
    return int(minutes)*60 + int(seconds)

def reverse_to_time(time:int) -> str:
    minutes = int(time/60)
    seconds = time%60

    complement_of_zero_digit_for_minutes = '0' if minutes < 10 else ''
    complement_of_zero_digit_for_seconds = '0' if seconds < 10 else ''

    return f"{complement_of_zero_digit_for_minutes}{minutes}:{complement_of_zero_digit_for_seconds}{seconds}"

a = reverse_to_time(60)

def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18             
             231 + 320 seconds = 551 seconds

    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
