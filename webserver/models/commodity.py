import storm.locals as orm
import datastore

class CommodityStore(datastore.DataStore):
    def __init__(self, db_url):
        super(Commodity, self).__init__(db_url)

    def create_commodity(self, commodity):
        self.store.add(commodity)
        self.store.commit()

    def update_commodity(self, commodity):
        dst_commodity = self.store.find(Commodity, Commodity.id == commodity.id)
        if not dist_commodity:
            self.store.add(commodity)
        else:
            dst_commodity = dst_commodity.one()

        self.store.commit()
        return dist_commodity

    def get_commodity_by_id(self, id):
        results = self.store.find(Commodity, Commodity.id == id)
        if results.count() == 0:
            return None
        return results.one()

class Commodity(object):
    __storm_table__ = "commodity"
    id = orm.Int(primary=True)

    def __init__(self):
        return


