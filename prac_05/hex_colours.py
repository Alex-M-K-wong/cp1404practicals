HEX_COLOURS = {
    "aliceblue": "#f0f8ff",
    "burnished brown": "#a17a74",
    "burnt orange": "#cc5500",
    "cadet blue": "#5f9ea0",
    "cadmium red": "#e30022",
    "camel": "#c19a6b",
    "caribbean green": "#00cc99",
    "chartreuse1": "#7fff00",
    "chocolate": "#d2691e",
    "coral": "#ff7f50"
}

color_name = input("Enter a colour name: ").strip().lower()
while color_name != "":
    try:
        print(f"{color_name.title()} is {HEX_COLOURS[color_name]}")
    except KeyError:
        print("Invalid colour name")
    color_name = input("Enter a colour name: ").strip().lower()

