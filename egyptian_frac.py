import sys
def egyptian_fraction(numerator, denominator):
    result = []

    while numerator != 0:
        unit_fraction_denominator = -(-denominator // numerator)  # Ceiling division
        result.append(unit_fraction_denominator)

        # Update the numerator and denominator
        numerator = numerator * unit_fraction_denominator - denominator
        denominator = denominator * unit_fraction_denominator

    return result

numerator_1 = int(input())
denominator_1 = int(input())

output_1 = egyptian_fraction(numerator_1, denominator_1)
for unit_fraction in output_1:
    print(unit_fraction)
