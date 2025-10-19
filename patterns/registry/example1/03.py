from functools import wraps
from typing import Callable, Dict, Literal

type IData = Dict[str, str | int | None]
type ExportFn = Callable[[IData], None]

exporters: Dict[str, ExportFn] = {}


def register_exporter(
    format: Literal["pdf", "json", "csv"]
) -> Callable[[ExportFn], ExportFn]:
    def decorator(fn: ExportFn) -> None:
        @wraps(fn)
        def wrapper(data: IData) -> None:
            return fn(data)

        exporters[format] = wrapper
        return wrapper

    return decorator


@register_exporter("pdf")
def export_pdf(data: IData) -> None:
    print("Exporting to pdf ...")


@register_exporter("json")
def export_json(data: IData) -> None:
    print("Exporting to json ...")


@register_exporter("csv")
def export_csv(data: IData) -> None:
    print("Exporting to csv ...")


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
