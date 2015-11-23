import logging


class Search(object):
    """
    Search Object class
    """
    def __init__(self, client):
        """

        :param client: client.Client object
        :return: Search Object
        """
        self.logger = logging.getLogger(__name__)
        self.client = client

    def search(self, q, limit=None):
        """
        Performs a search against the /search endpoint

        :param q: query to be searched for [STRING]
        :param limit: limit the results [INT]
        :return: list of dicts
        """
        uri = '{}/search?q={}'.format(self.client.remote, q)
        self.logger.debug(uri)

        body = self.client.get(uri)
        body = {
            "feed": {
                "observables": body
            }
        }
        return body
