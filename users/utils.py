import json


class AccessManager:
    """
    JSON exmaple
    {
        "product_name": 'Музыкальный курс',
    }
    """
    def __init__(self, filename: str = "users/access_to_product.json") -> None:
        self.filename = filename

    def _read(self) -> dict:
        with open(self.filename) as f:
            return json.load(f)

    def _write(self, date: dict) -> None:
        with open(self.filename, "w") as f:
            json.dump(date, f)

    def add_product(self, product_name: str) -> None:
        d = self._read()
        d[product_name] = []
        self._write(d)

    def add_user(self, product_name: str, username: str) -> None:
        d = self._read()
        if product_name not in d:
            d[product_name] = []
        d[product_name].append(username)
        self._write(d)

    def check_user_in_product(self, product_name: str, user_name: str) -> bool:
        d = self._read()
        if product_name in d and user_name in d[product_name]:
            return True
        return False
