import sys
from pathlib import Path

src_path = Path(__file__).parent
sys.path.append(str(src_path))

from ports.http.app import init_app  # noqa: E402
from settings import settings  # noqa: E402

app = init_app(settings=settings)
