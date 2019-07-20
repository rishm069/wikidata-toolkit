from pywikibot import ItemPage

from .television import Episode, Season
from .wikidata_properties import INSTANCE_OF, TELEVISION_SERIES_EPISODE, TELEVISION_SERIES_SEASON

class Factory():
    def __init__(self, repo):
        if repo is None:
            raise ValueError("repo cannot be None")
        self.repo = repo

    def get_typed_item(self, item_id):
        item_page = ItemPage(self.repo, item_id)
        item_page.get()
        if INSTANCE_OF.pid not in item_page.claims:
            raise ValueError(f"{item_id} has no 'instance of' property")

        item_type = item_page.claims[INSTANCE_OF.pid][0]
        instance_id = item_type.getTarget().id
        if instance_id == TELEVISION_SERIES_EPISODE:
            return Episode(item_page, self.repo)
        elif instance_id == TELEVISION_SERIES_SEASON:
            return Season(item_page, self.repo)

        raise ValueError(f"Unsupported item of type {item_type}")
