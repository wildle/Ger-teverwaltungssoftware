from devices import Device
class Maintenance:
    def get_next_maintenance_dates():
        
        next_maintenance_dates = {}
        all_device_names = Device.get_all_device_names()

        for device_name in all_device_names:
            device = Device.load_data_by_device_name(device_name)
            if device and device.end_of_life:
                next_maintenance_dates[device.device_name] = device.end_of_life

        return next_maintenance_dates

    @staticmethod
    def get_quarterly_maintenance_costs():
        # Hier sollte der Code stehen, der die Wartungskosten pro Quartal berechnet
        return {"Q1": 100, "Q2": 200}