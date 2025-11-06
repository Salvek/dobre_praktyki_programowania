class Link:
    def __init__(self, movieId: str, imdbId: str, tmdbId: str | None):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId
