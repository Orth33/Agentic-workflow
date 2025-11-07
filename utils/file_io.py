from pathlib import Path
from datetime import datetime
from config.settings import DOCUMENTS_DIR, RESULTS_DIR, TEXT_EXTENSIONS

def get_documents(folder_path=DOCUMENTS_DIR):
    folder = Path(folder_path)
    if not folder.exists():
        folder.mkdir(exist_ok=True)
        print(f"📂 Created '{folder}' — add text files to process.")
        return []
    return [
        (f.name, f.read_text(encoding='utf-8').strip())
        for f in folder.iterdir()
        if f.is_file() and f.suffix.lower() in TEXT_EXTENSIONS
    ]

def save_results(results, output_folder=RESULTS_DIR):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    batch_folder = Path(output_folder) / f"batch_{timestamp}"
    batch_folder.mkdir(parents=True, exist_ok=True)

    for result in results:
        base = Path(result['filename']).stem
        for key in ['summary', 'decision', 'report']:
            if result[key]:
                path = batch_folder / f"{base}_{key}.txt"
                path.write_text(result[key], encoding='utf-8')
    print(f"💾 Results saved in {batch_folder}")
    return batch_folder
