import pandas as pd
import folium
from folium.plugins import HeatMap

class HeatmapAgent:
    def build_map(self, df):

        # NOTE: In real HDB dataset, lat/lon is NOT included
        # So we approximate using town-level coordinates

        town_coords = {
            "bishan": [1.3521, 103.8510],
            "tampines": [1.3496, 103.9568],
            "jurong west": [1.3491, 103.7074],
            "punggol": [1.3984, 103.9072]
        }

        df = df.copy()
        df["town_lower"] = df["town"].str.lower()

        heat_data = []

        for _, row in df.iterrows():
            town = row["town_lower"]
            if town in town_coords:
                lat, lon = town_coords[town]
                price = row["resale_price"]
                heat_data.append([lat, lon, price])

        m = folium.Map(location=[1.3521, 103.8198], zoom_start=11)

        HeatMap(heat_data).add_to(m)

        return m