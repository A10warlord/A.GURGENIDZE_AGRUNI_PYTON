def write_foundation_lisp(path):
    colW = 500          # Column width (X direction)
    colH = 500          # Column length (Y direction)
    colHeight = 1200    # Column height in section (Python controls this)
    edgeX = 350         # Edge offset (foundation edge → column)
    edgeY = 350
    anchor_len = 300    # Anchorage length
    vbars_count = 8     # Number of vertical bars
    vbars_diam = 16     # Diameter of vertical bars
    stirrup_diam = 8
    stirrup_spacing = 100

    data = {
        "colW": colW,
        "colH": colH,
        "colHeight": colHeight,
        "edgeX": edgeX,
        "edgeY": edgeY,
        "anchorLen": anchor_len,
        "vbarsCount": vbars_count,
        "vbarsDiam": vbars_diam,
        "stirrupDiam": stirrup_diam,
        "stirrupSpacing": stirrup_spacing,
    }

    with open(path, "w", encoding="utf-8") as f:
        f.write("(setq FND_DATA\n  (list\n")
        for k, v in data.items():
            f.write(f"    (cons '{k} {float(v)})\n")
        f.write("  )\n)\n")


if __name__ == "__main__":
    write_foundation_lisp(r"C:/foundation/foundation_F1.lsp")