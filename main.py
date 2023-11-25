import glob
import pandas as pd
import numpy
from pandas import DataFrame
from os.path import basename


LOCATION_ROW = "location"


def csv_data_frames(dir_path: str) -> list[DataFrame]:
    files_paths = glob.glob(dir_path)
    files_list = []

    for file_path in files_paths:
        data = pd.read_csv(file_path)
        filename_ext = basename(file_path)
        location = filename_ext.split(".")[0].split("_")[-1]
        data[LOCATION_ROW] = location

        files_list.append(data)

    return files_list


MY_COLUMNS = {
    "NOMBRE": "name",
    "TELEFONO": "phone",
    "EMAIL": "email",
    "DIRECCION": "direction",
    "TIPO DE ESTABLECIMIENTO": "type_establishment",
}
MY_COLUMNS_TYPES = {
    MY_COLUMNS["NOMBRE"]: "string",
    MY_COLUMNS["TELEFONO"]: "string",
    MY_COLUMNS["EMAIL"]: "string",
    MY_COLUMNS["DIRECCION"]: "string",
    MY_COLUMNS["TIPO DE ESTABLECIMIENTO"]: "string",
    LOCATION_ROW: "string",
}

rs_dfs = csv_data_frames("./data/*.csv")
r_df = pd.concat(rs_dfs, ignore_index=True)
r_df = r_df.rename(columns=MY_COLUMNS)
r_df = r_df.replace(numpy.nan, "N/A")
r_df = r_df.astype(MY_COLUMNS_TYPES)


r_df[MY_COLUMNS["NOMBRE"]] = r_df[MY_COLUMNS["NOMBRE"]].str.lower()

r_df[MY_COLUMNS["DIRECCION"]] = r_df[MY_COLUMNS["DIRECCION"]].str.lower()

r_df[MY_COLUMNS["TIPO DE ESTABLECIMIENTO"]] = r_df[
    MY_COLUMNS["TIPO DE ESTABLECIMIENTO"]
].str.lower()

r_df[MY_COLUMNS["TELEFONO"]] = r_df[MY_COLUMNS["TELEFONO"]].apply(
    lambda x: x.replace(".0", "")
)

r_df[MY_COLUMNS["EMAIL"]] = r_df[MY_COLUMNS["EMAIL"]].apply(
    lambda x: x.replace("NO", "N/A")
)


r_df.pop("DIAS DE ATENCION")
r_df.pop("SERVICIOS ADICIONALES")

print(r_df.groupby("location").describe())
