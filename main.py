from sphere import Sphere
from cylinder import Cylinder


def main():
    shapes = []

    while True:
        choice = input("\nEnter shape (sphere/cylinder) or 'done' to finish: ").lower()

        if choice == 'done':
            break

        try:
            if choice == "sphere":
                r = float(input("Enter radius: "))
                if r <= 0:
                    raise ValueError("Radius must be positive")
                shapes.append(Sphere("Red", r))

            elif choice == "cylinder":
                r = float(input("Enter radius: "))
                h = float(input("Enter height: "))
                if r <= 0 or h <= 0:
                    raise ValueError("Dimensions must be positive")
                shapes.append(Cylinder("Blue", r, h))

            else:
                print("Invalid shape. Please try again.")
                continue

        except ValueError as e:
            print("Error:", e)
            continue

    print("\n--- Summary ---")
    for shape in shapes:
        print("\nType:", shape.get_type())
        print("Volume:", shape.volume())
        print("Surface Area:", shape.surface_area())
        shape.draw()


if __name__ == "__main__":
    main()
