from ex7a_turn_angle_module_ajm1115 import *

import turtle


# Test program
if __name__ == "__main__":
    # Test inputs and expected values
    side_lengths = [3, 4, 5, 6]
    expected_angles = [120.0, 90.0, 72.0, 60.0]
    computed_angles = []

    # Set up the turtle graphics window
    turtle.title("Ex 7a Turn Angle")
    
#Name of program coder and module coder
    print("Test Program Coder name:      Omarion Neal")
    print()
    print("Function module coder name:   Andre Marcano-Torres")
    print()

    # Print the test table header
    print("   Num Side    | Expected Angle   | Computed Angle   | Pass/Fail")
    print("               |     (deg)        |      (deg)       |")
    
count = 0

    # Draw polygons and compute angles
for i in range(len(side_lengths)):
        num_sides = side_lengths[i]
        expected_angle = expected_angles[i]

        # Compute the turn angle
        computed_angle = compute_turn_angle(num_sides)
        computed_angles.append(computed_angle)

        # Check if the computed angle matches the expected angle
        if abs(computed_angle - expected_angle) < 0.01:
            pass_fail = "Pass"
            count += 1
        else:
            pass_fail = "Fail"
            

    
        # Print the test results
        print(F"  {num_sides:^12} | {expected_angle:^15}  |{computed_angle:^15}   | {pass_fail:^8}")

print(f"{count}/4 Test Passed")

    # Draw polygons with different starting points
for i in range(len(side_lengths)):
        num_sides = side_lengths[i]
        turtle.penup()
        turtle.goto(-80  * i, i * 10)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(40)
            turtle.right(computed_angles[i])
            

    # Close the turtle graphics window on click
turtle.exitonclick()

