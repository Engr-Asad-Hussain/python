from typing import Dict, Literal

type IData = Dict[str, str | int | None]


def export_pdf(data: IData) -> None:
    print("Exporting to pdf ...")


def export_json(data: IData) -> None:
    print("Exporting to json ...")


def export_csv(data: IData) -> None:
    print("Exporting to csv ...")


def export_data(data: IData, format: Literal["pdf", "json", "csv"]) -> None:
    if format == "pdf":
        export_pdf(data)
    elif format == "json":
        export_json(data)
    elif format == "csv":
        export_csv(data)
    else:
        raise ValueError("❌ No exporter found.")


def main() -> None:
    sample_data = {"id": 1, "name": "Izzah", "gender": "female"}
    export_data(sample_data, "pdf")
    export_data(sample_data, "json")
    export_data(sample_data, "csv")

    # Exception!
    # export_data(sample_data, "xml")


if __name__ == "__main__":
    main()
