import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

LOCATION_ROW = "location"
AVERAGE_CLIENT_PER_DAY = "average_client_day"
AVERAGE_EARNINGS_PER_DAY = "average_earnings_day"
MY_COLUMNS = {
    "NOMBRE": "name",
    "TELEFONO": "phone",
    "EMAIL": "email",
    "DIRECCION": "direction",
    "TIPO DE ESTABLECIMIENTO": "type_establishment",
    "LOACION": LOCATION_ROW,
    "PROMEDIO DE GANANCIAS POR DIA": AVERAGE_EARNINGS_PER_DAY,
    "PROMEDIA DE CLIENTES POR DIA": AVERAGE_CLIENT_PER_DAY,
}
MY_COLUMNS_TYPES = {
    "name": "string",
    "phone": "string",
    "email": "string",
    "direction": "string",
    "type_establishment": "string",
    LOCATION_ROW: "string",
    AVERAGE_CLIENT_PER_DAY: "int",
    AVERAGE_EARNINGS_PER_DAY: "int",
}

r_df = pd.read_csv("./data/industria_gastronomica.csv")
r_df = r_df.rename(columns=MY_COLUMNS)
r_df = r_df.astype(MY_COLUMNS_TYPES)
r_df = r_df.replace(np.nan, "n/a")

r_df["name"] = r_df["name"].str.lower()
r_df["direction"] = r_df["direction"].str.lower()
r_df["type_establishment"] = r_df["type_establishment"].str.lower()
r_df["type_establishment"] = r_df["type_establishment"].apply(
    lambda x: x.replace("á", "a")
)
r_df = r_df[r_df["type_establishment"].str.contains("restaurante")]
r_df["phone"] = r_df["phone"].apply(lambda x: x.replace(".0", ""))
r_df["email"] = r_df["email"].apply(lambda x: x.replace("NO", "N/A"))

# restaurants_by_location = (
#     r_df.groupby(["location", "type_establishment"]).size().unstack()
# )
# restaurants_by_location = restaurants_by_location.replace(np.nan, 0)

# fig, ax = plt.subplots(figsize=(12, 6), gridspec_kw={"right": 0.70, "bottom": 0.23})
# restaurants_by_location.plot(kind="bar", ax=ax)

# ax.set_title("Tipos de Restaurantes por Ubicación")
# ax.set_xlabel("Ubicación")
# ax.set_ylabel("Número de Establecimientos")
# ax.legend(title="Tipo de Establecimiento", bbox_to_anchor=(1.05, 1), loc="upper left")

# plt.show()

# grouped_data = r_df.groupby("location")["average_client_day"].mean()

# # Crea un diagrama de sectores con colores diferentes para cada sección
# plt.figure(figsize=(8, 8))
# plt.pie(grouped_data, labels=grouped_data.index, autopct="%1.1f%%")

# # Ajusta el diseño y muestra el gráfico
# plt.title("Diagrama de Sectores por Número Promedio de Clientes y Ubicación")
# plt.show()
