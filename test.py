import requests


class TestProgram:
    def test_usd_balance(self):
        site = requests.get('http://localhost:4545/rate/usd')
        assert site.status_code == 200
        assert site.json() == {'usd': {'rate': 75.43}}

    def test_eur_balance(self):
        site = requests.get('http://localhost:4545/rate/eur')
        assert site.status_code == 200
        assert site.json() == {'eur': {'rate': 90.25}}

    def test_hryvnia_balance(self):
        site = requests.get('http://localhost:4545/rate/bgn')
        assert site.status_code == 400