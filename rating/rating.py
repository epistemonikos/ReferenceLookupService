from rating.ratings.authors_rating import AuthorsRating
from rating.ratings.title_rating import TitleRating
from rating.ratings.year_rating import YearRating

class Rating:
    def __init__(self, cita, json):
        self.cita = cita
        self.json = json

        authors_given = [aut['given'] for aut in json['author']]
        authors_family = [aut['family'] for aut in json['author']]
        year = str(json['created']['date-parts'][0][0])
        title = ''
        try:
            title = json['title'][-1] or json['short-title'][-1]
        except:
            pass
        self.authors_rating = AuthorsRating(cita, authors_given, authors_family)
        self.title_rating = TitleRating(cita, title)
        self.year_rating = YearRating(cita, year)

    def value(self, verbose=False):
        title_rating = self.title_rating.value()
        authors_rating = self.authors_rating.value()
        year_rating = self.year_rating.value()
        if verbose:
            print(pretty_cita(cita))
            print(self.json)
            print("authors: %s" % a_rate)
            print("year: %s" % y_rate)
            print("t_rate: %s" % t_rate)
            print("final_rate: %s" % final_rate)
        return {
            'total' : title_rating*0.65 + authors_rating*0.25 + year_rating*0.1,
            'title' : title_rating,
            'authors' : authors_rating,
            'year' : year_rating
        }
