import plates
def main():
    print(test_plates_starting_with_atlest_two_letters())
    print(test_plates_with_more_than_6_chars())
    print(test_plates_with_alphaneumeric())
    print(test_plates_with_all_alpha_chars())
    print(test_plates_with_neumeric())
    print(test_plates_with_period_space_and_punchuation_marks())

def test_plates_starting_with_atlest_two_letters():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("C") == False

def test_plates_with_more_than_6_chars():
    assert plates.is_valid("Cs505050505") == False

def test_plates_with_alphaneumeric():
    #numbers should always be at the end
    #numbers shouldnt be the middle or start
    #first num cant be 0
    assert plates.is_valid("AAA222") == True
    assert plates.is_valid("AAA22A") == False
    assert plates.is_valid("dec007") == False
    assert plates.is_valid("CS50P") == False

def test_plates_with_all_alpha_chars():
    assert plates.is_valid("OUTATIME") == False

def test_plates_with_neumeric():
    assert plates.is_valid("123456") == False

def test_plates_with_period_space_and_punchuation_marks():
    assert plates.is_valid("ABC..32") ==  False
    assert plates.is_valid("ABC_ ?9") == False
    assert plates.is_valid("PI3.14") == False

if __name__ == "__main__":
    main()