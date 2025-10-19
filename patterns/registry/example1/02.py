from typing import Callable, Dict, Literal

type IData = Dict[str, str | int | None]
type ExportFn = Callable[[IData], None]


def export_pdf(data: IData) -> None:
    print("Exporting to pdf ...")


def export_json(data: IData) -> None:
    print("Exporting to json ...")


def export_csv(data: IData) -> None:
    print("Exporting to csv ...")


exporters: Dict[str, ExportFn] = {
    "pdf": export_pdf,
    "json": export_json,
    "csv": export_csv,
}


def export_data(data: IData, format: Literal["pdf", "json", "csv"]) -> None:
    exporter = exporters.get(format)
    if exporter is None:
        raise ValueError("❌ No exporter found.")
    exporter(data)


def main() -> None:
    sample_data = {"id": 1, "name": "Izzah", "gender": "female"}
    export_data(sample_data, "pdf")
    export_data(sample_data, "json")
    export_data(sample_data, "csv")

    # Exception!
    # export_data(sample_data, "xml")


if __name__ == "__main__":
    main()
