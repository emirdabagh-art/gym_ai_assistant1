def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def test_bmi():
    result = calculate_bmi(95, 184)

    if result > 0:
        print("BMI Test Passed")

    else:
        print("BMI Test Failed")


test_bmi()
