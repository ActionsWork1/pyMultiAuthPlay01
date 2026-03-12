BROWSER_CONFIG = {
    "browser_name": "chromium",   # chromium | firefox | webkit
    "headless": False,

    "context": {
        "viewport": {"width": 1440, "height": 900},
        "locale": "en-US",
        "timezone_id": "Asia/Kolkata",
        "ignore_https_errors": True,
        "record_video_dir": "videos/"
    },

    "mode": "web",  # web | device

    "device": "iPhone 13"
}