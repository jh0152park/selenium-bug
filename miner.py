DATA = "product.csv"


class Miner:
    def __init__(self):
        self.products = []

    def check_product_list(self):
        try:
            with open(DATA, "r", encoding="cp949") as f:
                for p in f.readlines()[1:]:
                    datas = p.split(",")
                    if len(datas) > 4:
                        self.products.append({
                            "url": datas[0],
                            "name": datas[1],
                            "price": datas[2],
                            "amount": datas[3],
                            "delivery": datas[4],
                        })
        except Exception as err:
            print(f"Occurrend some error: {err}")

    def get_product_list(self):
        self.check_product_list()
        return self.products
