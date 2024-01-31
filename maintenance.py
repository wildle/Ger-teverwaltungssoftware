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
        q1_costs, q2_costs, q3_costs, q4_costs = 0, 0, 0, 0

        all_device_names = Device.get_all_device_names()

        for device_name in all_device_names:
            device = Device.load_data_by_device_name(device_name)
            if device and device.end_of_life and device.quarterly_costs:
                end_of_life_year = int(device.end_of_life.split('.')[0])

                if end_of_life_year == 2024:
                    # Verteile die Kosten auf die Quartale entsprechend dem end_of_life-Monat
                    end_of_life_month = int(device.end_of_life.split('.')[1])
                    if end_of_life_month <= 3:
                        q1_costs += device.quarterly_costs
                    elif end_of_life_month <= 6:
                        q2_costs += device.quarterly_costs
                    elif end_of_life_month <= 9:
                        q3_costs += device.quarterly_costs
                    else:
                        q4_costs += device.quarterly_costs

        return {"Q1": q1_costs, "Q2": q2_costs, "Q3": q3_costs, "Q4": q4_costs}
