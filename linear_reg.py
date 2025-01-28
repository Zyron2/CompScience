import matplotlib.pyplot as plt

# Input data from the user
print("Enter the X values separated by spaces:")
X = list(map(float, input().split()))
print("Enter the Y values separated by spaces:")
Y = list(map(float, input().split()))

# Check if the lengths of X and Y match
if len(X) != len(Y):
    print("Error: X and Y must have the same number of elements.")
else:
    # Calculate the mean of X and Y
    mean_x = sum(X) / len(X)
    mean_y = sum(Y) / len(Y)

    # Calculate slope (m) and intercept (b)
    numerator = sum((X[i] - mean_x) * (Y[i] - mean_y) for i in range(len(X)))
    denominator = sum((X[i] - mean_x) ** 2 for i in range(len(X)))
    m = numerator / denominator
    b = mean_y - m * mean_x

    # Predict Y values using the regression line
    Y_pred = [m * x + b for x in X]

    # Output the slope and intercept
    print(f"Slope (m): {m}")
    print(f"Intercept (b): {b}")

    # Plot the original data and the regression line
    plt.scatter(X, Y, color='blue', label='Data points')
    plt.plot(X, Y_pred, color='red', label='Regression line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression')
    plt.legend()
    plt.show()
