from db.run_sql import run_sql
from models.repair import Repair


def delete_all():
    sql = "DELETE FROM repairs"
    run_sql(sql)