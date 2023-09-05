import hashlib
import pathlib
import shutil

BASE_DIR = pathlib.Path(__file__).resolve().parent
TARGET_DIR = BASE_DIR / "video_renamed"


def copy_videos():
    for idx, video in enumerate(sorted(BASE_DIR.glob("*.mkv")), start=1):
        new_name = f"{idx:03}{video.suffix}"
        shutil.copy(video, TARGET_DIR / new_name)


def check_videos():
    for from_, to in zip(
        sorted(BASE_DIR.glob("*.mkv")),
        sorted(TARGET_DIR.glob("*.mkv")),
        strict=True,
    ):
        with from_.open("rb") as from_file, to.open("rb") as to_file:
            from_hash = hashlib.sha256(from_file.read()).hexdigest()
            to_hash = hashlib.sha256(to_file.read()).hexdigest()
            assert from_hash == to_hash, f"File {from_} and {to} not match."


if __name__ == "__main__":
    if not TARGET_DIR.exists():
        TARGET_DIR.mkdir()

    copy_videos()
    check_videos()

    print("Done")
