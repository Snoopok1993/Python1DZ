from sqlalchemy import create_engine 
db_connection_string = "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"
db = create_engine(db_connection_string)

def test_db_connection():
    name = db.table_names()
    assert name[0] == 'company'