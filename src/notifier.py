import requests


class Notifier:
    def __init__(self, url, trigger_strings):
        self.url = url
        self.trigger_strings = trigger_strings

    def notify(self, diffs):
        for url, xpath_diffs in diffs.items():
            for xpath, diff in xpath_diffs.items():
                if any(s in diff for s in self.trigger_strings):
                    self._send_notification(url, xpath, diff)

    def _send_notification(self, url, xpath, diff):
        payload = {
            "url": url,
            "xpath": xpath,
            "diff": diff,
        }
        requests.post(self.url, json=payload)
