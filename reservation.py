import streamlit as st
from tinydb import TinyDB, Query
from tab3_Reservierungssystem import reservation_system

class reservation_system():
    def __init__(self, db_file="database.json"):
        self.db = TinyDB(db_file)
        self.reservation_table = self.db.table("reservations")
        self.Reservation = Query()

    def create_reservation(self, device, period, reason):
        self.reservation_table.insert({"device": device, "period": period, "reason": reason})

    def get_reservations(self, device):
        reservations = self.reservation_table.search(self.Reservation.device == device)
        return reservations