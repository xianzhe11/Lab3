import Lab2.bmi as bmi

print("Test_BMI")

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.73,57)
    assert(result == 0)

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.73,20)
    assert(result == -1)    

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.73,100)
    assert(result == 1)