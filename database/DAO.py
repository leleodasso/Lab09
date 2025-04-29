from database.DB_connect import DBConnect
from model.airport import Airport
from model.flight import Flight


class DAO():
    
    def __init__(self):
        pass


    @staticmethod
    def getAllAirport():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "select * from extflightdelays.airports a "
        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "select * from extflightdelays.flights f"
        cursor.execute(query)

        for row in cursor:
            result.append(Flight(**row))
        cursor.close()
        conn.close()
        return result