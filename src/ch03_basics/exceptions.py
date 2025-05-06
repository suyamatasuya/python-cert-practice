class BloodPressureError(Exception):
    """収縮期血圧が範囲外のときに送出する独自例外"""
    pass                           # ← なくても docstring があれば OK

def validate_systolic(bp: int) -> None:
    """120〜250 以外なら BloodPressureError"""
    if not (120 <= bp <= 250):
        raise BloodPressureError(f"異常値: {bp}")

def demo() -> None:
    for bp in (130, 80, 260):
        try:
            validate_systolic(bp)
            print(f"{bp}: ✅ 正常")
        except BloodPressureError as e:
            print(f"{bp}: ❌ {e}")

if __name__ == "__main__":
    demo()