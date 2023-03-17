from psycopg_pool import ConnectionPool
import os

class Db:
  def __init__(self):
    self.init_pool()
  
  def init_pool():
    connection_url = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_url)

  def query_commit():
    try:
      conn = self.pool.connection()
      cur = conn.cursor()
      cur.execute(sql)
      conn.commit()
    except Exception as err:
      self.print_sql_err(err)
      #conn.rollback()

  def query_array():
    wrapped_sql = query_wrap_array(sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql)
        # this will return a tuple
        # the first field being the data
        json = cur.fetchone()
  
  def query_object(sql):

  
  def query_wrap_object(template):
    sql = f"""
    (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
    {template}
    ) object_row);
    """
    return sql

  def query_wrap_array(template):
    sql = f"""
    (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
    {template}
    ) array_row);
    """
    return sql

  def print_sql_err(err):
    err_type, err_obj, traceback = sys.exc_info()
    line_num = traceback.tb_lineno

    print("\npsycopg ERROR", err, "on line number:", line_num)
    print("psycopg traceback:", traceback, "-- type:", err_type)

    print("\nextensions.Diagnostics:", err.diag)
    
    print("pgerror:", err.pgerror)
    print("pgcode:", err.pgcode, "\n")


db = Db()