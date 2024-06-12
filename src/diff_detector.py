class DiffDetector:
    def __init__(self, xpaths):
        self.xpaths = xpaths
        self.previous_data = {}

    def detect_diffs(self, scraped_data):
        diffs = {}
        for url, soup in scraped_data.items():
            if url not in self.previous_data:
                self.previous_data[url] = {}

            for xpath in self.xpaths:
                current_elements = soup.select(xpath)
                previous_elements = self.previous_data[url].get(xpath, [])

                if current_elements != previous_elements:
                    diff = self._get_diff(current_elements, previous_elements)
                    diffs.setdefault(url, {})[xpath] = diff

            self.previous_data[url] = {xpath: soup.select(xpath) for xpath in self.xpaths}

        return diffs

    def _get_diff(self, current_elements, previous_elements):
        # Implement diff logic here
        # Return the diff as a string
        return ""
